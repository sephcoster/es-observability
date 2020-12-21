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

def main():
    index_name = os.environ.get('ES_INDEX_NAME')
    es = get_aws_es_connection()

    logger = setup_logging('complaint')
    
    cluster_info = es.info()
    logger.info('Cluster Information: {}'.format(cluster_info) )
    
    cluster_health = es.cluster.health()
    logger.info('Cluster Health: {}'.format(cluster_health) )
    
    cluster_indices = es.cat.indices()
    logger.info('Cluster Indices Available: {}'.format(cluster_indices) )
    
    logger.info('Index value: ')
    logger.info(index_name)

if __name__ == '__main__':
    main()  
