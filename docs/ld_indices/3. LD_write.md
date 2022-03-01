
# LD write?

LD write function allows you to save your analysis into a csv file.

```python
from taaled import ld
from pylats import lats
from datetime import datetime
from datetime import date
import glob
```

```python
def outname_creator(fldname,isprll,other = None):
	day = date.today().strftime("%Y%m%d") #get date
	time = datetime.now().strftime("%H%M%S")
	ldv = "taaledv" + ld.version
	latsv = "pylatsv" + lats.version
	if isprll == True:
		pa = "pa"
	else:
		pa = "nopa"

	if other == None:
		outn = "_".join([day,time,fldname,pa]) + ".txt"
	else:
		outn = "_".join([day,time,fldname,pa,other]) + ".txt"

	return(outn)
```

```python
#get list of corpus files
corp_path = "/Users/hakyungsung/Desktop/" #path to corpora
sample = glob.glob(corp_path + "sample*.txt") #get list of filenames from the stage234/ folder
len(sample) #check list
```

```python
outname = outname_creator("sample",False)
```

```python
#run data
ld.ldwrite(sample,outname) #calculate ld for entire corpus: filename should be "date_time_sample_nopa(no parallel analysis).txt" ("20220301_065208_stage234_nopa.txt")
ld.ldwrite(sample,outname_creator("sample",True),mx = 200, prll = True) #run parallel analysis for entire corpus-filename should be "date_time_sample_pa(parallel analysis).txt"
```
