import datetime as dt
from github_contents import GithubContents

# For repo simonw/disaster-data:
GITHUB_OAUTH_TOKEN = '19c724addb0023b2cf4f3475e00dad3bb3da87db'
github = GithubContents(
    "geekinfo1030",
    "mystore",
    token=GITHUB_OAUTH_TOKEN,
    branch="main"
)


def read_github_file(path_within_repo):
    t = content_in_bytes, sha = github.read(path_within_repo)
    return t


def write_github_file(path_within_repo, contents_in_bytes, previous_sha, commit_message):
    content_sha, commit_sha = github.write(
        filepath=path_within_repo,
        content_bytes=contents_in_bytes,
        sha=previous_sha,  # Optional
        commit_message=commit_message,
        committer={
            "name": 'harish',
            "email": 'geekinfo1030@gmail.com',
        },
    )
def fetch_date():
    csv_in_bytes = read_github_file(file_types[3])
    csv_in_str = str(csv_in_bytes)
    date_str = csv_in_str[2:csv_in_str.find(", ")]
    date_str = date_str.replace("'", "")
    print('dat_______time = '+date_str)
    date_dt = dt.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

    if(dt.datetime.today().now() > date_dt ):
        print('date=' + str(date_dt))
        print('current time= '+str(dt.datetime.today().now()))
    else:
        print('comparison dint work ')




file_types = ['run_date.csv', 'date.json', 'previous_day.csv', 'last_run_csv.csv']
raw_path_within_repo= 'https://raw.githubusercontent.com/geekinfo1030/mystore/main/'+file_types[1]


csv_in_bytes = read_github_file(file_types[3])

csv_in_str = str(csv_in_bytes)
print('csv_in_str='+csv_in_str)
fetch_date()
tam = csv_in_str[csv_in_str.find(", ")+2:]
two_sha = tam.replace("'", "").replace(")", "")
print('sha = '+two_sha)


today_dt = dt.datetime.today()
today_str = str(today_dt)
#today_bytes = bytes("123", 'utf-8')# bytes(today_str, 'utf-8')
today_bytes =  bytes(today_str, 'utf-8')

write_github_file(file_types[3], today_bytes, two_sha, 'second run')

csv_in_bytes = read_github_file(file_types[3])

print(csv_in_bytes)

