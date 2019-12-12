import collections
 
 
# class Mydict(collections.UserDict):


	# def __missing__(self, key):
		# if isinstance(key, str):
			# raise KeyError(key)
		# return self[str(key)]

	# def __contains__(self, key):
		# return str(key) in self.data

	# def __setitem__(self, key, item):
		# self.data[str(key)] = item

	# def __getattr__(self, key):
		# return self.data[str(key)]
 
 
# if __name__ == '__main__':
	# mydict = Mydict((('a',1),('c',('d',3)),('b',2)))

	# print(mydict)
	# print(mydict.a)
	# print(mydict['a'])


class Foo:
	def __getitem__(self, item):
		print('=====>get')
		return self.__dict__[item]

	def __setitem__(self, key, value):
		self.__dict__[key] = value
		# setattr(self,key,value)

	def __delitem__(self, key):
		# self.__dict__.pop(key)
		print(key,type(key))#
		
		
		
f = Foo()
f['x']=1
f['y']=3
print(f.__dict__)
print(dir(f))

del f['x']


















