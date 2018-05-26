import uuid
from pip._vendor import requests


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        self.new_urls = url

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def get_content(self, new_url):
        print("正在下载: %s" %new_url)
        pic_name = 'pic/'+str(uuid.uuid4())+'.jpg'
        with open(pic_name, 'wb') as f:
            f.write(requests.get(new_url).content)