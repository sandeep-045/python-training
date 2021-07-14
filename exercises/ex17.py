from sys import argv

sf=open(argv[1],'r')

df=open(argv[2],'w')

content=sf.read()
df.write(content)
sf.close()

df.close()