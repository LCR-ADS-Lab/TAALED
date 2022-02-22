# Tool for the Automatic Analysis of Lexical Diversity (TAALED)
TAALED is designed to calculate classic (but flawed) indices of lexical diversity such as the type-token ratio (TTR) and root TTR (also referred to as Guiraud's index) and more newly developed indices of lexical diversity that are stable across texts of different lengths such as moving average TTR (MATTR; Covington & McFall, 2010) and the measure of textual lexical diversity (MTLD; McCarthy & Jarvis, 2010).

## Installation
To install taaled, you can use `pip`:

```bash
pip install taaled
```
While not strictly necessary, this tutorial will presume that you have also installed [pylats](https://github.com/LCR-ADS-Lab/pylats) and [spacy](https://spacy.io/) for text preprocessing.

taaled also makes use of [plotnine](https://plotnine.readthedocs.io/en/stable/installation.html) for data visualization. This package is not required for taaled to function properly, but is needed if data visualization (e.g., density plots for mtld factor lengths) are desired.

## Getting started
TAALED takes a list of strings as input and returns various indices of lexical diversity (and diagnostic information). In the rest of the tutorial, we will use [pylats](https://github.com/LCR-ADS-Lab/pylats) for preprocessing of texts (e.g., tokenization, lemmatization, word disambiguation, checking for misspelled words). Currently pylats only supports advanced features for English (models for other languages are forthcoming). However, TAALED can work with any language, as long as texts are tokenized (and appropriately preprocessed). See tools such as [spacy](https://spacy.io/), [stanza](https://stanfordnlp.github.io/stanza/), and [trankit](https://github.com/nlp-uoregon/trankit) for NLP pipelines for a wide range of languages.

### Import TAALED
```python
from taaled import ld
from pylats import lats #optional, but recommended for text preprocessing
```

### Calculating indices
Because some indices presume that texts are at least 50 words in length (see, e.g., [McCarthy & Jarvis, 2010](https://link.springer.com/article/10.3758/BRM.42.2.381); [Kyle, Crossley, & Jarvis, 2021](https://doi.org/10.1080/15434303.2020.1844205); [Zenker & Kyle, 2021](https://doi.org/10.1016/j.asw.2020.100505)), we will use a [longer text in this example](https://catalog.ldc.upenn.edu/desc/addenda/LDC2014T06.orig.txt) that conveniently is included in TAALED.

### Preprocess a text
Minimally, a text string must be turned into a flat list of strings to work with TAALED.

Ideally, a number of text preprocessing/normalization steps will be used. In the example below, the [pylats](https://github.com/LCR-ADS-Lab/pylats) package is used to tokenize, the text, remove most punctuation, add part of speech tags (for homograph disambiguation), lemmatize each word, check for (and ignore) misspelled words (misspelled words will innapropriately inflate ld values), and convert all words to lower case. [pylats](https://github.com/LCR-ADS-Lab/pylats) is quite flexible/customizable, and the taaled package includes a default parameters object `ld.params` for use with pylats.

```python
#if pylats is installed, preprocess the sample text using the default taaled parameters file
clnsmpl = lats.Normalize(ld.txtsmpl, ld.params)
print(clnsmpl.toks[:10]) #check sample output
```

```
['there_PRON', 'be_VERB', 'a_DET', 'saying_NOUN', 'in_ADP', 'my_PRON', 'language_NOUN', 'that_PRON', 'go_VERB', 'like_ADP']
```

### Calculate lexical diversity indices
Calculation of lexical diversity indices is demonstrated below with the index MATTR (moving average type token ratio). For information about the full list of lexical diversity indices calcuated by taaled, see the next section.

**Create ldvals object**
```python
#create ld object
ldvals = ld.lexdiv(clnsmpl.toks)
```
**Report mattr value**

By default, `.mattr` reports the average TTR value for all 50-word moving windows in a text (tokens 1-50, 2-51, 3-52, etc.). Higher values indicate more diverse texts.
```python
print(ldvals.mattr) #moving average TTR value
```
```
0.7922466960352423
```

**Check TTR values for each window**

```
print(ldvals.mattrs)
```

```
[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.78, 0.78, 0.78, 0.78, 0.8, 0.82, 0.84, 0.82, 0.8, 0.8, 0.82, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.78, 0.8, 0.78, 0.76, 0.76, 0.76, 0.78, 0.78, 0.78, 0.78, 0.8, 0.8, 0.78, 0.76, 0.78, 0.78, 0.8, 0.82, 0.8, 0.82, 0.82, 0.82, 0.82, 0.8, 0.82, 0.82, 0.8, 0.78, 0.78, 0.8, 0.8, 0.8, 0.8, 0.8, 0.78, 0.78, 0.8, 0.82, 0.8, 0.8, 0.78, 0.8, 0.8, 0.8, 0.8, 0.8, 0.82, 0.8, 0.82, 0.82, 0.84, 0.84, 0.86, 0.86, 0.84, 0.84, 0.86, 0.84, 0.84, 0.84, 0.84, 0.84, 0.86, 0.84, 0.84, 0.82, 0.8, 0.78, 0.78, 0.8, 0.82, 0.82, 0.82, 0.82, 0.84, 0.84, 0.86, 0.86, 0.84, 0.84, 0.84, 0.84, 0.82, 0.82, 0.8, 0.78, 0.76, 0.76, 0.76, 0.76, 0.78, 0.8, 0.8, 0.78, 0.76, 0.76, 0.76, 0.78, 0.78, 0.78, 0.78, 0.76, 0.76, 0.74, 0.76, 0.76, 0.76, 0.78, 0.78, 0.78, 0.78, 0.78, 0.76, 0.78, 0.78, 0.8, 0.8, 0.8, 0.78, 0.78, 0.76, 0.76, 0.76, 0.78, 0.78, 0.78, 0.76, 0.76, 0.78, 0.76, 0.78, 0.76, 0.76, 0.76, 0.76, 0.76, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.76, 0.78, 0.8, 0.8, 0.8, 0.8, 0.8, 0.82, 0.8, 0.8, 0.8, 0.78, 0.78, 0.8, 0.8, 0.82, 0.84, 0.82, 0.82, 0.82, 0.84, 0.84, 0.84, 0.82, 0.8, 0.8, 0.8, 0.78, 0.8, 0.78, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.78, 0.78, 0.76, 0.76, 0.78, 0.76, 0.74, 0.74, 0.74, 0.74, 0.72, 0.74, 0.74, 0.74, 0.76, 0.76, 0.74, 0.74, 0.72, 0.72]
```

**Check tokens in each window**

```python
print(ldvals.mattrwins[0]) #first window
print(ldvals.mattrwins[1]) #second window
```

```
['there_PRON', 'be_VERB', 'a_DET', 'saying_NOUN', 'in_ADP', 'my_PRON', 'language_NOUN', 'that_PRON', 'go_VERB', 'like_ADP', 'if_SCONJ', 'only_ADV', 'the_DET', 'young_ADJ', 'could_AUX', 'know_VERB', 'and_CCONJ', 'the_DET', 'old_ADJ', 'could_AUX', 'do_VERB', 'this_PRON', 'explain_VERB', 'an_DET', 'important_ADJ', 'lesson_NOUN', 'but_CCONJ', 'one_PRON', 'have_VERB', 'to_PART', 'attain_VERB', 'a_DET', 'certain_ADJ', 'degree_NOUN', 'of_ADP', 'wisdom_NOUN', 'to_PART', 'understand_VERB', 'it_PRON', 'in_ADP', 'my_PRON', 'opinion_NOUN', 'be_AUX', 'young_ADJ', 'be_AUX', 'more_ADV', 'enjoyable_ADJ', 'be_AUX', 'old_ADJ', 'may_AUX']

['be_VERB', 'a_DET', 'saying_NOUN', 'in_ADP', 'my_PRON', 'language_NOUN', 'that_PRON', 'go_VERB', 'like_ADP', 'if_SCONJ', 'only_ADV', 'the_DET', 'young_ADJ', 'could_AUX', 'know_VERB', 'and_CCONJ', 'the_DET', 'old_ADJ', 'could_AUX', 'do_VERB', 'this_PRON', 'explain_VERB', 'an_DET', 'important_ADJ', 'lesson_NOUN', 'but_CCONJ', 'one_PRON', 'have_VERB', 'to_PART', 'attain_VERB', 'a_DET', 'certain_ADJ', 'degree_NOUN', 'of_ADP', 'wisdom_NOUN', 'to_PART', 'understand_VERB', 'it_PRON', 'in_ADP', 'my_PRON', 'opinion_NOUN', 'be_AUX', 'young_ADJ', 'be_AUX', 'more_ADV', 'enjoyable_ADJ', 'be_AUX', 'old_ADJ', 'may_AUX', 'make_VERB']
```
## Overview of Indices
This documentation describes available lexical diversity (LD) indices in this package. Each section provides how each index is calculated and what to remember before using them for your functional or academic purposes. Each section is organized as follows:
1. Provide a functional definition
2. Provide a general guideline for using indices across texts of different lengths<sup>[1]</sup>
	
| Recommendation               | Index (Minimum Text Length (tokens))               |
| --------------------------- | --------------------------------------------------- |
| Use with confidence (★★★)  |[MATTR](https://github.com/LCR-ADS-Lab/taaled/blob/main/README.md#mattr) (50), [MTLD-Original](https://github.com/LCR-ADS-Lab/taaled/blob/main/README.md#mtld-original) (50)   |
| Use with caution (★★☆)      |[HD-D](https://github.com/LCR-ADS-Lab/taaled/blob/main/README.md#hd-d) (50),  [Maas](https://github.com/LCR-ADS-Lab/taaled/blob/main/README.md#maas) (100)              |
| Avoid  (★☆☆)|[MSTTR](https://github.com/LCR-ADS-Lab/taaled/blob/main/README.md#msttr),  [Log TTR](https://github.com/LCR-ADS-Lab/taaled/blob/main/README.md#log-ttr),  [Root TTR](https://github.com/LCR-ADS-Lab/taaled/blob/main/README.md#root-ttr),  [Simple TTR](https://github.com/LCR-ADS-Lab/taaled/blob/main/README.md#type-token-ratio-ttr)                 |
3. Provide information about related studies and references [**CLICK ▹LEARN MORE**]


## Classic (but flawed) LD Indices (TTR, Root TTR, Log TTR)

### Type-token ratio (TTR)<sup>★☆☆</sup>

<img src="https://latex.codecogs.com/svg.latex?\fn_cm&space;TTR&space;=&space;\frac{nTypes}{nTokens}" title="TTR = \frac{nTypes}{nTokens}" />

TTR is calculated as the number of unique words in a text (types) divided by the number of running words (tokens)(Johnson, 1944)<sup>[2]</sup>.


```python
print(ldvals.ttr)
```

```
0.5507246376811594
```

### Root TTR<sup>★☆☆</sup>

<img src="https://latex.codecogs.com/svg.latex?\fn_cm&space;Root&space;TTR&space;=&space;\frac{nTypes}{\sqrt{nTokens}}" title="Root TTR = \frac{nTypes}{\sqrt{nTokens}}" />

Root TTR is calculated as the number of types divided by the square root of the number of tokens (Guiraud, 1960, also called *Guirad's index*)<sup>[3]</sup>.

```python
print(ldvals.rttr)
```
```
9.14932483451846
```
### Log TTR<sup>★☆☆</sup>

<img src="https://latex.codecogs.com/svg.latex?\fn_cm&space;Log&space;TTR&space;=&space;\frac{log(nTypes)}{log(nTokens)}" title="Log TTR = \frac{log(nTypes)}{log(nTokens)}" />

Log TTR is calculated by dividing the logarithm of the number of word types by the logarithm of the number of word tokens (Chotlos, 1944; Herdan, 1960, also known as *Herdan's C*)<sup>[4][5]</sup>.
```python
print(ldvals.lttr)
```
```
0.8938651603109881
```
<details><summary>LEARN MORE</summary>
<p>

* TTR is perhaps the most well known LD index.
* Root TTR and Log TTR were two early attempts to correct for TTR's sensitivity to text length using simple mathematical transformations.
* TTR values are intrinsically skewed by the length of a text, wherein longer texts tend to have lower TTR scores because the proportion of repeated words increases as the text grows longer (e.g., Koizumi & In'nami, 2012; Tweedie & Baayen, 1998)<sup>[6][7]</sup>.
* Hess, Sefton, and Jandry (1986)<sup>[8]</sup> analyzed oral language samples from 83 preschool children using five LD measures that were popular at the time: simple TTR, corrected TTR (Carroll, 1964)<sup>[9]</sup>, Root TTR, Log TTR, and Characteristic K (Yule, 1944)<sup>[10]</sup>. They concluded that all these LD measures were unsuitable for comparing texts of different lengths.
* Hess, Haug, and Landry (1989)<sup>[11]</sup> used oral language samples from 52 elementary school children to analyze four versions of TTR: simple TTR, corrected TTR, Root TTR, and Log TTR. As was the case in the earlier study by Hess et al. (1986)<sup>[8]</sup>, results suggested that none of the TTR measures were stable across texts of different lengths.
* Baayen & Tweedy (1998) ... This needs to be added!
* McCarthy and Jarvis (2007)<sup>[12]</sup> used a parallel sampling technique to investigate the relationship between text length and LD indices in an L1 corpus of speaking and writing. They found that most indices (including TTR and root TTR) were strongly correlated with the text length.
* Zenker & Kyle (2021) ... This needs to be added!

</p>
</details>


## Maas

### Maas<sup>★★☆</sup>
<img src="https://latex.codecogs.com/svg.latex?\fn_cm&space;Maas&space;=&space;\frac{log(nTokens)-log(nTypes)}{log(nTokens)^{2}}" title="Maas = \frac{log(nTokens)-log(nTypes)}{log(nTokens)^{2}}" />

Maas' index is a more complex transformation of TTR that attempts to fit the value to a logarithmic curve. It is often referred to simply as *Maas* (Maas, 1972)<sup>[13]</sup>.

<details><summary>LEARN MORE</summary>
<p>

* Unlike most LD indices, lower Maas values are associated with higher LD.
* Maas can be categorized into a log-transformed approach to the measure of LD. 
* McCarthy and Jarvis (2010)<sup>[14]</sup> showed that Maas index was one of the main predictors of their register prediction model (along with MTLD and vocd-D).
* Zenker & Kyle (2021) ... This needs to be added!


</p>
</details>


## MSTTR & MATTR

### MSTTR<sup>★☆☆</sup>
The Mean-Segmental Type-Token Ratio (MSTTR) is the average TTR for successive segments of text containing a standard number of word tokens (Johnson, 1944)<sup>[2]</sup>.


### MATTR<sup>★★★</sup>
The Moving-Average Type-Token Ratio calculates the moving average for all segments of a given length. For a segment length of 50 tokens, TTR is calculated on tokens 1-50, 2-51, 3-53, etc., and the resulting TTR measurements are averaged to produce the final MATTR value (Covington & McFall, 2010)<sup>[15]</sup>.

<details><summary>LEARN MORE</summary>
<p>

* MSTTR computes TTR values for equal-sized segments (sometimes 30 words, but more typically 100 words) out of the original text and averages the values for each non-overlapping segments. The remaining words are discarded (Malvern & Richards, 2002)<sup>[16]</sup>.
* MSTTR was introduced by Johnson (1944)<sup>[2]</sup> to overcome the weakness of classical TTR. However, a number of weaknesses have been identified in this approach (Malvern & Richards, 2002)<sup>[16]</sup>.
* MATTR has been demonstrated as one of the measures that meaningfully contributes to the human judgment of LD (Kyle et al., 2021)<sup>[17]</sup>.

</p>
</details>


## HD-D

### HD-D<sup>★★☆</sup>
The hypergeometric distribution diversity index (HDD) is a more reliable calculation of *vocd-D* (Malvern & Richards, 1997)<sup>[18]</sup>. It relies on the probability that a word in a text would be included in a random sample from the text (McCarthy & Jarvis, 2007)<sup>[12]</sup>. For each word type in a text, HD-D uses the hypergeometric distribution to calculate the probability of encountering one of its tokens in a random sample of 42 tokens. These probabilities are then added together to produce the final HD-D value for the text. We convert this to the same scale as TTR for ease of interpretation.

<details><summary>LEARN MORE</summary>
<p>

* Observing that vocd-D was rapidly becoming the preferred LD measures in the field, McCarthy and Jarvis (2007)<sup>[12]</sup> conducted an assessment of its sensitivity to text length using a corpus of 23 genres taken from various corpora. As a result, they concluded that vocd-D scores were not as independent of text length. In contrast, they found a small relationship (r=.282) between text length and HD-D for longer texts (up to 2000 words).
* Koizumi and In'nami (2012)<sup>[6]</sup>, using a relatively small sample (n=38) of spoken L2 texts, found that HD-D was less affected by text length than other commonly used indices, while still reporting meaningful and significant effects.
* Zenker and Kyle (2021)<sup>[1]</sup>, using a large corpus (n = 4,542) of written L2 argumentative texts found a negligible relationship (r = 0.064) between HD-D and text length.
  
</p>
</details>


## MTLD (Original, MA-Bi, MA-Wrap)
The Measure of Textual Lexical Diversity (MTLD; McCarthy, 2005; McCarthy & Jarvis, 2010)<sup>[19][14]</sup> essentially measures the average number of tokens it takes to reach a specified TTR value (i.e., .720). There are variants of MTLD implementation.

### MTLD-Original<sup>★★★</sup>
In the McCarthy and Jarvis's (2010)<sup>[14]</sup> paper, each of the text segments (i.e., the number of tokens) maintaining the TTR values is called a "factor". In MTLD-Original (McCarthy & Jarvis, 2010)<sup>[14]</sup>, factors are computed uni-directionally from the beginning to the end of the document, using non-overlapping text segments (i.e., subsequent cycles of factor calculation starts at the next token in the text). The remaining tokens that do not make up a full factor is called a partial factor, and this is used to adjust the final MTLD score. 

### MTLD-MA-Bi<sup>★★☆</sup>
Moving-average bidirectional MTLD (MTLD-MA-Bi; McCarthy & Jarvis, 2010)<sup>[14]</sup> is a revised MTLD procedure that takes a moving-average approach to compute factors. Moving-average calculation means that MTLD-MA-Bi uses the n-th token as the starting token for an n-th factor. Accordingly, the number of words required to create a factor is calculated for each progressive word in the text until a factor cannot be completed. Bidirectional means that the same procedure is repeated in backward, from the last token in the text. The final value is calculated as the average factor lengths out of all the factors.

### MTLD-MA-Wrap<sup>★★★</sup>
Moving-average wrapped MTLD (MTLD-MA-Wrap; McCarthy & Jarvis, 2010)<sup>[14]</sup> is another revised method of calculating MTLD. Like MTLD-MA-Bi, it takes a moving-average approach to create factors. However, instead of working through the text in both directions, MTLD-MA-Wrap avoids partial factors by looping back to the text's beginning.

<details><summary>LEARN MORE</summary>
<p>
 
* Koizumi (2012)<sup>[20]</sup> evaluated MTLD (including simple TTR, Root TTR, and vocd-D) using spoken English samples from 20 Japanese adolescents. Each text was clipped to the first 200 words and then subdivided into 25 segments ranging in length from 50 to 200 tokens by parallel sampling. Results indicated that MTLD values stabilized at roughly 100 tokens, and none of the other indices produced stable values within the text length ranges included in the study.
* Koizumi and In’nami (2012)<sup>[6]</sup> used similar methods and obtained the same pattern of results. Among simple TTR, Root TTR, Maas, vocd-D, HD-D, and MTLD, MTLD was the only index that produced stable values, with stabilization occurring at around 100 tokens.
* Following the parallel sampling approach in Koizumi et al. (Koizumi, 2012; Koizumi & In'nami, 2012)<sup>[20][6]</sup>, Zenker and Kyle (2021)<sup>[1]</sup> evaluated MTLD using 4,542 argumentative essays by English learners from Asian regions. The result indicated that MTLD-Original and MTLD-MA-Wrap were robust to even shorter texts such as 50 words.
* McCarthy and Jarvis (2010)<sup>[14]</sup> observed a very low correlation between MTLD-Original and the text length (using a corpus comprising texts from a range of registers such as editorials, official documents, academic prose, fiction, etc.). They also found that MTLD had a low correlation with the simple TTR, which can be a desirable property of a lexical diversity index since the simple TTR strongly correlates with text length.


</p>
</details>



## Related Studies
<details><summary>REFERENCES</summary>
<p>

[[1]](https://www.sciencedirect.com/science/article/pii/S1075293520300660?casa_token=5idiJdzo-EgAAAAA:uEW6GcL5DgURMVTQkZ48sOukpXURAMiwOtARDnQJ1mFTdwM_XqymVTkRdYyulAacZ_1xiQ) Zenker, F., & Kyle, K. (2021). Investigating minimum text lengths for lexical diversity indices. *Assessing Writing, 47*, 100505.

[[2]](https://psycnet.apa.org/fulltext/2011-16010-001.pdf) Johnson, W. (1944). Studies in language behavior 1: A program of research. *Psychological Monographs, 56*, 1-15.
 
[[3]](https://scholar.google.com/scholar_lookup?title=Problèmes%20et%20méthodes%20de%20la%20statistique%20linguistique%20%5BProblems%20and%20methods%20of%20linguistic%20statistics%5D&author=P.%20Guiraud&publication_year=1960) Guiraud, P. (1960). *Probl`emes et m ́ethodes de la statistique linguistique [Problems and methods of linguistic statistics]*. Dordrecht: Reidel.

[[4]](https://psycnet.apa.org/fulltext/2011-16010-004.pdf) Chotlos, J. W. (1944). Studies in language behavior IV: A statistical and comparative analysis of individual written language samples. *Psychological Monographs, 56*(2),
77–111.
 
[[5]](https://scholar.google.com/scholar_lookup?title=Type-token%20mathematics%3A%20A%20textbook%20of%20mathematical%20linguistics&author=G.%20Herdan&publication_year=1960) Herdan, G. (1960). *Type-token mathematics: A textbook of mathematical linguistics*. The Hague: Mouton.
	
[[6]](https://www.sciencedirect.com/science/article/pii/S0346251X12000887?via%3Dihub) Koizumi, R., & In’nami, Y. (2012). Effects of text length on lexical diversity measures: Using short texts with less than 200 tokens. *System, 40*(4), 554–564.

[[7]](https://link.springer.com/article/10.1023%2FA%3A1001749303137) Tweedie, F. J., & Baayen, R. H. (1998). How variable may a constant be? Measures of lexical richness in perspective. *Computers and the Humanities, 32*(5), 323–352.
	
[[8]](https://pubs.asha.org/doi/10.1044/jshr.2901.129) Hess, C. W., Sefton, K. M., & Landry, R. G. (1986). Sample size and type-token ratios for oral language of preschool children. *Journal of Speech and Hearing Research, 29*(1), 129–134.
 
[[9]](https://scholar.google.com/scholar_lookup?title=Language%20and%20thought&author=J.B.%20Carroll&publication_year=1964) Carroll, J. B. (1964). *Language and thought.* Englewood Cliffs, NJ: Prentice-Hall.
 
[[10]](https://scholar.google.com/scholar_lookup?title=The%20statistical%20study%20of%20literary%20vocabulary&author=G.U.%20Yule&publication_year=1944) Yule, G. U. (1944). *The statistical study of literary vocabulary.* Cambridge: Cambridge University Press.
 
[[11]](https://pubs.asha.org/doi/10.1044/jshr.3203.536) Hess, C. W., Haug, H., & Landry, R. G. (1989). The reliability of type-token ratios for the oral language of school age children. *Journal of Speech and Hearing Research, 32*(3), 536–540.

[[12]](https://journals.sagepub.com/doi/10.1177/0265532207080767) McCarthy, P. M., & Jarvis, S. (2007). Vocd: A theoretical and empirical evaluation. *Language Testing, 24*(4), 459–488.
	
[[13]](https://www.proquest.com/openview/ef789d09940e4fe1243a5c679a49de76/1/advanced) Maas, H. D. (1972). Über den Zusammenhang zwischen Wortschatzumfang und L ̈ange eines Textes [On the relationship between vocabulary and the length of a text].*Zeitschrift für Literaturwissenschaft und Linguistik, 2*(8), 73.

[[14]](https://link.springer.com/article/10.3758%2FBRM.42.2.381) McCarthy, P. M., & Jarvis, S. (2010). MTLD, vocd-D, and HD-D: A validation study of sophisticated approaches to lexical diversity assessment. *Behavior Research Methods, 42*(2), 381–392.
 
[[15]](https://www.tandfonline.com/doi/abs/10.1080/09296171003643098) Covington, M. A., & McFall, J. D. (2010). Cutting the Gordian knot: The moving-average type–token ratio (MATTR). *Journal of quantitative linguistics, 17*(2), 94-100.
  
[[16]](https://journals.sagepub.com/doi/10.1191/0265532202lt221oa) Malvern, D., & Richards, B. (2002). Investigating accommodation in language proficiency interviews using a new measure of lexical diversity. *Language Testing, 19*(1), 85–104.
	
[[17]](https://www.tandfonline.com/doi/full/10.1080/15434303.2020.1844205) Kyle, K., Crossley, S. A., & Jarvis, S. (2021). Assessing the validity of lexical diversity indices using direct judgements. *Language Assessment Quarterly, 18*(2), 154-170.	
	  
[[18]](https://scholar.google.com/scholar?hl=ko&as_sdt=0%2C38&q=A+new+measure+of+lexical+diversity.+*British+Studies+in+Applied+Linguistics&btnG=) Malvern, D. D., & Richards, B. J. (1997). A new measure of lexical diversity. *British Studies in Applied Linguistics, 12*, 58–71.	

[[19]](https://www.aaai.org/ocs/index.php/FLAIRS/2010/paper/view/1283) McCarthy, P. M. (2005). *An assessment of the range and usefulness of lexical diversity measures and the potential of the measure of textual lexical diversity (MTLD)* (Doctoral dissertation). Memphis, TN: University of Memphis 
	
[[20]](http://www.vli-journal.org/issues/01.1/issue01.1.10.html) Koizumi, R. (2012). Relationships between text length and lexical diversity measures: Can we use short texts of less than 100 tokens? *Vocabulary Learning and Instruction, 1*(1), 60–69.
 
</p>
</details>
  
