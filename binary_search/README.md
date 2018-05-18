Binary search algorithm is userd for searching an element in a list. Just hit in the middle and you will get what you want in log2(n) tries (n is the number of list).




You can use this as a python library.

Usage:

  from binary_search import *
  
  a = list(range(1,100))

  x=input("Give number to search:")

  if(a.Bsearch(int(x))):
	  print("Found")
  else:
	  print("Not found")
