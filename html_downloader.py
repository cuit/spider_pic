from pip._vendor import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        response = requests.get(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
        response.encoding = 'utf-8'  #必须添加此项，否则会出现乱码
        if response.status_code != 200:
            return None
        return response.text