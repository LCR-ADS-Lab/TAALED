---
sort: 1
---

# Calculate LD indices

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

**Created ldvals object**
```python
#create ld object
ldvals = ld.lexdiv(clnsmpl.toks)
```

### Let's start calculate LD indices!

{% include list.liquid %}
