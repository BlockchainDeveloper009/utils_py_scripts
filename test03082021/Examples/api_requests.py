import requests

def api_get(url):
    resp = requests.get(url);
    print(resp)


owner = 'geekinfo1030'
repo_name = 'mystore'
f_name = 'last_run_csv.csv'
#'https://api.github.com/repos/'+owner+'/'+ repo_name +'/git/trees/master:Lib%2FMoQ'
get_url1 = 'https://api.github.com/repos/'+owner+'/' + repo_name +'/git/trees/tree_sha'

print(get_url1)

api_get(get_url1)

get_url2 = 'https://api.github.com/repos/geekinfo1030/mystore/contents/last_run_csv.csv'
print(get_url2)

t = api_get(get_url2)

print('get_url2=={}'.format(t))