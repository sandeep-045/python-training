states={'AndhraPradesh':'AP',
		'TamilNadu':'TN',
		'UttarPradesh':'UP'}

cities={'AP':'Vizag','TN':'Chennai','UP':'Lucknow'}

x='welcome'
print(x.center(20,'*'))

for state,acro in states.items():
	print(acro,state,sep=':-')


for state in states.keys():
	print(state,cities[states[state]],sep=':-')