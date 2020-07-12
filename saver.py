import requests
import fuck
def saver():
	information = fuck.fuck()
	classifie = information.split('::$')
	print('classifie', classifie)
	if classifie[0] != '':
		p = requests.get(classifie[0].strip())
		out = open("1.jpg", "wb")
		out.write(p.content)
		out.close()
	return classifie
saver()