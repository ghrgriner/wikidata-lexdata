
# Load libraries
library(ggplot2)
library(dplyr)
library(stringr)
library(forcats)

#-----------------------------------------------------------------------------
# Parameters
#-----------------------------------------------------------------------------
INPUT_FILE <- "../output/count_tr_sense_top_langs_pp.tsv"
OUTPUT_FILE <- "../output/tr_sense_heatmap.png"

#-----------------------------------------------------------------------------
# Main entry point
#-----------------------------------------------------------------------------
df = read.csv(INPUT_FILE, header=TRUE, sep='\t')

# Convert the language labels to be ordered factors so that the combination
# of the two lowest ranks is in the upper left corner of the figure
df <- df %>%
  mutate(langFact = fct_reorder(langLabel, -langRank)) %>%
  mutate(targFact = fct_reorder(targLabel, targRank))

# TODO: generate programmatically here or in the .py program
cap_line1 <- 'Translation counts over 10,000 are truncated at 10,000 for 6 cells. See table in text for details.'
cap_line2 <- paste0('Translations are senses mapping to same item using ',
                    '"item for this sense" (P5137), "demonym of" (P6271), or ',
                    '"predicate for" (P9970) or that can be reached using the ',
                    '"translation" property (P5972) in a path of length 1 or ',
                    '2.')
cap_line3 <- paste0('The fifty languages with the most senses are presented ',
                    'and ordered by the total number of senses for the ',
                    'language.')
cap_line4 <- paste0('Source: Wikidata "latest_lexemes.ttl" download file ',
                    'retrieved 21 Sep 2026')

fig_title <- 'Number of senses with at least 1 translation to target language'

cap_line1_wrap = str_wrap(cap_line1, width=99)
cap_line2_wrap = str_wrap(cap_line2, width=99)
cap_line3_wrap = str_wrap(cap_line3, width=99)
cap_line4_wrap = str_wrap(cap_line4, width=99)

ggplot(data = df, aes(x = targFact, y = langFact, fill = nsAnyTrunc10k)) +
  geom_tile(color = "white") +
  scale_fill_gradient2(
      low = "white",
      high = "red",
      name = 'N senses with\n>= 1 translation\n(truncated)') +
  labs(
      title = fig_title,
      x = 'Target Language',
      y = "Language",
      caption = paste0(cap_line1_wrap, '\n',
                       cap_line2_wrap, '\n',
                       cap_line3_wrap, '\n',
                       cap_line4_wrap)) +
  theme(
      axis.text.x = element_blank(),
      axis.tick.x = element_blank(),
      plot.caption = element_text(
          size = 8,
          face = 'italic',
          hjust = 0
          ))
ggsave(OUTPUT_FILE, width = 7, height = 7, dpi = 300)
#ggsave("heatmap.pdf", width = 7, height = 7)
