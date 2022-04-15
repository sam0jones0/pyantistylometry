### Proposed Features

- Round trip machine translation followed by manually correcting errors -- Rao and Rohatgi (2000)
  - "the synonym method was especially resistant [to machine translation]" -- Brennan, M., Afroz, S., & Greenstadt, R. (2012)
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
- word2vec
- l3375p34k
  - "This means if we deliberately misspell important words, we can easily convert those important words to “unknown” (i.e., words not in the dictionary). The unknown words will be mapped to the “unknown” embedding vector in deep learning modeling. Our results strongly indicate that such simple strategy can effectively force text classification models to behave incorrectly." -- Li, J., Ji, S., Du, T., Li, B., & Wang, T. (2018)
- GloVe: Global Vectors for Word Representation: https://github.com/stanfordnlp/GloVe
- BERT-based Lexical Substitution -- Zhou, W., Ge, T., Xu, K., Wei, F., & Zhou, M. (2019, July).

### Brennan, M., Afroz, S., & Greenstadt, R. (2012)

- Neural Network, the Basic-9 Feature Set and SVM classifiers. **(medium accuracy)**
  - include nine linguistic measurements: number of unique words, lexical density, Gunning-Fog readability index, character count without whitespace, average syllables per word, sentence count, average sentence length, and the Flesch-Kincaid Readability Test
- Vocabulary Frequency / Synonym-Based **(medium-high accuracy)**
  - when a word has a large number of synonyms, the choice the author makes is significant in understanding his or her writing style -- Clark and Hannon 2007
  - synonyms that the word has according to Princeton’s WordNet lexical database
- Support Vector Machine and the Writeprints-Static Approach **(Highest accuracy)**
  - "Writeprints Static feature set. It contains 557 static features, detailed in Table II. We applied this feature set to a Support Vector Machine (SVM) classifier in the form of a Sequential Minimal Optimization (SMO) with a polynomial kernel using Weka machine learning software."
- Round-trip machine translation
  - Reduces attribution of synonym method by ~10-15% with EN-DE-JA-EN
- "if it is possible to create a generic writing style by automated means."

### (Anonymouth) McDonald, A. W., Afroz, S., Caliskan, A., Stolerman, A., & Greenstadt, R. (2012, July)
- "none of the participants in our study were able to anonymize themselves using the Writeprints (Limited) features."
- "Sufficient anonymity can be achieved after changing 13.79% (96 out of 696) of the [top Writeprints (Limited) features] features."
- "87.5% of the successful participants (7/8) increased average sentence length and decreased sentence count. Average syllable count was increased in 75% of the cases."

### Emmery, C., Kádár, Á., & Chrupała, G. (2021)
- we focus on lexical substitution of content words strongly related to a given label, as those have been shown to explain a significant portion of the accuracy of stylometric models

### (Textbugger) Li, J., Ji, S., Du, T., Li, B., & Wang, T. (2018)
- Textbugger:
  - (1) Insert: Insert a space into the word3. Generally, words are segmented by spaces in English. Therefore, we can deceive classifiers by inserting spaces into words.
  - (2)Delete: Delete a random character of the word except for the first and the last character.
  - (3) Swap: Swap random two adjacent letters in the word but do not alter the first or last letter4. This is a common occurrence when typing quickly and is easy to implement.
  - (4) Substitute-C (Sub-C): Replace characters with visually similar characters (e.g., replacing “o” with “0”, “l” with “1”, “a” with “@”) or adjacent characters in the keyboard (e.g., replacing “m” with “n”).
  - (5) Substitute-W(Sub-W): Replace a word with its topk nearest neighbors in a context-aware word vector space.
  - Original / Insert / Delete / Swap / Sub-C / Sub-W
  - foolish / f oolish / folish / fooilsh / fo0lish / silly

### Emmery, C., Kádár, Á., & Chrupała, G. (2021)
- Our attack framework extends TextFooler (TF, Jin et al., 2020) in several ways. First, a substitute gender classifier is trained, from which the logit output given a document is used to rank words by their prediction importance through an omission score(Section 3.1). For the top most important words, substitute candidates are proposed, for which we add two additional techniques (Section 3.2). These candidates can be checked and filtered on consistency with the original words (by their POS tags, for example), accepted as-is, or re-ranked (Section 3.3). For the latter, we add a scoring method. Finally, the remaining candidates are used for itera- tive substitution until TF’s stopping criterion is met(i.e., the prediction changes, or candidates run out)
- To create D<sub>ADV</sub> , a minimum number of edits is preferred, and thus we rank all words in D by their omission score (similar to e.g., Kádár et al.,2017) according to f' (omission score in Algorithm 1)
- Lexical Substitution Attacks (see p5, section 4.2 for details)
  - Synonym Substitution (WS)
  - Masked Substitution (MB): The embedding-based substitutions can be replaced by a language model predicting the contextually most likely token. BERT (Devlin et al., 2019)—a bi-directional encoder (Vaswani et al., 2017) trained through masked language modeling and next-sentence prediction—makes this fairly trivial.
  - Dropout Substitution (DB) A method to circumvent the former (i.e., BERT’s masked prediction limitations for lexical substitution), was presented by Zhou et al. (2019).
  - Heuristic Substitution: i.e. Textbugger like perturbations. 
- Candidate Filtering and Re-ranking (semantic consistency checks)
  - Part-of-Speech and Document Encoding: Remove subtitute token if POS tag differs from original.