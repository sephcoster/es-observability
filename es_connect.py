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

es = get_aws_es_connection()
index_name = os.environ.get('ES_INDEX_NAME')

es.

def main():
	es = get_aws_es_connection()
	logger = setup_logging('complaint')
	logger.info('Cluster Information: ')
	es.info()
	logger.info('Cluster Health: ')
	es.cluster.health()
	logger.info('Cluster Indices Available: ')
	es.cat.indices()
	logger.info('Index value: ')
	logger.info(index_name)

if __name__ == '__main__':
    main()	
