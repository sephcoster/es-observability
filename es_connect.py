import json
import os

from log import setup_logging
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

def get_aws_es_connection():
    es_host = os.environ.get('ES_HOST')
    
    awsauth = AWS4Auth(
        os.environ.get('AWS_ES_ACCESS_KEY'),
        os.environ.get('AWS_ES_SECRET_KEY'),
          'us-east-1',
          'es'
        )
    
    es = Elasticsearch(
        hosts=[{'host': es_host, 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        timeout=1000
    )

    return es

def pretty_json(thing):
    return json.dumps(thing, indent=2)

def main():
    index_name = os.environ.get('ES_INDEX_NAME')
    index_alias = os.environ.get('ES_ALIAS')
    query = os.environ.get('ES_QUERY_STRING')

    es = get_aws_es_connection()

    logger = setup_logging('complaint')
    
    cluster_info = pretty_json( es.info() )
    logger.info('Cluster Information: \n {}'.format(cluster_info) )
    
    cluster_health = pretty_json( es.cluster.health() )
    logger.info('Cluster Health: \n {}'.format(cluster_health) )
    
    cluster_indices = es.cat.indices()
    logger.info('Cluster Indices Available: \n {}'.format(cluster_indices) )

    if index_alias:
        logger.info('Index Alias value: {}'.format(index_alias))
        index_count = es.count(body=None, index=index_alias)
        logger.info('Record Count: {}'.format(index_count))
        index_info = pretty_json( es.indices.get(index_alias))
        logger.info('Information about this index alias: \n {}'.format(index_info))

    if index_name:
        logger.info('Index value: {}'.format(index_name))
        index_count = es.count(body=None, index=index_name)
        logger.info('Record Count: {}'.format(index_count))
        index_info = pretty_json( es.indices.get(index_name))
        logger.info('Information about this index: \n {}'.format(index_info))

    if query:
        search = {}
        search["query"] = {
            "query_string": {
                "query": query
            }
        }
        
        search_results = pretty_json(es.search(body=search, index=index_name))
        logger.info('Example Search: {}'.format( search_results) )

if __name__ == '__main__':
    main()  
