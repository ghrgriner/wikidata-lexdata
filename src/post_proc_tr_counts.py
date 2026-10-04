'''Post-process translation counts: mostly to add labels and rank to languages

We also create truncated counts here, but we might move that to the R file
that creates the heatmap so that any changes to the truncation level need
only be done in one place.

Of course, this all could also be done in the R program that makes the
heatmap, but we'll do it in Python as we think there are more programmers
regularly using Python than R.
'''

import csv
import pandas as pd

#-----------------------------------------------------------------------------
# Parameters
#-----------------------------------------------------------------------------
INPUT_FILE = '../output/count_tr_sense_top_langs.tsv'
TRUNC_MD_FILE = '../output/tr_trunc_main.md'
OUTPUT_FILE = '../output/count_tr_sense_top_langs_pp.tsv'

#-----------------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------------
INPUT_LANG_LABEL_FILE = '../input/lang_labels.tsv'

#-----------------------------------------------------------------------------
# Functions
#-----------------------------------------------------------------------------
def remove_qmark(x):
    if x[0] == '?': return x[1:]
    else: return x

def make_uniq_label(row):
    if row['dup']:
        return row['itemLabel'] + ' (' + row['itemQ'] + ')'
    else:
        return row['itemLabel']

def post_proc_tr_counts(input_file, output_file,
                        trunc_md_file=None):
    df = pd.read_csv(input_file, sep='\t', quoting=csv.QUOTE_NONE)

    df = df.rename(columns=remove_qmark)
    init_vars = list(df.columns)

    dfl = pd.read_csv(INPUT_LANG_LABEL_FILE, sep='\t', quoting=csv.QUOTE_NONE)
    dfl['itemQ'] = dfl.item.map(
        lambda x: x.replace('http://www.wikidata.org/entity/', ''))
    # delete this 'English', it is town in United States. When selecting
    # lexemes that uses this, only one lexeme is returned (L1548780) and this
    # lexeme was deleted in Dec 2025, 10 months before the query was run.
    # Known bug, see: https://phabricator.wikimedia.org/T407702
    # SELECT ?l WHERE { ?l a ontolex:LexicalEntry; dct language wd:2017605 }
    dfl = dfl[ dfl.itemQ != 'Q2017605' ]
    dfl['dup'] = dfl.itemLabel.duplicated(keep = False)
    dfl['itemUniqLabel'] = dfl.apply(make_uniq_label, axis=1)
    if dfl.dup.any():
        print('Duplicate language labels had item name added.')
        print(f'(These languages might not be used in {INPUT_FILE}.)')
        print(dfl[dfl.dup][['item','itemLabel','itemUniqLabel']])

    # put the resource IRI in brackets to match what is in `df`
    dfl['bitem'] = dfl.item.map(lambda x: '<' + x + '>')

    df = df.merge(dfl[['bitem','itemUniqLabel']],
                  left_on='lang', right_on='bitem').rename(
            columns = {'itemUniqLabel': 'langLabel'}).drop(['bitem'], axis=1)
    df = df.merge(dfl[['bitem','itemUniqLabel']],
                  left_on='targ', right_on='bitem').rename(
            columns = {'itemUniqLabel': 'targLabel'}).drop(['bitem'], axis=1)

    df_order = df[ df.lang == df.targ ].copy()
    df_order = df_order.sort_values(
        ['nSense','lang'],
        ascending=[False, True]).reset_index(drop=True).reset_index()
    df_order['rank'] = df_order['index'] + 1

    df = df.merge(df_order[['lang','rank']], how='left', on='lang').rename(
             columns = {'rank': 'langRank'})
    df = df.merge(df_order[['targ','rank']], how='left', on='targ').rename(
             columns = {'rank': 'targRank'})

    df_out = df[ df.lang != df.targ].copy()

    print()
    print(df_out['nsAny'].describe())

    df_out['nsAnyTrunc10k'] = df_out.nsAny.map(
        lambda x: x if x < 10000 else 10000)

    df_trunc=df_out[df_out.nsAny > 10000][['langLabel','targLabel',
                   'nSense','nsAny','nsAnyTrunc10k']].sort_values(
                            by='nsAny', ascending=False)
    print()
    print(df_trunc)
    df_trunc['md_row'] = (
        '| ' + df_trunc.langLabel +
       ' | ' + df_trunc.targLabel +
       ' | ' + df_trunc.nsAny.map(lambda x: str(round(x / 1000))) +
       ' |')
    if trunc_md_file is not None:
        df_trunc['md_row'].to_csv(trunc_md_file, sep='\t',
                                  quoting=csv.QUOTE_NONE, index=False)

    print()
    print(df_out['nsAnyTrunc10k'].describe())

    out_vars = (['langLabel', 'targLabel', 'langRank', 'targRank'] + init_vars
                + ['nsAnyTrunc10k'])
    df_out = df_out.sort_values(['langLabel','targLabel'])
    df_out[out_vars].to_csv(output_file, sep='\t',
                            quoting=csv.QUOTE_NONE, index=None)

    #print(df)
    #print(dfl)

#-----------------------------------------------------------------------------
# Main entry point
#-----------------------------------------------------------------------------
post_proc_tr_counts(INPUT_FILE, OUTPUT_FILE, trunc_md_file=TRUNC_MD_FILE)
