import nltk
import sys

# lexical_diversity
def lexical_diversity(txt):
	return len(set(txt)) / len(txt)
		
# "main"
nltk.download('punkt')

file1 = './data/2.txt'
file2 = './data/4.txt'
file3 = './data/6.txt'

f1 = open(file1, 'rU')
f2 = open(file2, 'rU')
f3 = open(file3, 'rU')

raw = f1.read()
tokens = nltk.word_tokenize(raw)
txt1 = nltk.Text(tokens)

raw = f2.read()
tokens = nltk.word_tokenize(raw)
txt2 = nltk.Text(tokens)

raw = f3.read()
tokens = nltk.word_tokenize(raw)
txt3 = nltk.Text(tokens)

orig_stdout = sys.stdout
f = open('Korey_MacVittie_Hmwk1.txt', 'w')
sys.stdout = f

print("MACVITTIE - DS 7337 (NLP) - HOMEWORK 1\n")

print("-- Lexical Diversity --")
print(lexical_diversity(txt1))
print(lexical_diversity(txt2))
print(lexical_diversity(txt3))

print("\nThese results seem odd: one would expect a higher-grade \"reader\" to have more diversity in the words used than a lower-grade.")

print("\n-- Vocabulary Size --")
print(len(set(txt1)))
print(len(set(txt2)))
print(len(set(txt3)))

print("\nThese results are not surprising. A higher-grade reader would be expected to have a stronger, larger vocabulary than a younger one.")

q_ans = "\nIt seems fairly sensible that using multiple metrics is going to be more effective than using only one: the main concern, however, seems to be that lexical diversity seems paradoxical, in that as a text grows in length and presumably complexity, the apparent diversity decreases. I would presume that this is probably due to 'functional' words in English: connecting words like 'a' and 'the,' for instance, may appear more often in longer texts, effectively reducing their diversity even in the presence of an increased diversity in vocabulary. For an example, let's run those metrics on this answer:"

print(q_ans)

tokens = nltk.word_tokenize(q_ans)
q_txt = nltk.Text(tokens)

print("")
print(lexical_diversity(q_txt))
print(len(set(q_txt)))