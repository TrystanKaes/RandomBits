""" Trystan Kaes
    requests library example
    January 29th, 2020 """

import requests



headers = {
  "Content-Type": "application/x-www-form-urlencoded"
  }
body = {
  "username": "testuser",
  "password": "cu"
  }

res = requests.post('https://kaest-csc3916-hw2.herokuapp.com/signup',data=body, headers=headers)

print("Signed up with response: \n  \"" + res.text + "\"\n")


res = requests.post('https://kaest-csc3916-hw2.herokuapp.com/signin',data=body, headers=headers)

token = res.json().get('token')

print("Signed in with token: \n  \"" + token + "\"\n")

headers = {'Content-Type': 'application/json',
           'Authorization':token}
body = {}
res = requests.put('https://kaest-csc3916-hw2.herokuapp.com/movies', headers=headers)

print("PUT response: \n  \"" + res.json().get('msg') + "\"")


# requests
