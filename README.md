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
  * fileName
  * review: default = **True**; if this is True, then the function check the return value, and *remove zeros*
* return: python *dictionary* type include CNA value with **gene name along HUGO type**

### CNAwithPatient

* input
  * fileName
  * review: default = **True**; if this is True, then the function check the return value, and *remove zeros*
* return: python *dictionary* type include CNA value with **patient ID** 

### handCNAFromCosmic

### onlyCNAFromCosmic

* input
  * fileName: file name which include desired CNA data
  * see: default = **None**; the number of column which *want to see* (zero base)
* return: 



### 