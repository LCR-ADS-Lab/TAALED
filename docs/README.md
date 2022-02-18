
# Tool for the Automatic Analysis of Lexical Diversity (TAALED)

**Note that the current documentation is under construction.**
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

### Preprocess a text
Because some indices presume that texts are at least 50 words in length (see, e.g., [McCarthy & Jarvis, 2010](https://link.springer.com/article/10.3758/BRM.42.2.381); [Kyle, Crossley, & Jarvis, 2021](https://doi.org/10.1080/15434303.2020.1844205); [Zenker & Kyle, 2021](https://doi.org/10.1016/j.asw.2020.100505)), we will use a [longer text in this example](https://catalog.ldc.upenn.edu/desc/addenda/LDC2014T06.orig.txt) that conveniently is included in TAALED.

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

### Calculate basic numbers

**Number of Token**
```python
len(clnsmpl.toks)
```
```
276
```

**Number of Type**
```python
len(set(clnsmpl.toks))
```
```
154
```