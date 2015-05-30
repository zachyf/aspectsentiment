import json

m = {}
num_lines = sum(1 for line in open('glove.twitter.27B.50d.txt'))
print num_lines
f = open('glove.twitter.27B.50d.txt')
i = 0
for line in f:
    if i % 1000000 == 0:
        print "progress: ", i
    s = line.strip().split()
    try: 
        word = s[0]
        vector = [float(num) for num in s[1:]]
        m[word] = vector
    except:
        print s
    i += 1

with open('wordvectors.twitter.50d.json','w') as outfile:
    json.dump(m, outfile)
        
