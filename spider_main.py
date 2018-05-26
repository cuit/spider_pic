import url_manager, html_downloader, html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()

    def craw(self, root_url, flag, join_url = None):
        'flag:标志位显示发起第二次请求的链接是否需要重新拼接'
        count = 1
        html_content = self.downloader.download(root_url)
        new_urls = self.parser.parse(html_content, flag, join_url)
        self.urls.add_new_url(new_urls)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d: %s" %(count, new_url))
                self.urls.get_content(new_url)
                if count == 1000:
                    break
                count += 1
            except:
                print("craw failed")
        print("成功下载: %d 张图片" %count)

if __name__ == "__main__":

    # 第一种图片源地址需要拼接
    root_url = "http://www.quanjing.com/Free/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, True, "http://www.quanjing.com")
    # 或
    # 第二种图片源地址不需要拼接
    # root_url = "http://tu.duowan.com/tu"
    # obj_spider = SpiderMain()
    # obj_spider.craw(root_url, False)