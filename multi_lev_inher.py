class Parent:
	total_prop=1000000
	def parent(cls):
		print("parents total property is :",cls.total_prop)
class Child_1(Parent):
	prop_1=Parent.total_prop+100000
	def child_1(cls):
		print("child_1 property is :",cls.prop_1)
class Child_2(Parent):
	prop_2=Parent.total_prop-200000
	def child_2(cls):
		print("child_2 property is :",cls.prop_2)
p=Parent()
p.parent()
c1=Child_1()
c1.child_1()
c2=Child_2()
c2.child_2()