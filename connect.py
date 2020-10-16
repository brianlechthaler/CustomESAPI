import elasticsearch as es

##############################################
### Elasticsearch Connection Configuration ###
##############################################

ElasticsearchIndex = 'logstash-*'
ElasticsearchAPIID = 'Your_Elasticsearch_API_ID'
ElasticsearchAPIKey = 'Your_Elasticsearch_API_Key'
ElasticsearchHost = 'https://localhost:9243'

connection = es.Elasticsearch([ElasticsearchHost], api_key=(ElasticsearchAPIID, ElasticsearchAPIKey),)
