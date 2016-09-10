# encoding=utf8
# cleaned = “ ”.join(re.findall(‘[A-Z][^A-Z]*’, original_tweet)) removing emoticons
import csv,re,time

start_time = time.time()

def is_nonword(word):
    if word.startswith('?'):
        return 1
    if word.startswith('http'): # to remove links
        return 1
    if word.startswith('.'):
        return 1
    #if re.search(r'[0-9]+',word): #qwerty {2,4}
        #return 1
    
with open('dataset.csv', 'rb') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        s=''
        w_list=[ele.lower() for ele in row[1].strip("\"").split()]
        #word_list=[''.join(c for c in word if c.isalpha()) for word in w_list if not is_nonword(word)]
        word_list=[''.join(c for c in word) for word in w_list if not is_nonword(word)]
        #print word_list
        for w in word_list:
            s=s+' '+str(w)
        
        
        cls=open('cls1.txt','a')
        cls.write('%s \n' % str(row[0]))
        cls.close()
        f=open('lower_case1.txt','a')
        f.write('%s \n' % s)
        i+=1
        f.close()
        print i
        #if(i==6):
           # break


print("--- %s seconds ---" % (time.time() - start_time))
        
