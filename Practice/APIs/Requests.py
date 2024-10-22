# pip install requests
import requests

r = requests.get('https://xkcd.com/353/')
print(r)

#print(help(r))
#print(dir(r))  #Recieve attributes

print(r.text)

r = requests.get('https://imgs.xkcd.com/comics/python.png') #Download using write bytes
with open('comic.png', 'wb') as f: 
    f.write(r.content)

print(r.status_code)
#200s are success, 300s are redirects, 400s are client errors,
#And 500s are server errors

print(r.ok) #Easy way for checking errors. If it returns false,
#There is an error either with the client or server.

print(r.headers)
