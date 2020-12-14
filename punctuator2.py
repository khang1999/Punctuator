from punctuator import Punctuator
import sys

punctuatorSelected = input('Which punctuator would you like to test: \n1. Demo-Europarl-En.pcl \n2. INTERSPEECH-T-BRNN.pcl\n\n')

if(punctuatorSelected == '1'):
	p = Punctuator('Demo-Europarl-EN.pcl')
	pText = 'Demo-Europarl-EN'	
if(punctuatorSelected == '2'):
	p = Punctuator('INTERSPEECH-T-BRNN.pcl')
	pText = 'INTERSPEECH-T-BRNN'

print('\nYou have selected ', pText, '\n')

textfile = sys.argv[1]
output_file = open('output.txt', 'w')

with open(textfile, 'r') as file:
	data = file.read().replace('\n', ' ')
	data = data.lower()

fillerwords = ['uh']
datawords = data.split()

processData = [word for word in datawords if word.lower() not in fillerwords]
finalText = ' '.join(processData)


print(p.punctuate(finalText))

output_file.write(p.punctuate(finalText))