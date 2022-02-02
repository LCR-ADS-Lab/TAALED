#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:35:53 2021

@author: kristopherkyle

Underlying code for TAALED (second generation)
"""
version = ".019" #split off from pre-process_17.py

import math
import pickle
import stat
import operator
import statistics as stat
from collections import Counter
import pkg_resources #for importing data from packages
import itertools #for zip() function


#Try to import plotnine
try:
	from plotnine import ggplot, aes, stat_bin, geom_bar,geom_histogram,geom_vline,geom_density,xlab
	pltn = True
except ModuleNotFoundError:
	print("plotnine has not been installed.\nTo enable advanced data visualization features, please install plotnine.")
	pltn = False

#load datafiles
def get_fname(packagename,filename): #look in package, then in local working directory
	try: 
		data_filename = pkg_resources.resource_filename(packagename, filename)
	except (ModuleNotFoundError, TypeError):
		print("NOTE:",filename,"not found in package, using local file")
		data_filename = filename
	return(data_filename)

#realwordsf = get_fname('taaled',"real_words5.pickle") #words in written COCA that occur at least 5 times
#for testing prior to upload:
realwordsf = get_fname('taaled',"taaled/real_words5.pickle") #words in written COCA that occur at least 5 times
realwords = pickle.load(open(realwordsf,"rb"))

txtsmpl = """There is a saying in my language that goes like: 'If only the young could know and the old could do'. This explains an important lesson, but one has to attain a certain degree of wisdom to understand it. In my opinion being young is more enjoyable, being older may make somebody more experienced but it would not make his life less boring.

While you're young your mind is fresh, open for ideas and future is full of possibilties. Excitement is more preferable than the regret which inevitably comes with the old age and even feeling of fullfillment can't beat the hapiness you feel when you're upon a new discovery. Just remember your greatest triumph. Would you feel the same after ten years passed?

Nobody can deny that having an energetic, heathy body is better than being frail, dependant on medicine or on someone. You can't try parachute jumping if you're past 60. Doctors wouldn't allow it. Even the eating wouldn't be the same with lots of constraints.

It's always easier to meet and get on well with new people as a young person. People accept and trust each other easily. It's simple to find common ground when you're young. Older people tend to be more rigid in their views. Traits and ideas begin to turn to stone. After a certain age it becomes impossible to change them.

Let's face it; people don't get wiser when they get old. They only get old, both in mind and the body. It's becomes harder and harder to deal with them so unfortunatly some families even consider to send them away."""

class params: #for use with pylats.Normalize()
	punctuation = ['``', "''", "'", '.', ',', '?', '!', ')', '(', '%', '/', '-', '_', '-LRB-', '-RRB-', 'SYM', ':', ';', '"']
	punctse = [".","?","!"]
	abbrvs = ["mrs.","ms.","mr.","dr.","phd."]
	splitter = "\n" #for splitting paragraphs
	rwl = realwords
	sp = True
	sspl = "spacy"
	pos = "upos" #other options are "pos" for Penn tags and "upos" for universal tags
	removel = ['becuase'] #typos and other words not caught by the real words list
	lemma = True
	lower = True
	attested = True #filter output using real words list?
	spaces = [" "] #need to add more here
	override = [] #items the system ignores that should be overridden

class default_params: #for resetting params if needed
	punctuation = ['``', "''", "'", '.', ',', '?', '!', ')', '(', '%', '/', '-', '_', '-LRB-', '-RRB-', 'SYM', ':', ';', '"']
	punctse = [".","?","!"]
	abbrvs = ["mrs.","ms.","mr.","dr.","phd."]
	splitter = "\n" #for splitting paragraphs
	rwl = realwords
	sp = True
	sspl = "spacy"
	pos = "upos" #other options are "pos" for Penn tags and "upos" for universal tags
	removel = ['becuase'] #typos and other words not caught by the real words list
	lemma = True
	attested = True #filter output using real words list?
	spaces = [" "] #need to add more here
	override = [] #items the system ignores that should be overridden

