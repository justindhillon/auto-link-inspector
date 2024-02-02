import os
import json
import shutil
import requests
import subprocess
from bs4 import BeautifulSoup

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

def remove_existing_strings(new_array, existing_array):
    return [item for item in new_array if item not in existing_array]

URL = "https://github.com/trending"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
articles = soup.find_all("article")

new_array = []

for article in articles:
    articl = article.find_all("h2")
    for artic in articl:
        arti = artic.find_all("a")
        for art in arti:
            link = art["href"]
            new_array.append("https://github.com" + link)

json_filename = "data.json"
existing_array = load_from_json(json_filename)
filtered_array = remove_existing_strings(new_array, existing_array)
save_to_json(existing_array + filtered_array, json_filename)

def delete_directory(directory_path):
    # Iterate over all items in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        # Check if it's a file or a directory
        if os.path.isfile(item_path):
            # If it's a file, delete it
            os.remove(item_path)
        elif os.path.isdir(item_path):
            # If it's a directory, delete it recursively using shutil.rmtree
            shutil.rmtree(item_path)

def download_repositories(urls, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for url in urls:
        # Extract repository name from URL
        repo_name = url.split('/')[-1].rstrip('.git')

        # Clone the repository
        target_path = os.path.join(target_directory, repo_name)
        subprocess.run(['git', 'clone', url, target_path])

directory_path = 'repos'

delete_directory(directory_path)
download_repositories(filtered_array, directory_path)
subprocess.run(['npx', 'link-inspector', directory_path])
