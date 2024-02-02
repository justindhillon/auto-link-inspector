import os, json, shutil, requests, subprocess
from bs4 import BeautifulSoup

###############################################################
# Puts all the urls of the trending github repos in repo_urls #
###############################################################

page = requests.get("https://github.com/trending")
soup = BeautifulSoup(page.content, "html.parser")

articles = soup.find_all("article")
repo_urls = []

for article in articles:
    h2 = article.find('h2', class_='h3').text
    repo_name = h2.replace("\n", "").replace(" ", "")
    repo_urls.append("https://github.com/" + repo_name)

#################################################
# Removes all the repo urls that are already    #
# scanned by comparing them with old_repos.json #
#################################################

try: # In a try catch in case old_repos.json doesn't exist
    with open("old_repos.json", 'r') as json_file:
        old_repos = json.load(json_file)
except:
    old_repos = []

# Filter out old repos
repo_urls = [item for item in repo_urls if item not in old_repos]

# If there are no new repos, stop the program
if (not repo_urls):
    print("There are no new trending repos!")
    quit()

# Add new repos to old_repos.json
with open("old_repos.json", 'w') as json_file:
    json.dump(old_repos + repo_urls, json_file)

##############################################
# Clone all the repos and run link-inspector #
##############################################

directory_path = 'repos'

# Delete old repos in directory_path
if os.path.exists(directory_path):
    shutil.rmtree(directory_path)
else:
    os.makedirs(directory_path)

# Clone the repos
for repo_url in repo_urls:
    repo_name = repo_url.split('/')[-1]
    target_path = os.path.join(directory_path, repo_name)
    subprocess.run(['git', 'clone', repo_url, target_path])

# Run link-inspector on directory_path
subprocess.run(['npx', 'link-inspector', directory_path])
