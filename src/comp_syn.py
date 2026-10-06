'''Compare sensitivity analysis allowing 'synonym' paths with main analysis.
'''

import csv
import pandas as pd

#-----------------------------------------------------------------------------
# Parameters
#-----------------------------------------------------------------------------
INPUT_FILE = '../output/count_tr_sense_top_langs_pp.tsv'
INPUT_SYN_FILE = '../output/count_tr_synsense_top_langs_pp.tsv'
COLS = ['langLabel','targLabel','nsAny']

#-----------------------------------------------------------------------------
# Main entry point
#-----------------------------------------------------------------------------

df  = pd.read_csv(INPUT_FILE, sep='\t', usecols=COLS, quoting=csv.QUOTE_NONE)
dfs = pd.read_csv(INPUT_SYN_FILE, sep='\t', usecols=COLS,
                  quoting=csv.QUOTE_NONE)

df = df.merge(dfs, how="left", on=['langLabel','targLabel'],
              suffixes=['','_syn'])

df['syn_diff'] = df.nsAny_syn - df.nsAny
print(df.syn_diff.describe())

print(df.nlargest(5, 'syn_diff'))
