### Proposed Features

- Round trip machine translation followed by manually correcting errors -- Rao and Rohatgi (2000)
- Normalise idiosyncratic formatting, language use and spelling (Misspellings, typos or region-specific spelling/slang) with grammar/spell-checking -- Rao and Rohatgi (2000)
- Randomise or normalise function words (while vs whilst / whoever vs whom vs whomever vs whose)
- Whiteprint features perturbation
- Syntactic information removal -- Rao, J. R., & Rohatgi, P. (2000)
    - Length of sentences and paragraphs.
    - Number of words and paragraphs.
    - Paragraph style: This includes the indentation style and the spacing between paragraphs.
    - Words, Phrases and their frequency: This includes the vocabulary of the user.
    - Misspelled words and their frequency.
    - Capitalized words and their frequency.
    - Hyphenated words and their frequency.
    - Punctuation usage: including usage of hyphens: - vs. - vs. --.
    - Choice of acceptable uses of words or phrases: That is, choices taken when there is more than one alternative such as, British vs. American spelling and ``I'm'' vs. ``I am''. 
    - eystroke fingerprinting, for example in conjunction with Javascript
- Other Features
  - stylistic flourishes
  - abbreviations
  - spelling preferences and misspellings
  - language preferences
  - number of unique words
  - regional linguistic preferences in slang, idioms and so on
  - sentence/phrasing patterns
  - word co-location (pairs)
  - use of formal/informal language
  - function words
  - vocabulary usage and lexical density
  - character count with white space
  - average sentence length
  - average syllables per word
  - synonym choice
  - expressive elements like colors, layout, fonts, graphics, emoticons and so on
  - analysis of grammatical structure and syntax

### Brennan, M., Afroz, S., & Greenstadt, R. (2012)

- Neural Network, the Basic-9 Feature Set and SVM classifiers.
  - include nine linguistic measurements: number of unique words, lexical density, Gunning-Fog readability index, character count without whitespace, average syllables per word, sentence count, average sentence length, and the Flesch-Kincaid Readability Test
- Vocabulary Frequency / Synonym-Based
  - when a word has a large number of synonyms, the choice the author makes is significant in understanding his or her writing style -- Clark and Hannon 2007
  - synonyms that the word has according to Princeton’s **WordNet** lexical database
- Support Vector Machine and the Writeprints-Static Approach
  - 