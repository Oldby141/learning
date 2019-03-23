import json

f = open("text.text","w")
info = {"age":23,"name":"byf"}
f.write(json.dumps(info))

f.close()