#feature rich lexdiv functions
class lexdiv():
	
	def safe_divide(self, numerator, denominator):
		if denominator == 0 or denominator == 0.0:
			index = 0
		else: index = numerator/denominator
		return index
	
	def frequency(self,text):
		freq_d = {}
		for tok in text:
			if tok not in freq_d:
				freq_d[tok] = 1
			else:
				freq_d[tok] += 1
		return(freq_d)
	
	def sorter(self,freq_d):
		sorts =  sorted(freq_d.items(), key=operator.itemgetter(1))
		return(sorts)

	def TTR(self, text):
		ntokens = len(text)
		ntypes = len(set(text))
		
		return(self.safe_divide(ntypes,ntokens))

	def RTTR(self, text):
		ntokens = len(text)
		ntypes = len(set(text))
		
		return(self.safe_divide(ntypes, math.sqrt(ntokens)))

	def MAAS(self, text):
		ntokens = len(text)
		ntypes = len(set(text))
		return(self.safe_divide((math.log10(ntokens)-math.log10(ntypes)), math.pow(math.log10(ntokens),2)))

	def LTTR(self, text):
		ntokens = len(text)
		ntypes = len(set(text))
		
		return(self.safe_divide(math.log10(ntypes), math.log10(ntokens)))

	def MATTR(self, text, window_length = 50, outputs = True):
		vals = []
		windows = []
		if len(text) < (window_length + 1):
			index = self.safe_divide(len(set(text)),len(text))
			return(index,[index],[text])
	
		else:
			for x in range(len(text)):
				small_text = text[x:(x + window_length)]
				if len(small_text) < window_length:
					break
				windows.append(small_text)
				vals.append(self.safe_divide(len(set(small_text)),float(window_length))) 
				index = stat.mean(vals)
			if outputs == True:
				return(index,vals,windows)
			else:
				return(index)

	def MSTTR(self, text, window_length = 50): #add functionality here (lists, etc.)
	
		if len(text) < (window_length + 1):
			ms_ttr = self.safe_divide(len(set(text)),len(text))
	
		else:
			sum_ttr = 0
			denom = 0
	
			n_segments = int(self.safe_divide(len(text),window_length))
			seed = 0
			for x in range(n_segments):
				sub_text = text[seed:seed+window_length]
				#print sub_text
				sum_ttr += self.safe_divide(len(set(sub_text)), len(sub_text))
				denom+=1
				seed+=window_length
	
			ms_ttr = self.safe_divide(sum_ttr, denom)
	
		return(ms_ttr)
	
	def HDD(self,text, samples = 42): #add info to output (probability for each word?)
		#requires Counter import
		def choose(n, k): #calculate binomial
			"""
			A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
			"""
			if 0 <= k <= n:
				ntok = 1
				ktok = 1
				for t in range(1, min(k, n - k) + 1): #this was changed to "range" from "xrange" for py3
					ntok *= n
					ktok *= t
					n -= 1
				return ntok // ktok
			else:
				return 0
	
		def hyper(successes, sample_size, population_size, freq): #calculate hypergeometric distribution
			#probability a word will occur at least once in a sample of a particular size
			try:
				prob_1 = 1.0 - (float((choose(freq, successes) * choose((population_size - freq),(sample_size - successes)))) / float(choose(population_size, sample_size)))
				prob_1 = prob_1 * (1/sample_size)
			except ZeroDivisionError:
				prob_1 = 0
				
			return prob_1
	
		prob_sum = 0.0
		ntokens = len(text)
		types_list = list(set(text))
		frequency_dict = Counter(text)
	
		for items in types_list:
			prob = hyper(0,samples,ntokens,frequency_dict[items]) #random sample is 42 items in length
			prob_sum += prob
	
		return(prob_sum)
	
	def MTLDER(self, text, mn=10,ttrval = .720):
		ft = [] #factor texts
		fl = [] #factor lengths
		fp = [] #factor proportions
		start = 0
		for x in range(len(text)):
			factor_text = text[start:x+1]
			if x+1 == len(text):
				ft.append(factor_text) #add factor text to list
				fact_prop = self.safe_divide((1 - self.TTR(factor_text)),(1 - ttrval)) #proportion of factor
				fp.append(fact_prop)
				fl.append(len(factor_text)) #add partial factor length to list
			else:
				if self.TTR(factor_text) < ttrval and len(factor_text) >= mn:
					ft.append(factor_text) #add factor text to list
					fl.append(len(factor_text))
					fp.append(1)
					start = x+1
				else:
					continue

		return(ft,fl,fp)
	
	#original approach taken by McCarthy and Jarvis (number of words in text divided by number of factors):
	def MTLD_O(self,windowl,factorprop): #window length, factor proportion
		nwords = sum(windowl)
		nfactors = sum(factorprop)
		return(nwords/nfactors)
	
	#mean factor length approach:
	def MTLD_MFL(self,windowl,factorprop, listout = False): #window length, factor proportion
		factorls = [] #holder for factor lengths
		for wl, fp in zip(windowl,factorprop): #iterate through window lengths and factor proportions
			#print(wl/fp)	
			factorls.append(wl/fp) #window length/factor proportion
		if listout == True:
			return(factorls)
		else:
			return(sum(factorls)/len(factorls))

	
	def MTLD(self, text, mn = 10,ttrval = .720, outputs = False): 
		
		fwft,fwfl,fwfp = self.MTLDER(text,mn,ttrval) #factor text list, factor length list, factor proportion list
		bwft,bwfl,bwfp = self.MTLDER(list(reversed(text)),mn,ttrval) #backward text
		
		valo = stat.mean([self.MTLD_O(fwfl,fwfp),self.MTLD_O(bwfl,bwfp)])
		valmfl = stat.mean([self.MTLD_MFL(fwfl,fwfp),self.MTLD_MFL(bwfl,bwfp)]) #average of forward and backward
		valmfl2 = self.MTLD_MFL(fwfl+bwfl,fwfp+bwfp) #mean for all factors (including forward and backward)
		
		if outputs == True:
			return(valmfl2,valmfl,valo,self.MTLD_MFL(fwfl+bwfl,fwfp+bwfp,listout=True),[fwft,fwfl,fwfp,bwft,bwfl,bwfp])
		return(valmfl2)
	
	def __init__(self, text = None, window_length = 50,mn = 10,ttrval = .720,samples = 42):
		if text != None:
			if type(text) != list:
				self.text = text.split(" ")
			else:
				self.text = text
			#basic stats
			self.ntokens = len(self.text) #token count
			self.ntypes = len(list(set(self.text)))
			self.ttr = self.TTR(self.text)
			self.rttr = self.RTTR(self.text)
			self.lttr = self.LTTR(self.text)
			self.maas = self.MAAS(self.text)
			self.msttr = self.MSTTR(self.text,window_length)
			self.hdd = self.HDD(self.text,samples)
			#frequency
			self.freqd = self.frequency(self.text)
			self.freqs = sorted(self.freqd.items(), key=operator.itemgetter(1),reverse = True)
			#mattr stuff
			self.mattr,self.mattrs,self.mattrwins = self.MATTR(self.text,window_length,outputs = True)
			self.nmattrwins = len(self.mattrs) #number of windows for mattr
			if pltn == True:
				self.mattrplot = ggplot() + aes(x=self.mattrs) + geom_density(fill = "#56B4E9",alpha = .2) + geom_vline(xintercept = self.mattr,color = "red",linetype="dashed") + xlab("Density Plot")
			#mtld stuff
			self.mtld,self.mtldav,self.mtldo,self.mtldvals,self.mtldlists = self.MTLD(self.text,mn,ttrval,outputs = True)
			if pltn == True:
				self.mtldplot = ggplot() + aes(x=self.mtldvals) + geom_density(fill = "#56B4E9",alpha = .2) + geom_vline(xintercept = self.mtld,color = "red",linetype="dashed") + xlab("Density Plot")