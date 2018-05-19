def partition(self,pivot,end):
	x = self[end]
	i = pivot - 1

	for j in range(pivot,end):
		if(self[j]<=x):
			i = i +1
			temp = self[i]
			self[i] = self[j]
			self[j] = temp
	
	temp = self[i+1]
	self[i+1] = self[end]
	self[end] = temp


	return i + 1




def QuickSort(self,pivot,end):
	if(pivot<end):
		q = partition(self,pivot,end)
		QuickSort(self,pivot,q - 1)
		QuickSort(self,q + 1, end)






class list(list):
	def Qsort(self):
		if(len(self)>1):
			self = QuickSort(self,0,len(self)-1)

