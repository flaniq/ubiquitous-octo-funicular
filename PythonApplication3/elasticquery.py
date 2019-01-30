import json
from elasticsearch import Elasticsearch
es = Elasticsearch(['https://dev-logs.cnetcontent.com:9201'], 
                   http_auth=('admin', 'n71yJoMLHE9N'), 
                   verify_certs=False)

#query_body1 = json.dumps({"query":{"bool":{"must":[{"term":{"manufacturer_name":"Lenovo"}},{"terms":{"attributes.5471.value_id":["641176"]}}]}}})

query_body =  {        
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "manufacturer_name": "Lenovo"
          }
        },
        {
          "terms": {
            "product_line_id": [
              389832,379361,387323,445594,429610,492511,379364,446674
            ]
          }
        }
      ]
    }
  }
}

query_alias = es.indices.get_alias('*');
query_response = es.search(index="*",body = query_body)
print("%d documents found" % query_response['hits']['total'])
output = query_response['hits']['total']