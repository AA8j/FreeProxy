# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 10:30
# @Author  : AA8j
# @FileName: CrawlFreeProxyIP.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
import requests
import threading


def check_proxy(check_ip: dict):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    try:
        # 6秒内通过测试
        r = requests.get('http://www.baidu.com', headers=headers, proxies=check_ip, timeout=time_out)
        if r.status_code == 200:
            # 验证成功
            return True
    except:
        # 验证失败
        return False


def read_ip():
    ip_list = []
    try:
        print('正在读取ip...', end='')
        with open('save/ips.txt', 'r') as f:
            for ip in f:
                ip_dic = eval(ip.split('\n')[0])
                ip_list.append(ip_dic)
        print(f'读取成功！共读取{len(ip_list)}条。')
        return ip_list
    except Exception as e:
        print('读取失败！')
        raise e


def save_success_ip(ip_lsit):
    try:
        with open('save/success_ips.txt', 'w') as f:
            for i in ip_lsit:
                f.write(str(i) + '\n')
        print(f'保存成功！共保存{len(ip_lsit)}条。')
    except Exception as e:
        print('保存失败！', e)


# 创建一个线程类
class MyThread(threading.Thread):
    def __init__(self, proxy_ip: dict):
        super().__init__()
        self.proxy_ip = proxy_ip

    def run(self):
        # 如果通过了检测，则加入可用代理列表
        with threading_max:
            Flag = check_proxy(self.proxy_ip)
            # 防止同时输出
            with lock:
                if Flag:
                    SuccessProxyList.append(self.proxy_ip)
                    print(threading.current_thread().name.ljust(12), str(self.proxy_ip).ljust(35), '--------验证成功！√'.ljust(15))
                else:
                    print(threading.current_thread().name.ljust(12), str(self.proxy_ip).ljust(35), '--------验证失败！'.ljust(15))


if __name__ == '__main__':
    # 读取已经爬取的IP
    IpList = read_ip()
    # 多线程验证代理
    # 成功代理的列表
    SuccessProxyList = []
    # 最大并发线程数量
    max_num = 30
    threading_max = threading.Semaphore(max_num)
    # 超时时间
    time_out = 6
    # 同步锁，防止同时输出
    lock = threading.Lock()

    # 创建线程池
    ThreadList = []
    for i in IpList:
        thread = MyThread(i)
        ThreadList.append(thread)
    print(f'开始验证...（线程数：{max_num}、超时时间：{time_out}）')
    for i in ThreadList:
        i.start()

    for i in ThreadList:
        i.join()

    save_success_ip(SuccessProxyList)
