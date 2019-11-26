import json

data = '''
{
  "name" : "Mark",
  "phone" : {
    "type" : "intl",
    "number" : "+63 920 981 0209"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
