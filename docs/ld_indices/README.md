---
sort: 1
---

# Quick Start Guides

### How to Install TAALED
To install TAALED, you can use `pip (a package installer for Python)`:

```bash
pip install taaled
```

### How to Install Related Packages
While not strictly necessary, this tutorial will presume that you have also installed following pacakges for text preprocessing and visualization. These are optional but recommended.

TAALED takes a list of strings as input and returns various indices of LD (and diagnostic information). In the rest of the tutorial, we will use [pylats](https://github.com/LCR-ADS-Lab/pylats) for preprocessing of texts (e.g., tokenization, lemmatization, word disambiguation, checking for misspelled words). Currently pylats only supports advanced features for English (models for other languages are forthcoming). Pylats was tested using spacy version 3.2 and be default uses the "en_core_web_sm" model. To install spacy and a language model, see the [spacy installation instructions](https://spacy.io/usage).

However, TAALED can work with any language, as long as texts are tokenized (and appropriately preprocessed). See tools such as [spacy](https://spacy.io/), [stanza](https://stanfordnlp.github.io/stanza/), and [trankit](https://github.com/nlp-uoregon/trankit) for NLP pipelines for a wide range of languages.

```bash
pip install pylats
```

TAALED also makes use of [plotnine](https://plotnine.readthedocs.io/en/stable/installation.html) for data visualization. This package is not required for taaled to function properly, but is needed if data visualization (e.g., density plots for mtld factor lengths) are desired.

```bash
pip install plotnine
```

### How to Import 
We will import the installed packages in Python.

```python
from taaled import ld
from pylats import lats #optional, but recommended for text preprocessing
```

### How to Preprocess a text
Because some indices presume that texts are at least 50 words in length (see, e.g., McCarthy & Jarvis, 2010<sup>[18](https://lcr-ads-lab.github.io/TAALED/references/1.%20Related%20Studies.html#mccarthy-p-m--jarvis-s-2010)</sup>; Kyle, Crossley, & Jarvis, 2021<sup>[12](https://lcr-ads-lab.github.io/TAALED/references/1.%20Related%20Studies.html#kyle-k-crossley-s-a--jarvis-s-2021)</sup>; Zenker & Kyle, 2021<sup>[22](https://lcr-ads-lab.github.io/TAALED/references/1.%20Related%20Studies.html#zenker-f--kyle-k-2021)</sup>, we will use a [longer text in this example](https://catalog.ldc.upenn.edu/desc/addenda/LDC2014T06.orig.txt) that conveniently is included in TAALED.

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

### Create a ldvals object

To calculate LD indices for a single text, all you need is to run the following command over a tokenized list. 

```python
ldvals = ld.lexdiv(clnsmpl.toks)
```
The `ldvals` object contains the result of the LD analysis, which can be accessed through respective methods. These are explained below.

### Calculate basic numbers
Once you created an `ldvals` object, you will be able to see the result of the analysis by calling a method.

Here, we present how to inspect basic textual information such as the number of tokens, types, and document frequency for each word (i.e., how many times a particular word occurs in the input text).

For how to output modern LD indices (e.g., MTLD, MATTR), see [Calculate Revised LD indices](https://lcr-ads-lab.github.io/TAALED/ld_indices/1.%20Revised_LD_indices.html).
For classic LD indices (not recommended except for comparison), see [Calculate Classic (but Flawed) LD Indices](https://lcr-ads-lab.github.io/TAALED/ld_indices/2.%20Classic_LD_indices.html).


**Number of Tokens**

The `.ntokens` method will return the number of tokens in the input text.

```python
print(ldvals.ntokens)
```
```result
276
```

**Number of Types**

The `.ntypes` method will return the number of types (i.e., unique words) in the input text.

```python
print(ldvals.ntypes)
```
```result
154
```

**Word Frequency**

The `.freqd` method will return the document frequencies (i.e., how many times each word occurs in the text) of each word in the input text.

```python
print(ldvals.freqd)
```
```result
{'there_PRON': 1, 'be_VERB': 1, 'a_DET': 5, 'saying_NOUN': 1, 'in_ADP': 4, 'my_PRON': 2, 'language_NOUN': 1, 'that_PRON': 1, 'go_VERB': 1, 'like_ADP': 1, 'if_SCONJ': 2, 'only_ADV': 2, 'the_DET': 9, 'young_ADJ': 5, 'could_AUX': 2, 'know_VERB': 1, 'and_CCONJ': 8, 'old_ADJ': 6, 'do_VERB': 1, 'this_PRON': 1, 'explain_VERB': 1, 'an_DET': 2, 'important_ADJ': 1, 'lesson_NOUN': 1, 'but_CCONJ': 2, 'one_PRON': 1, 'have_VERB': 2, 'to_PART': 9, 'attain_VERB': 1, 'certain_ADJ': 2, 'degree_NOUN': 1, 'of_ADP': 4, 'wisdom_NOUN': 1, 'understand_VERB': 1, 'it_PRON': 8, 'opinion_NOUN': 1, 'be_AUX': 17, 'more_ADV': 4, 'enjoyable_ADJ': 1, 'may_AUX': 1, 'make_VERB': 2, 'somebody_PRON': 1, 'experienced_ADJ': 1, 'would_AUX': 4, 'not_PART': 6, 'his_PRON': 1, 'life_NOUN': 1, 'less_ADV': 1, 'boring_ADJ': 1, 'while_SCONJ': 1, 'you_PRON': 7, 'your_PRON': 2, 'mind_NOUN': 2, 'fresh_ADJ': 1, 'open_ADJ': 1, 'for_ADP': 1, 'idea_NOUN': 2, 'future_NOUN': 1, 'full_ADJ': 1, 'excitement_NOUN': 1, 'preferable_ADJ': 1, 'than_ADP': 2, 'regret_NOUN': 1, 'which_PRON': 1, 'inevitably_ADV': 1, 'come_VERB': 1, 'with_ADP': 4, 'age_NOUN': 2, 'even_ADV': 3, 'feeling_NOUN': 1, 'can_AUX': 3, 'beat_VERB': 1, 'feel_VERB': 2, 'when_SCONJ': 3, 'upon_SCONJ': 1, 'new_ADJ': 2, 'discovery_NOUN': 1, 'just_ADV': 1, 'remember_VERB': 1, 'great_ADJ': 1, 'triumph_NOUN': 1, 'same_ADJ': 2, 'after_ADP': 2, 'ten_NUM': 1, 'year_NOUN': 1, 'pass_VERB': 1, 'nobody_PRON': 1, 'deny_VERB': 1, 'that_SCONJ': 1, 'energetic_ADJ': 1, 'body_NOUN': 2, 'well_ADJ': 1, 'frail_ADJ': 1, 'dependant_ADJ': 1, 'on_ADP': 3, 'medicine_NOUN': 1, 'or_CCONJ': 1, 'someone_PRON': 1, 'try_VERB': 1, 'parachute_VERB': 1, 'jump_VERB': 1, 'past_ADJ': 1, '60_NUM': 1, 'doctor_NOUN': 1, 'allow_VERB': 1, 'eating_NOUN': 1, 'lot_NOUN': 1, 'constraint_NOUN': 1, 'always_ADV': 1, 'easy_ADJ': 1, 'meet_VERB': 1, 'get_VERB': 4, 'well_ADV': 1, 'people_NOUN': 4, 'as_ADP': 1, 'person_NOUN': 1, 'accept_VERB': 1, 'trust_VERB': 1, 'each_DET': 1, 'other_ADJ': 1, 'easily_ADV': 1, 'simple_ADJ': 1, 'find_VERB': 1, 'common_ADJ': 1, 'ground_NOUN': 1, 'tend_VERB': 1, 'rigid_ADJ': 1, 'their_PRON': 1, 'view_NOUN': 1, 'trait_NOUN': 1, 'begin_VERB': 1, 'turn_VERB': 1, 'to_ADP': 1, 'stone_NOUN': 1, 'become_VERB': 2, 'impossible_ADJ': 1, 'change_VERB': 1, 'they_PRON': 5, 'let_VERB': 1, 'us_PRON': 1, 'face_VERB': 1, 'do_AUX': 1, 'wise_ADJ': 1, 'both_PRON': 1, 'hard_ADJ': 2, 'deal_VERB': 1, 'so_ADV': 1, 'some_DET': 1, 'family_NOUN': 1, 'consider_VERB': 1, 'send_VERB': 1, 'away_ADV': 1}
```
We can also sort the output using the `.freqs` method. In the following, we output 10 most frequent items in the input text.
```python
print(ldvals.freqs[:10]) #sorted ten most frequent items
```
```result
[('be_AUX', 17), ('the_DET', 9), ('to_PART', 9), ('and_CCONJ', 8), ('it_PRON', 8), ('you_PRON', 7), ('old_ADJ', 6), ('not_PART', 6), ('a_DET', 5), ('young_ADJ', 5)]
```

#### You can apply the codes your own sample essay.
* The sample essay below is randomly chosen from the [The Gachon Learner Corpus](https://app.box.com/s/vw4803lct2dq4xbrquae).

```python
sample ='''
On the road almost crash makes me very frightening. 
We have every Saturday and Sunday off. I decided to go shopping on Saturday. 
I bought some daily necessities. And I have eat lunch in a restaurant. 
So I have been going home. When I passed the crossroad the green light was not bright. 
After a while the green light I ready to cross the road. When I walk in the middle of the road suddenly a car rushed. 
I was still. I want to finish it to hit me. On me from the place near the car stopped. The tyres was made brake loud. 
The driver rushed off to apologize to me. This thing that made me think I fear.
'''

clnsmpl2 = lats.Normalize(sample, ld.params)
ldvals2 = ld.lexdiv(clnsmpl2.toks)
```

```python
print(ldvals2.ntokens)
```
```result
120
```

```python
print(ldvals2.ntypes)
```
```result
70
```
```python
print(ldvals2.freqs[:5])
```
```result
[('i_PRON', 15), ('the_DET', 11), ('to_PART', 5), ('be_AUX', 4), ('on_ADP', 3)]
```

### Let's start calculating LD indices!
This quick-start guide walked you through how to create `ldvals` object and output basic information.
In the following pages, we outline how to output lexical diversity indices and how to batch process input text files and save the output in csv.
