import os
from bs4 import BeautifulSoup

members = set()
for file in [file for file in os.listdir('./') if file.endswith('.html')]:
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
        avatars = soup.select('div[class*="avatar_"][aria-hidden="false"]')

        for avatar in avatars:
            members.add(avatar.get('aria-label'))

with open('out_list.txt', 'w', encoding='utf-8') as f:
    members = [f'"{member}"' for member in members]
    f.write("["+',\n'.join(members)+']')