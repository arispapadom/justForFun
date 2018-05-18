
def BinarySearch(element,list_s):

	l=len(list_s)
	
	if(l==1 and list_s[0]!=element):
		return False
	
	if(element>list_s[l//2]):
		f = BinarySearch(element,list_s[l//2:l])
	elif(element<list_s[l//2]):
		f = BinarySearch(element,list_s[0:l//2])
	else:
		return True
	
	return f
	
class list(list):
	def Bsearch(self,element):
		found = BinarySearch(element,self)
		return found		
