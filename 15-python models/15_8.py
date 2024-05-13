import requests

class Github():
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "" #generate new oAuth "classic" token  with "repo" perms
    
    def get_user(self,username):
        respose = requests.get(self.api_url+"/users/"+username)
        data = respose.json()
        return f"name:{data['name']}  public repos :{data['public_repos']} followers :{data['followers']}"
    


    def get_repos(self,username):
        respose = requests.get(self.api_url+"/users/"+username+"/repos")
        data = respose.json()
        return data
    

    def create_repo(self,reponame):
        respose = requests.post(
            self.api_url+"/user/repos",
            headers={
                "Authorization": f"token {self.token}"
                },
            json= {
                "name": reponame,
                "description": 'This is your first repo!',
                "homepage": 'https://salehkhaled.com',
                "private": False,
                "is_template": False,
                }
        )
        
        data = respose.json()
        return data
        


        
# ('POST /user/repos', {
#   name: 'Hello-World',
#   description: 'This is your first repo!',
#   homepage: 'https://github.com',
#   'private': false,
#   is_template: true,
#   headers: {
#     'X-GitHub-Api-Version': '2022-11-28'
#   }
# })

# respose = requests.get("https://api.github.com/users/SalehKhaled7/repos")
# result = respose.json()
# for repo in result:
#             print([repo['name'],repo['url']])
print("Welcome to GitHub API")

github = Github()  # Creating an instance of the Github class


while True:
    user_choice = input("1-find a user \n2-Get user repos \n3-Crate new repo \n4-Exit\n")

    if user_choice == "4":
        break
    else:
        if user_choice == "1":

            username = input("username :")
            result = github.get_user(username)
            print(result)

        elif user_choice == "2":
            username = input("username :")
            result = github.get_repos(username)
            for repo in result:
                print(repo['name']) 
                

        elif user_choice == "3":
            repo_name = input("repo name :")
            result = github.create_repo(repo_name)
            print(result)
        else :
            print("wrong input pelase select from the choices")

    