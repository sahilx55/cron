# import requests module
import requests
  
# Making a get request
response = requests.get('https://classroombysahil.nolia.repl.co/')
  
# print response
print(response)
  
# print url
print(response.content)
