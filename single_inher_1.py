class Parent:
	prop=100000
	def child(cls):
		print("your parents property is :",cls.prop)
class Child(Parent):
	prop2=Parent.prop+200000
	def child(cls):
		print("your property is :",cls.prop2)
c=Parent()
c.child()
d=Child()
d.child()