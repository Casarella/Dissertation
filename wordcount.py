#filename='~/Documents/Dissertation_Casarella/Dissertation_Casarella.tex'
words1=0
words2=0
words3=0
words4=0
words5=0
template_words=0
textfile1=open('Chapter1_Casarella.tex','r')
textfile2=open('Chapter2_Casarella.tex','r')
textfile3=open('Chapter3_Casarella.tex','r')
textfile4=open('Chapter4_Casarella.tex','r')
textfile5=open('Chapter5_Casarella.tex','r')

for wordcount in textfile1.read().split():
  words1+=1
for wordcount in textfile2.read().split():
  words2+=1
for wordcount in textfile3.read().split():
  words3+=1
for wordcount in textfile4.read().split():
  words4+=1
for wordcount in textfile5.read().split():
  words5+=1
textfile_template=0
#open('template.tex','r')

#for wordcount in textfile_template.read().split():
#  template_words+=1

net_word_count=words1+words2+words3+words4+words5-template_words

print('Your dissertation is', net_word_count, 'words long.')