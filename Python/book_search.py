""" Trystan Kaes
    Search Query Example
    February 2, 2020 """
import requests

headers = {
    'Content-Type': 'application/json'
}

while True:
    searchTerm = input("\nEnter a term to search for (or exit):\n")

    if searchTerm == 'exit':
        break

    res = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + searchTerm)

    if(res.json().get('items')):
        print("\nSearch Results:")
        for books in res.json().get('items'):
            print("  " + books['volumeInfo']['title'])
    else:
        print("\nNo Results\n")
