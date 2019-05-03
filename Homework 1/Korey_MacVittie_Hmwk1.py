import nltk

# lexical_diversity
def lexical_diversity(txt):
	return len(set(text)) / len(text)
	
# percentage
def percentage(cnt, ttl):
	return 100 * count / total

# loadData
def loadData(f1, f2, f3):
	a = []
	b = []
	c = []
	
	for line in open(f1):
		lin = line.rstrip('\n').split()
		
		for x in lin:
			a.append(x)
	
	for line in open(f2):
		lin = line.rstrip('\n').split()
		
		for x in lin:
			b.append(x)
			
	for line in open(f3):
		lin = line.rstrip('\n').split()
		
		for x in lin:
			c.append(x)
	
	return a, b, c
		
# "main"
file1 = './data/2.txt'
file2 = './data/4.txt'
file3 = './data/6.txt'

txt1, txt2, txt3 = loadData(file1, file2, file3)

print(txt1)
print(txt2)
print(txt3)