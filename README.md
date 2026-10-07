# Overview

This is a small repository with queries for Wikidata lexicographical
data. We have run some of the queries and present the results.

In particular, this repository contains:

- Queries for counting senses with at least one translation to various
  target languages and a partial comparison to the English-language
  Wiktionary.
  - We analyze the fifty languages in Wikidata with the
    most senses and present counts for each of the 2450 analyzed
    source language by target language combinations. The results are
    presented graphically in the wiki of this repository and the file
    with counts is made available for download.
  - We count not only the Wikidata 'translation' property, but also the
    'item for this sense' property, the 'denonym of' property, and the
    'predicate for' property. We generate sense counts separately by
    property and overall. Sensitivity analyses also (1) count senses
    where the translation can be found from a synonym, (2) where a
    reversed 'translation' property path is considered, or (3)
    where sense glosses are also counted as translations.
  - We provide a partial comparison of counts to the English-language
    Wiktionary for cases where English is the target language in the
    sensitivity analysis which includes sense glosses.
    For languages with more than 10,000 translations in Wiktionary or
    Wikidata, we report which source has more translations.
    - Results: we found that while usually (69 languages) Wiktionary
      has the higher counts, Wikidata has the higher counts (listed in
      thousands) for Bokmål (50 vs 30), Nynorsk (33 vs 28),
      Egyptian (18 vs 8), Sumerian (17 vs 2), Akkadian (16 vs 1) and
      Northern Sami (10 vs 5).

- Description and comments for setting up a local SPARQL endpoint with
  just the lexicographical data using Apache Jena.

See [LICENSE.txt](LICENSE.txt) for complete license and attribution
details for Wikidata and for this repository.

# Files with Example Queries

There are some remarks provided as comments in the files. There may be some
other example queries embedded in wiki pages (see link to wiki below).
In general the
[Methods](https://github.com/ghrgriner/wikidata-lexdata/wiki/Methods) page
in the wiki provides a link to the query that is used to conduct each
analysis it describes.

1. [extract\_en\_lang\_labels.rq](src/extract\_en\_lang\_labels.rq):
   Extract the languages used on all lexical entries and their English
   labels. We ran this on the Wikidata Query Service (WDQS) to generate
   `input/lang_labels.tsv`. The purpose here is that we run some of the
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

