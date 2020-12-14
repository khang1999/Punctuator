from punctuator import Punctuator
import sys

p = Punctuator('Demo-Europarl-EN.pcl')

textfile = sys.argv[1]

with open(textfile, 'r') as file:
	data = file.read().replace('\n', ' ')
	data = data.lower()

print(p.punctuate(data))