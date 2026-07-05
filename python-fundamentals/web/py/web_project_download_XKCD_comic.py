#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/11/8 15:34
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : web_project_download_XKCD_comic.py
# @Software: PyCharm

import requests, bs4, os
from urllib.parse import urljoin, urlparse

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
for _ in range(4):  # 使用下划线作为循环变量，表示我们不关心循环的索引
    # Download the page.
    print(f'Downloading the page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comic_elem = soup.select('#comic img')
    if comic_elem:
        comic_url = comic_elem[0]['src']

        # 检查 comic_url 是否以 '//' 开头，如果是，则添加 'https:'
        if comic_url.startswith('//'):
            comic_url = 'https:' + comic_url

        # 确保 comic_url 是绝对的
        parsed_url = urlparse(comic_url)
        if not parsed_url.netloc:  # 这通常不会发生，因为我们已经处理了 '//' 的情况
            # 但如果仍然发生，可能是因为 comic_url 是完全错误的
            print('Invalid comic URL:', comic_url)
            continue  # 跳过这个页面
        # Download the image
        print(f'Downloading image from {comic_url}')
        image_res = requests.get(comic_url)
        image_res.raise_for_status()
        # Save the image to ./xkcd
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in image_res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    else:
        print('Could not find comic image')
        break  # 如果找不到漫画图片，则退出循环

    # Get the Prev button's URL
    prev_links = soup.select('a[rel="prev"]')
    if prev_links:
        url = 'http://xkcd.com' + prev_links[0].get('href')
    else:
        print('No previous link found, stopping.')
        break  # 如果没有前一个链接，则退出循环

print('Done.')