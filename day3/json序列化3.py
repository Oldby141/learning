#import json

import pickle

def sayhi(name):
    print("hello,",name)

info = {
    'name':'alex',
    'age':22,
    'func':sayhi
}


f = open("test.text","wb")
#print(json.dumps(info))
print(pickle.dumps(info) )
f.write( pickle.dumps( info) )#pickle.dump(info,f)

f.close()

f = open("test.text","rb")
data = pickle.loads(f.read())#data = pickle.load(f)
print(data["func"]("Alex"))
f.close()
