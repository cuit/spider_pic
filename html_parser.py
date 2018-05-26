from bs4 import BeautifulSoup
import urllib.parse


class HtmlParser(object):
    def _get_new_urls(self, soup, flag, join_url):
        new_urls = set()
        links = soup.find_all('img')
        for link in links:
            new_url = link['src']
            if flag:
                new_url = urllib.parse.urljoin(join_url, new_url)
            new_urls.add(new_url)
        return new_urls

    def parse(self, html_content, flag, join_url):
        if html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        new_urls = self._get_new_urls(soup, flag, join_url)
        return new_urls


