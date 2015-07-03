import markov
import markov2
import os


fn = "I:\python_projects\markov\corpus.txt"
open_file = open(fn,'r')


mv = markov.Markov(open_file)
res = mv.generate_markov_text(300)
print(res)
mv.save(os.path.join(os.path.split(fn)[0], 'output.txt'),'a')


'''
mark2 = markov2.Markov(open_file)
res = mark2.generate_markov_text(50)
print(res)
print mark2.words
'''