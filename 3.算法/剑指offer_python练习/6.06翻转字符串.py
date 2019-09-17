



class Solution:
	def ReverseSentence(self, s):
		# write code here
		if s==None or len(s)<=0:
			return ''
		s=list(s)	#字符串转为数组
		s=self.Reverse(s)
		pStart=0 	#左指针
		pEnd=0  	#右指针
		listTemp=[]	
		result=''
		#print(s)
		while pEnd<len(s):
			if pEnd==len(s)-1:
				#print(self.Reverse(s[pStart:]))
				listTemp.append(self.Reverse(s[pStart:]))
				break
			if s[pStart]==' ':	#左，右一起指着空格
				pStart +=1
				pEnd +=1		#左右同时指向下一个单词的第一个字母
				listTemp.append(' ')	#意思是上一个单词结束
			
			elif s[pEnd]==' ':#直到右指到空格
				#print(self.Reverse(s[pStart:pEnd]))
				listTemp.append(self.Reverse(s[pStart:pEnd]))	#左:右-1  为一个单词，自翻转然后放入listTemp
				pStart=pEnd		#左移动到右，同时指向空格
			else:#首先是第一步
				pEnd +=1
		print(listTemp)
		for i in listTemp:
			result+=''.join(i)	#最后将数组取出来弄成字符串
		return result

	def Reverse(self,s):	#设置左右指针，互换数据，来做全部翻转
		# s是一个list列表
		start=0
		end=len(s)-1
		while(start<end):
			s[start],s[end]=s[end],s[start]
			start+=1
			end-=1
		return s















