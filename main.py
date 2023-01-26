import requests

test = "https://www.terra.com.br/"
r = requests.get(test)

arq = open("lista.txt")
lista = arq.readlines()

for i in lista:
 if (r.status_code >= 200 and r.status_code <= 299):
  print("ON :)")
 else: 
  print("OFF :(")

for i in lista:
 if (r.status_code >= 400 and r.status_code <= 499):
  print("Bad Request")
 else: 
  print("ok")

for i in lista:
 if (r.status_code >= 500 and r.status_code <= 599):
  print("internal server error")
 else: 
  print("server ok ... \(^^)/")