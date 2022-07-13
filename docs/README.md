
# Tool for the Automatic Analysis of Lexical Diversity (TAALED)

TAALED is a Python package for calculating lexical diversity (LD) indices. The package is designed for the researchers, students, and teachers in (applied) linguistics needing to calculate LD indices that are stable across different text lengths (i.e., revised LD indices) as well as classic LD indices. The package was developed by [Kristopher Kyle](https://kristopherkyle.github.io/professional-webpage/). Many thanks to [Scott Jarvis](https://faculty.utah.edu/u6013287-Scott_Jarvis/research/index.hml), who provided valuable insights about the calculation of MTLD and HD-D. This documentation page is contributed by [Hakyung Sung](https://hksung.github.io) and [Masaki Eguchi](https://masakieguchi.weebly.com) in the [LCR-ADS lab](https://lcr-ads-lab.github.io/LCR-ADS-Home/) at the University of Oregon.

# Quick Start Guides

## How to Install TAALED
To install TAALED, you can use `pip (a package installer for Python)`:

```bash
pip install taaled
```

## How to Install Related Packages
While not strictly necessary, this tutorial will presume that you have also installed a few helpful  packages for text preprocessing and visualization. These are optional but recommended.

TAALED takes a list of strings as input and returns various indices of LD (and diagnostic information). In the rest of the tutorial, we will use [pylats](https://github.com/LCR-ADS-Lab/pylats) for preprocessing of texts (e.g., tokenization, lemmatization, word disambiguation, checking for misspelled words, etc.). Currently pylats only supports advanced features for English (models for other languages are forthcoming). Pylats was tested using spacy version 3.2 and by default uses the "en_core_web_sm" model. To install spacy and a language model, see the [spacy installation instructions](https://spacy.io/usage).

However, TAALED can work with any language, as long as texts are tokenized (and appropriately preprocessed). See tools such as [spacy](https://spacy.io/), [stanza](https://stanfordnlp.github.io/stanza/), and [trankit](https://github.com/nlp-uoregon/trankit) for NLP pipelines for a wide range of languages.

```bash
pip install pylats
```

TAALED also makes use of [plotnine](https://plotnine.readthedocs.io/en/stable/installation.html) for data visualization. This package is not required for taaled to function properly, but is needed if data visualization (e.g., density plots for mtld factor lengths) are desired.

```bash
pip install plotnine
```

## How to Import 
We will import the installed packages in Python.

```python
from taaled import ld
from pylats import lats #optional, but recommended for text preprocessing
```

## How to Preprocess a text
Because some indices presume that texts are at least 50 words in length (see, e.g., McCarthy & Jarvis, 2010<sup>[19](https://lcr-ads-lab.github.io/TAALED/references/1.%20Related%20Studies.html#mccarthy-p-m--jarvis-s-2010)</sup>; Kyle, Crossley, & Jarvis, 2021<sup>[12](https://lcr-ads-lab.github.io/TAALED/references/1.%20Related%20Studies.html#kyle-k-crossley-s-a--jarvis-s-2021)</sup>; Zenker & Kyle, 2021<sup>[22](https://lcr-ads-lab.github.io/TAALED/references/1.%20Related%20Studies.html#zenker-f--kyle-k-2021)</sup>, we will use a [longer text in this example](https://catalog.ldc.upenn.edu/desc/addenda/LDC2014T06.orig.txt) that is conveniently included in TAALED.

Minimally, a text string must be turned into a flat list of strings to work with TAALED.

Ideally, a number of text preprocessing/normalization steps will be used. In the example below, the [pylats](https://github.com/LCR-ADS-Lab/pylats) package is used to tokenize the text, remove most punctuation, add part of speech tags (for homograph disambiguation), lemmatize each word, check for (and ignore) misspelled words (misspelled words will innapropriately inflate ld values), and convert all words to lower case. [pylats](https://github.com/LCR-ADS-Lab/pylats) is quite flexible/customizable, and the taaled package includes a default parameters object `ld.params` for use with pylats.

```python
#if pylats is installed, preprocess the sample text using the default taaled parameters file
clnsmpl = lats.Normalize(ld.txtsmpl, ld.params)
print(clnsmpl.toks[:10]) #check sample output
```

```result
['there_PRON', 'be_VERB', 'a_DET', 'saying_NOUN', 'in_ADP', 'my_PRON', 'language_NOUN', 'that_PRON', 'go_VERB', 'like_ADP']
```

**To continue reading the quick-start guide, follow [this link and learn about how to calculate LD indices](https://lcr-ads-lab.github.io/TAALED/ld_indices/#create-a-ldvals-object).**

## How to Cite
Kyle, K., Crossley, S. A., & Jarvis, S. (2021). Assessing the validity of lexical diversity indices using direct judgements. *Language Assessment Quarterly, 18*(2), 154-170.<sup>[12](https://lcr-ads-lab.github.io/TAALED/references/1.%20Related%20Studies.html#kyle-k-crossley-s-a--jarvis-s-2021)</sup>
 
