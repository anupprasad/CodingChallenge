__author__ = 'Anup'

target=[6,2,1,5]
input=[3,8,5,0]

def calDirection(tar,curr):
	if tar==curr :
		return "- stay"
	elif tar>curr :
		s1=tar-curr
		s2=(10-tar)+curr
		if s1<s2:
			return str(s1)+" down"
		else :
			return str(s2)+" up"
	else :
		s1=curr-tar
		s2=(10-curr)+tar
		if s1<s2 :
			return str(s1)+" up"
		else :
			return str(s2)+" down"




for i in range(len(target)):
	print calDirection(target[i],input[i])