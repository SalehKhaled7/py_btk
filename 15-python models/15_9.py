import requests

class TheMovieDB():
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMDNiYmI3NzZlNzNkMmM1Yzc2YjNhNTE5MGM0NDRkYyIsInN1YiI6IjY2NDIxM2M0ZWYzZTNmN2JlZTFkZmU5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.K0XMbOpYir29g97shD_3EW-imMninBl_awPatRs1RYI"
        }
        self.token = "" #generate new oAuth "classic" token  with "repo" perms
    
    def search(self,keyword,page):

        response =requests.get(self.api_url+"search/keyword?query="+keyword+"&page="+page , headers=self.headers)

        data = response.json()
        return data

    


    def get_popular(self,page):
        respose = requests.get(self.api_url+"movie/popular?language=en-US&page="+page+"&region=TRU" ,headers=self.headers)
        data = respose.json()
        return data
    

    def get_upcomming(self,page):
        respose = requests.get(self.api_url+"movie/upcoming?language=en-US&page="+page ,headers=self.headers)
        data = respose.json()
        return data
        


    def test_api(self):
        response = requests.get(self.api_url+"configuration", headers=self.headers)
        print(response)
        data = response.json()
        return data
    

print("Welcome to theMovies.org API")

theMovieDB = TheMovieDB()  # Creating an instance of the Github class

def print_movies(result):
    for movie in result['results']:
        print(movie['title'])

while True:
    user_choice = input("1-search a movie \n2-popular movies lis \n3-upcomming movies list \n9-test api \n4-Exit\n")

    if user_choice == "4":
        break
    else:
        if user_choice == "1":

            keyword = input("keyword :")
            page = input("pages :")
            result = theMovieDB.search(keyword,page)
            print(f"page:{result['page']}/{result['total_pages']}")
            print_movies(result)
            for movie in result['results']:
                print(movie['name'])
            


        elif user_choice == "2":
            page = input("pages :")
            result = theMovieDB.get_popular(page)
            print(f"page:{result['page']}/{result['total_pages']}")
            print_movies(result)
            
            current_page = int(page)
            while True:
                choice = input("next page :n , quit:q ")
                if choice == 'n':
                    current_page += 1
                    result = theMovieDB.get_popular(str(current_page))
                    print(f"page:{result['page']}/{result['total_pages']}")
                    print_movies(result)

                elif choice == 'q':
                    break
                else:
                    continue
                

        elif user_choice == "3":
            page = input("pages :")
            result = theMovieDB.get_upcomming(page)
            # print(result)
            print(f"page:{result['page']}/{result['total_pages']}")            
            current_page = int(page)
            print_movies(result)
            while True:
                choice = input("next page :n , quit:q ")
                if choice == 'n':
                    current_page += 1
                    result = theMovieDB.get_upcomming(str(current_page))
                    print(f"page:{result['page']}/{result['total_pages']}")
                    print_movies(result)

                elif choice == 'q':
                    break
                else:
                    continue
                
        elif user_choice == "9":
            result = theMovieDB.test_api()
            print(result)
        else :
            print("wrong input pelase select from the choices")

    