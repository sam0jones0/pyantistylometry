## Initial Research Notes

### Key Features:
- Frequency of uppercase words (see whiteprints feature set for others)
- Number of words that occur exactly once in the text.
- Word-based features are limited to stylistic “function words” (https://en.wikipedia.org/wiki/Function_word)
- Frequency of bi-words (two words occurring in a certain order) and tri-words (three words occurring in a certain order)?
- Bigrams (two characters in a row) and trigrams (three characters) and other n-grams?
- The question is basically this: what is the ‘signal’ and what is the ‘noise’? What can be used to discriminate between many potential authors or options and pick the right one?
- Writer invariant, also called authorial invariant or author's invariant
- word frequencies since these features are generally acknowledged to be effective for authorship attribution and are transparent, which allows the author to easily incorporate the information for document modification purposes.
- Support vector machines (SVMs)

### Adversarial:
- Proper spelling and grammar, and avoiding region specific spelling, among other things like the over use of slang, memes, and shorthand (Chat speak…etc).
- Rao and Rohatgi 2000 suggested round-trip machine translation
- Only allow top-n most common words / warnings for uncommon words.
- morphology or stemming may be required / Synonym list for uncommon words to common words (Stemming / Lemminisation)?
- Randomized change of punctuation – including brackets and so.
- Whiteprints feature set
- Function word removal / randomization
- Insertion of false random trigrams/n-grams
- Random misspelling perhaps better than enforced perfect spelling as spellchecker may miss something.
- "The first step is to identify the set of authors K(including A) that could have possibly written the document. This can be a set of co-workers or a set of authors who have published on the topic. Once the authors have been selected, a suitable corpus for each author needs to be gathered. This can be emails or newsgroup postings or other documents."  -- Kacmarcik, G., & Gamon, M. (2006, July)

### Blogs:
- https://33bits.wordpress.com/2012/02/20/is-writing-style-sufficient-to-deanonymize-material-posted-online/
- https://paranoidsbible.tumblr.com/post/182527122939/preventing-stylometry
- https://programminghistorian.org/en/lessons/introduction-to-stylometry-with-python
- https://peterkirby.com/basic-stylometry-101.html
- https://33bits.wordpress.com/2012/02/20/is-writing-style-sufficient-to-deanonymize-material-posted-online/

### Existing Solutions:
- https://github.com/psal/anonymouth
- https://github.com/travis-crow/Worden/
- https://www.philocomp.net/texts/signature.htm

### Existing Stylometry Libs:
- https://github.com/jpotts18/stylometry/issues/12
- https://github.com/psal/jstylo

### Concepts:
- https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation
- https://en.wikipedia.org/wiki/Information_retrieval
- https://en.wikipedia.org/wiki/Statistically_improbable_phrase
- Stemming is the ability to take a word such as "running" and trace it back to its 
original form to the word "run".

### Motivations:
- "the desire to avoid retribution from an employer or government agency. Beyond the issue of personal privacy, the public good is often served by whistle-blowers who expose wrong- doing in corporations and governments. The loss of an expectation of privacy can result in a chill- ing effect where individuals are too afraid to draw attention to a problem, because they fear being discovered and punished for their actions." -- Kacmarcik, G., & Gamon, M. (2006, July)

### Caveats of This Tool
- Verification effort still required. Not a one shot and done.
- Contextual information cannot easily be removed in an automated fashion.
- The tool will leave a distinctive stylometric signature.
- "Proposing feature insertion sites can be more problematic." -- Kacmarcik, G., & Gamon, M. (2006, July)
- "modifying the document to increase or decrease the frequency of a term will necessarily impact the frequencies of other terms and thus affect the document's stylometric signature." -- Kacmarcik, G., & Gamon, M. (2006),

### Research Papers
- (READ) Kacmarcik, G., & Gamon, M. (2006, July). Obfuscating document stylometry to preserve author anonymity. In Proceedings of the COLING/ACL 2006 Main Conference Poster Sessions (pp. 444-451).
- (__METHODOLOGY__) Brennan, M. R., & Greenstadt, R. (2009, April). Practical attacks against authorship recognition techniques. In Twenty-First IAAI Conference.
- Brennan, M., Afroz, S., & Greenstadt, R. (2012). Adversarial stylometry: Circumventing authorship recognition to preserve privacy and anonymity. ACM Transactions on Information and System Security (TISSEC), 15(3), 1-22.
- Emmery, C., Kádár, Á., & Chrupała, G. (2021). Adversarial stylometry in the wild: Transferable lexical substitution attacks on author profiling. arXiv preprint arXiv:2101.11310.
- Brocardo, M. L., Traore, I., Saad, S., & Woungang, I. (2013, May). Authorship verification for short messages using stylometry. In 2013 International Conference on Computer, Information and Telecommunication Systems (CITS) (pp. 1-6). IEEE.
- Abbasi, A., & Chen, H. (2008). Writeprints: A stylometric approach to identity-level identification and similarity detection in cyberspace. ACM Transactions on Information Systems (TOIS), 26(2), 1-29.
- Horton, T. B. (1987). The Effectiveness of the Stylometry of Function words in Discriminating between Shakespeare and Fletcher.
- Neal, T., Sundararajan, K., Fatima, A., Yan, Y., Xiang, Y., & Woodard, D. (2017). Surveying stylometry techniques and applications. ACM Computing Surveys (CSuR), 50(6), 1-36.
- Afroz, S., Islam, A. C., Stolerman, A., Greenstadt, R., & McCoy, D. (2014, May). Doppelgänger finder: Taking stylometry to the underground. In 2014 IEEE Symposium on Security and Privacy (pp. 212-226). IEEE.
- Tweedie, F. J., Singh, S., & Holmes, D. I. (1996). Neural network applications in stylometry: The Federalist Papers. Computers and the Humanities, 30(1), 1-10.
- Narayanan, A., Paskov, H., Gong, N. Z., Bethencourt, J., Stefanov, E., Shin, E. C. R., & Song, D. (2012, May). On the feasibility of internet-scale author identification. In 2012 IEEE Symposium on Security and Privacy (pp. 300-314). IEEE.
- Narayanan, A., & Shmatikov, V. (2008, May). Robust de-anonymization of large sparse datasets. In 2008 IEEE Symposium on Security and Privacy (sp 2008) (pp. 111-125). IEEE.
- Narayanan, A., & Shmatikov, V. (2019). Robust de-anonymization of large sparse datasets: a decade later. May, 21, 2019.
- Brocardo, M. L., Traore, I., & Woungang, I. (2015). Authorship verification of e-mail and tweet messages applied for continuous authentication. Journal of Computer and System Sciences, 81(8), 1429-1440.
- Brocardo, M. L., Traore, I., & Woungang, I. (2014, May). Toward a framework for continuous authentication using stylometry. In 2014 IEEE 28th International Conference on Advanced Information Networking and Applications (pp. 106-115). IEEE.
- Vosoughi, S., Zhou, H., & Roy, D. (2015, December). Digital stylometry: Linking profiles across social networks. In International Conference on Social Informatics (pp. 164-177). Springer, Cham.
- Zheng, R., Li, J., Chen, H., & Huang, Z. (2006). A framework for authorship identification of online messages: Writing‐style features and classification techniques. Journal of the American society for information science and technology, 57(3), 378-393.
- Daelemans, W. (2013, March). Explanation in computational stylometry. In International conference on intelligent text processing and computational linguistics (pp. 451-462). Springer, Berlin, Heidelberg.
- Koppel, M., Schler, J., & Mughaz, D. (2004, January). Text categorization for authorship verification. In Eighth International Symposium on Artificial Intelligence and Mathematics. Fort Lauderdale, Florida, http://rutcor. rutgers. edu/~ amai/aimath04/SpecialSessions/Koppel-aimath04. pdf.

### Round-trip machine translation example:

#### Original
Taking the basics of the English language, you construct whatever you wish to say and then use a service like Google Translate and have it translated to another language. Once that is done, you translate it once more to another language and then back to English. With minor “fixes” you’ll be able to create a style of posting that reads as if it was written by a non-native English speaker.

#### Round-tripped (Google)
When you learn the basics of English, you create what you want to say and then use a service like Google Translate and translate it into another language. Once this is done, you will translate it into the other language once more and then back into English. With a few tweaks, you can create a post style that reads as if it were written by a non-English native.

#### Round-tripped (ArgosTranslate)
With the basics of English, you build what you mean, and then you hear a service like a google translation, and you translated it into another language; After you did, you translate it back into another language and then you return to English, with less correction, you can create a style of publication that says it was written by an unmarried English speaker.

#### SpaCy Lemminization
Take the basic of the english language, you construct whatever you wish to say and then use a service like Google Translate and have it translate to another language. Once that be do, you translate it once more to another language and then back to English. With minor "fix" you’ll be able to create a style of post that read as if it be write by a non-native english speaker.
