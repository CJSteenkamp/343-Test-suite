import requests, json

class TextColor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

API_URL = 'https://api.github.com'
TEST_URL = 'http://127.0.0.1:5000'

GITHUB_TOKEN = ''  # Replace this with your GitHub token

def APIcurl(url):
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    return json.loads(response.text) 

def APIuser(username):
    url = API_URL+"/users/"+username
    # apireq = requests.get(url)
    # apijson = json.loads(apireq.text)
    apijson = APIcurl(url)

    # print(json.dumps(apijson, indent=2))

    apiuser = {
        'login': apijson['login'],
        'id' : apijson['id'],
        'avatar_url': apijson['avatar_url'],
        'url': apijson['url'],
        'html_url': apijson['html_url'],
        'type': apijson['type'],
        'name': apijson['name'],
        'company': apijson['company'],
        'blog': apijson['blog'],
        'location': apijson['location'],
        'bio': apijson['bio'],
        'twitter_username': apijson['twitter_username'],
        'public_repos': apijson['public_repos'],
        'followers': apijson['followers'],
        'following': apijson['following']
    }

    return apiuser

def TESTuser(username):
    url = TEST_URL+"/users/"+username
    testreq = requests.get(url)
    testjson = json.loads(testreq.text)

    # print(json.dumps(testjson, indent=2))

    apiuser = {
        'login': testjson['login'],
        'id' : testjson['id'],
        'avatar_url': testjson['avatar_url'],
        'url': testjson['url'],
        'html_url': testjson['html_url'],
        'type': testjson['type'],
        'name': testjson['name'],
        'company': testjson['company'],
        'blog': testjson['blog'],
        'location': testjson['location'],
        'bio': testjson['bio'],
        'twitter_username': testjson['twitter_username'],
        'public_repos': testjson['public_repos'],
        'followers': testjson['followers'],
        'following': testjson['following']
    }

    return apiuser

def test_user(username):
    for user in username:
        api = APIuser(user)
        test = TESTuser(user)
        message = ""        
        fail = False

        for key in api.keys():
            if key not in test:
                # Dont have the field
                fail = True
                message = TextColor.RED + f"{key}"+ TextColor.RESET + "field not found!"  + '\n'
                continue

            if (api[key] == test[key] or api[key] == None and test[key] == "" or api[key] == "" and test[key] == None):
                # got the right field
                message += f"{key:<20} " + TextColor.GREEN + "Correct!" + TextColor.RESET + '\n'
            else:
                fail = True
                message += f"{key:<20} " + TextColor.RED + "Incorrect! 😞"+ TextColor.RESET + f"\n\tAPI  : \"{api[key]}\"\n\tTest : \"{test[key]}\"\n"
        
        if fail:
            message = TextColor.RED + f"GET users/{user} FAILED 😞" + TextColor.RESET + '\n' + message
        else:
            message = TextColor.GREEN +f"GET users/{user} PASSED 😊" + TextColor.RESET + '\n'
        print(message)

def APIrepo(user, params):
    url = API_URL+f"/users/{user}/repos"
    # apireq = requests.get(url, params=params)
    # apijson = json.loads(apireq.text)
    apijson = APIcurl(url)

    # print(json.dumps(apijson, indent=2))

    repoData = []
    for repo in apijson:
        repo = {
                    'id': repo['id'],
                    'name': repo['name'],
                    'full_name' : repo['full_name'],
                    'owner' : {
                        'login' : repo['owner']['login'],
                        'id' :repo['owner']['id']
                    },
                    'private': repo['private'],
                    'html_url' : repo['html_url'],
                    'description' : repo['description'],
                    'fork': repo['fork'],
                    'url' : repo['url'],
                    'homepage': repo['homepage'],
                    'language' : repo['language'],
                    'forks_count': repo['forks_count'],
                    'stargazers_count' : repo['stargazers_count'],
                    'watchers_count': repo['watchers_count'],
                    'default_branch': repo['default_branch'],
                    'open_issues_count': repo['open_issues_count'],
                    'topics' : repo['topics'],
                    'has_issues' : repo['has_issues'],
                    'has_projects': repo['has_projects'],
                    'has_discussions': repo['has_discussions'],
                    'archived': repo['archived'],
                    'pushed_at': repo['pushed_at']
                }
        repoData.append(repo)
    return repoData

def TESTrepo(user, params):
    url = TEST_URL+f"/users/{user}/repos"
    testapi = requests.get(url, params=params)
    testjson = json.loads(testapi.text)

    # print(json.dumps(testjson, indent=2))

    repoData = []
    for repo in testjson:
        repo = {
                    'id': repo['id'],
                    'name': repo['name'],
                    'full_name' : repo['full_name'],
                    'owner' : {
                        'login' : repo['owner']['login'],
                        'id' :repo['owner']['id']
                    },
                    'private': repo['private'],
                    'html_url' : repo['html_url'],
                    'description' : repo['description'],
                    'fork': repo['fork'],
                    'url' : repo['url'],
                    'homepage': repo['homepage'],
                    'language' : repo['language'],
                    'forks_count': repo['forks_count'],
                    'stargazers_count' : repo['stargazers_count'],
                    'watchers_count': repo['watchers_count'],
                    'default_branch': repo['default_branch'],
                    'open_issues_count': repo['open_issues_count'],
                    'topics' : repo['topics'],
                    'has_issues' : repo['has_issues'],
                    'has_projects': repo['has_projects'],
                    'has_discussions': repo['has_discussions'],
                    'archived': repo['archived'],
                    'pushed_at': repo['pushed_at']
                }
        repoData.append(repo)
    return repoData

def test_repos(list):
    for user in list:
        api = APIrepo(user, list[user])
        test = TESTrepo(user, list[user])
        i = 0
        for repo in api:
            message = ""
            fail = False
            for key in repo.keys():
                if key not in test[i]:
                    # Dont have the field
                    fail = True
                    message = TextColor.RED + f"{key:<20} "+ TextColor.RESET + "field not found!"  + '\n'
                    continue

                if (api[i][key] == test[i][key] or api[i][key] == None and test[i][key] == "" or api[i][key] == "" and test[i][key] == None):
                    # got the right field
                    message += f"{key:<20} " + TextColor.GREEN + "Correct!" + TextColor.RESET + '\n'
                else:
                    fail = True
                    message += f"{key:<20} " + TextColor.RED + "Incorrect! 😞"+ TextColor.RESET + f"\n\tAPI  : \"{api[i][key]}\"\n\tTest : \"{test[i][key]}\"\n"
            
            if fail:
                message = TextColor.RED + f"GET users/{user}/repos/{api[i]['name']:<50} FAILED 😞" + TextColor.RESET + '\n' + message
            else:
                message = TextColor.GREEN +f"GET users/{user}/repos/{api[i]['name']:<50} PASSED 😊" + TextColor.RESET + '\n'
            print(message)
            i += 1

def getrepofilejson(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def getuserfiledata(filename):
    with open(filename, 'r') as file:
        return  file.read().splitlines()
    
usersjson = getuserfiledata("users.test")
reposjson = getrepofilejson("repos.test")

print(usersjson)

# test_user(usersjson)
test_repos(reposjson)