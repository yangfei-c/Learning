#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/11/8 15:34
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : web_project_download_XKCD_comic.py
# @Software: PyCharm

import requests,bs4,os

url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print(f'Download the page {url}...')
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text)

    # Find thr url of the comic image
    comic_elem=soup.select('#comic img')
    if comic_elem==[]:
        print('Could not find comic image')
    else:
        comic_url=comic_elem[0].get('src')
        # Download the image
        print(f'Downloading image a{comic_url}')
        res=requests.get(comic_url)
        res.raise_for_status()
         # Save the image to ./xkcd
        image_file=open(os.path.join('xkcd',os.path.basename(comic_url)),'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # Get the Prev button's url
    prev_link=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prev_link.get('href')
print('Done.')