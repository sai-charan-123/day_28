class Father:
	prop_1=160000
	def father(cls):
		print("Father property is :",cls.prop_1)
class Mother:
	prop_2=200000
	def mother(cls):
		print("mother property is :",cls.prop_2)
class Child(Father,Mother):
	prop_3=Father.prop_1+Mother.prop_2+100000
	def child(cls):
		print("child property is :",cls.prop_3)
f=Father()
f.father()
m=Mother()
m.mother()
c=Child()
c.child()