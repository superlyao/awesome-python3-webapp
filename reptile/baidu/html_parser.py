# coding:utf-8
import re

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_data(self, url, soup):
        res_data = {}
        res_data['url'] = url
        res_data['title'] = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
        res_data['summary'] = soup.find('div', class_='lemma-summary').get_text()
        return res_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item'))
        for link in links:
            new_url = link['href']
            new_full_url = 'https://baike.baidu.com' + new_url
            new_urls.add(new_full_url)
        return new_urls
