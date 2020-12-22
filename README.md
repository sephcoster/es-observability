# es-observability
A utility library for CI tools to connect to Elasticsearch instances to return data

This script returns a few basic telemetry items so you can validate what's going on in a cloud environment to which you may not have console or other access including:
- Cluster health / info
- Cluster indices (`_cat/indices`)
- Index information / field mapping (if index name provided)
- Index counts (if name provided)
- Index field mapping
- A sample query for your index (when index name provided)

## ENV Requirements
Currently this is optimized for AWS / Key-based requests to elasticsearch clusters. If you would like to update to login / password it would require some small tweaks around the `get_aws_es_connection` method.

To connect using this script you'll need the following:
- `ES_HOST` (your host location)
- `AWS_ES_SECRET_KEY` (what it sounds like)
- `AWS_ES_ACCESS_KEY` (what it sounds like)

Port is currently hard-set at 443 but is easily changed.

## Parameters
The script accepts a couple of ENV parameters that can be set using parameterized build properties in Jenkins or directly via bash / command line:
- ES_INDEX_NAME (the name of the index you want to view in more detail)
- ES_ALIAS (If you would like to get information about an active alias, use this instead of the index name)
- ES_QUERY_STRING (The Query String Query you would like to run as a test against the index or alias above. It will be inserted into the `es.search` query_string.
