# TK_LabInternship

This directory is for Lab Internship with TK Lab. 

# Introduction



# Python Files

## getCNAData.py

to get CNA data from CNA files

### CNAFromCosmic

* input
  * fileName: file name which include desired CNA data
* return: **CNA value** with python *dictionary type*

Unique with gene name which is consist of first and second value of each row. 

### CNAonlyGene

* input
  * fileName: file name which include desired CNA data
* return: python *list type* include **gene names** with CNA 

### CNAwithHugo

* input
  * fileName: file name which include desired CNA data
  * review: default = **True**; this should be *boolean*; if this is True, then the function check the return value, and *remove zeros*
* return: python *dictionary* type include CNA value with **gene name along HUGO type**

### CNAwithPatient

* input
  * fileName: file name which include desired CNA data
  * review: default = **True**; this should be *boolean*; if this is True, then the function check the return value, and *remove zeros*
* return: python *dictionary* type include CNA value with **patient ID** 

### handCNAFromCosmic

* input
  * fileName: file name which include desired CNA data from COSMIC
* return: python *dictionary* type; keys are a pair of **(gene name, CNA value)**, and values are **repetition number** of that

### onlyCNAFromCosmic

* input
  * fileName: file name which include desired CNA data
  * see: default = **None**; the number of column which *want to see* (zero base)
* return: python dictionary type which include gene name and its CNA value

The gene names are unique in return data. Nothing in columns #14 and/or #15, regard as zero.

## getGeneExp.py

### geneExpFromCosmic

* input
  * fileName: file name which include desired gene expression data
  * wanted: default = **None**; this should be *None* or python *list* type; if this is not None, then the function only select gene which is included in wanted
  * cutNormal: default = **False**; this should be *boolean*; if this is true, then the function select gene expression data only over 2 or under -2 ("over" or "under" in column #3)
  * maxlen: default = **None**; this should be *None* or *integer*; if this is not None, the function returns maximum *maxlen* number of data
* return: python *dictionary* type; keys are gene name, and values are python *list* type which contain gene expression data

### geneExpInlier

* input
  * fileName: file name which include desired gene expression data
  * threshold: default = **6**; this should be *integer* or *float*; the function 
* return: 

### geneExpOnlyValue

* input
  * fileName
  * maxlen
* return

### geneExpOutlier

* input
  * fileName
  * threshold
* return