# Semaphore用于控制进入数量的锁
# 文件, 读, 写, 写一般只适用于一个线程写, 读可以有多个

# 爬虫
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("http://baidu.com/{}".format(i), sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()