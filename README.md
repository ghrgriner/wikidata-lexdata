# Overview

This is a small repository with queries for Wikidata lexicographical
data. We have run some of the queries and present the results.

In particular, this repository contains:

- Queries for counting senses with at least one translation to various
  target languages. We analyze the fifty languages in Wikidata with the
  most senses and present the results in the wiki of this repository.

- Description and comments for setting up a local SPARQL endpoint with
  just the lexicographical data using Apache Jena.

See [LICENSE.txt](LICENSE.txt) for complete license and attribution
details for Wikidata and for this repository.

# Files with Example Queries

There are some remarks provided as comments in the files. There may be some
other example queries embedded in wiki pages (see link to wiki below).

1. [extract\_en\_lang\_labels.rq](src/extract\_en\_lang\_labels.rq):
   Extract the languages used on all lexical entries and their English
   labels. We ran this on the Wikidata Query Service (WDQS) to generate
   `output/lang_labels.tsv`. The purpose here is that we run some of the
   queries below on our own SPARQL endpoint. We loaded only the
   lexicographical data dump into our own database, and the language
   labels aren't present in this dump.

2. [tr\_sense\_counts\_top\_langs.rq](src/tr\_sense\_counts\_top\_langs.rq):
   Counts senses with at least one translation for the top 50 languages.
   The results from this query are presented on the wiki. This query will
   timeout if run on the WDQS.

3. [tr\_sense\_counts\_sel\_langs.rq](src/tr\_sense\_counts\_sel\_langs.rq):
   This is the same query as above, but replacing the top 50 languages with
   one source language and one translation target language. We have successfully
   run this query on the WDQS.

# Wiki

The repository [wiki](https://github.com/ghrgriner/wikidata-lexdata/wiki) has
some further discussion.
The wiki home page linked above has the recommended reading order.

# References

