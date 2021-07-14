x='some great sentence'
words=x.split(' ')
extra_words=['some','extra','words','to','fix']

print(words)
while len(words)!=5:

	
	words.append(extra_words.pop())
	print(words)