# themoviedb.org => film ve dizi arsivi
# themoviedb'nin sundugu API'yi uygulamada kullan.
# Anahtar kelimeye gore arama
# En populer film listesi
# Vizyondaki film listesi

import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://www.themoviedb.org/3"
        self.api_key = "YOUR API KEY"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json
    
    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key= {self.api_key}&query={keyword}&page=1")
        return response.json

movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Search Movies\n3- Exit\nSecim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies:
                print(movie['title']) #sadece populer filmlerin titlenı yazdirir.

        if secim == "2":
            keyword = input('keyword: ')
            movies = movieApi.getSearchResults()
            for movie in movies['results']:
                print(movie)
