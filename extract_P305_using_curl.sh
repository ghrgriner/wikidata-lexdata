#------------------------------------------------------------------------------
# To run:
# 1. change 'your.name@example.com' below to your email
# 2. If you are running this on or after February 2027, you might need to replace
#    'query.wikidata.org' with the v2 tool URL. See details at: https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/WDQS_backend_update/Migrate
#    The v2 tool URL is currently given as: query-next.wikidata.org 
# 3. Run the script:
#    > sh extract_P305_using_curl.sh
#------------------------------------------------------------------------------
curl -G "https://query.wikidata.org/sparql" \
  --data-urlencode "query=CONSTRUCT { ?item wdt:P305 ?tag . } WHERE { { SELECT distinct ?item WHERE { ?l a ontolex:LexicalEntry; dct:language ?item .  } } ?item wdt:P305 ?tag . }" \
  -H "Accept: text/turtle" \
  -H "User-Agent: extract_P305_using_curl.sh/2026.10.05 (https://github.com/ghrgriner/wikidata-lexdata) (your.name@example.com)" \
  -o "extracted_P305_using_curl.ttl"
