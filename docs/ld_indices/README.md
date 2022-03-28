---
sort: 1
---

# Calculate LD indices

### Created ldvals object
```python
# We continue the tutorial using the sample text in the package.
ldvals = ld.lexdiv(clnsmpl.toks)
```

### Calculate basic numbers

**Number of Token**
```python
print(ldvals.ntokens)
```
```result
276
```

**Number of Type**
```python
print(ldvals.ntypes)
```
```result
154
```

**Word Frequency**
```python
print(ldvals.freqd)
```
```result
{'there_PRON': 1, 'be_VERB': 1, 'a_DET': 5, 'saying_NOUN': 1, 'in_ADP': 4, 'my_PRON': 2, 'language_NOUN': 1, 'that_PRON': 1, 'go_VERB': 1, 'like_ADP': 1, 'if_SCONJ': 2, 'only_ADV': 2, 'the_DET': 9, 'young_ADJ': 5, 'could_AUX': 2, 'know_VERB': 1, 'and_CCONJ': 8, 'old_ADJ': 6, 'do_VERB': 1, 'this_PRON': 1, 'explain_VERB': 1, 'an_DET': 2, 'important_ADJ': 1, 'lesson_NOUN': 1, 'but_CCONJ': 2, 'one_PRON': 1, 'have_VERB': 2, 'to_PART': 9, 'attain_VERB': 1, 'certain_ADJ': 2, 'degree_NOUN': 1, 'of_ADP': 4, 'wisdom_NOUN': 1, 'understand_VERB': 1, 'it_PRON': 8, 'opinion_NOUN': 1, 'be_AUX': 17, 'more_ADV': 4, 'enjoyable_ADJ': 1, 'may_AUX': 1, 'make_VERB': 2, 'somebody_PRON': 1, 'experienced_ADJ': 1, 'would_AUX': 4, 'not_PART': 6, 'his_PRON': 1, 'life_NOUN': 1, 'less_ADV': 1, 'boring_ADJ': 1, 'while_SCONJ': 1, 'you_PRON': 7, 'your_PRON': 2, 'mind_NOUN': 2, 'fresh_ADJ': 1, 'open_ADJ': 1, 'for_ADP': 1, 'idea_NOUN': 2, 'future_NOUN': 1, 'full_ADJ': 1, 'excitement_NOUN': 1, 'preferable_ADJ': 1, 'than_ADP': 2, 'regret_NOUN': 1, 'which_PRON': 1, 'inevitably_ADV': 1, 'come_VERB': 1, 'with_ADP': 4, 'age_NOUN': 2, 'even_ADV': 3, 'feeling_NOUN': 1, 'can_AUX': 3, 'beat_VERB': 1, 'feel_VERB': 2, 'when_SCONJ': 3, 'upon_SCONJ': 1, 'new_ADJ': 2, 'discovery_NOUN': 1, 'just_ADV': 1, 'remember_VERB': 1, 'great_ADJ': 1, 'triumph_NOUN': 1, 'same_ADJ': 2, 'after_ADP': 2, 'ten_NUM': 1, 'year_NOUN': 1, 'pass_VERB': 1, 'nobody_PRON': 1, 'deny_VERB': 1, 'that_SCONJ': 1, 'energetic_ADJ': 1, 'body_NOUN': 2, 'well_ADJ': 1, 'frail_ADJ': 1, 'dependant_ADJ': 1, 'on_ADP': 3, 'medicine_NOUN': 1, 'or_CCONJ': 1, 'someone_PRON': 1, 'try_VERB': 1, 'parachute_VERB': 1, 'jump_VERB': 1, 'past_ADJ': 1, '60_NUM': 1, 'doctor_NOUN': 1, 'allow_VERB': 1, 'eating_NOUN': 1, 'lot_NOUN': 1, 'constraint_NOUN': 1, 'always_ADV': 1, 'easy_ADJ': 1, 'meet_VERB': 1, 'get_VERB': 4, 'well_ADV': 1, 'people_NOUN': 4, 'as_ADP': 1, 'person_NOUN': 1, 'accept_VERB': 1, 'trust_VERB': 1, 'each_DET': 1, 'other_ADJ': 1, 'easily_ADV': 1, 'simple_ADJ': 1, 'find_VERB': 1, 'common_ADJ': 1, 'ground_NOUN': 1, 'tend_VERB': 1, 'rigid_ADJ': 1, 'their_PRON': 1, 'view_NOUN': 1, 'trait_NOUN': 1, 'begin_VERB': 1, 'turn_VERB': 1, 'to_ADP': 1, 'stone_NOUN': 1, 'become_VERB': 2, 'impossible_ADJ': 1, 'change_VERB': 1, 'they_PRON': 5, 'let_VERB': 1, 'us_PRON': 1, 'face_VERB': 1, 'do_AUX': 1, 'wise_ADJ': 1, 'both_PRON': 1, 'hard_ADJ': 2, 'deal_VERB': 1, 'so_ADV': 1, 'some_DET': 1, 'family_NOUN': 1, 'consider_VERB': 1, 'send_VERB': 1, 'away_ADV': 1}
```

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

### Let's start calculate LD indices!

{% include list.liquid %}
