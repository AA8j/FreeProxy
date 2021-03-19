# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 10:30
# @Author  : AA8j
# @FileName: CrawlFreeProxy.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
import time
import requests
import re


def get_7yip():
    print('正在抓取7yip...')
    # 将抓取到的代理存入列表
    ip_dic_list = []
    for i in range(10):
        try:
            print(f'正在抓取第{i + 1}(10)页：')
            headers = {
                'Host': 'www.7yip.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'Referer': 'https://www.7yip.cn/free/?action=china&page=1'
            }
            url = 'https://www.7yip.cn/free/?action=china&page=' + str(i + 1)
            r = requests.get(url, headers=headers, timeout=8)
            # 获得页面
            html_7yip = r.text
            # 抓取协议，IP，端口
            protocol = re.findall(r'<td data-title="类型">(.*?)<', html_7yip)
            IP = re.findall(r'<td data-title="IP">(.*?)<', html_7yip)
            PORT = re.findall(r'<td data-title="PORT">(.*?)<', html_7yip)

            for j in range(10):
                ip_dic = {protocol[j]: IP[j] + ':' + PORT[j]}
                print(ip_dic, end='')
                ip_dic_list.append(ip_dic)
            print()

        except Exception as e:
            print('抓取失败！', e)
    print(f'7yip抓取结束，共抓取{len(ip_dic_list)}个代理。')
    return ip_dic_list


def get_kuaidaili():
    print('正在抓取快代理ip...')
    # 将抓取到的代理存入列表
    ip_dic_list = []
    for i in range(10):
        try:
            print(f'正在抓取第{i + 1}(10)页：')
            headers = {
                'Host': 'www.kuaidaili.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
            }
            url = 'https://www.kuaidaili.com/free/intr/' + str(i + 1)
            r = requests.get(url, headers=headers, timeout=8)
            # 获得页面
            html_kauidaili = r.text
            # 抓取协议，IP，端口
            protocol = re.findall(r'<td data-title="类型">(.*?)<', html_kauidaili)
            IP = re.findall(r'<td data-title="IP">(.*?)<', html_kauidaili)
            PORT = re.findall(r'<td data-title="PORT">(.*?)<', html_kauidaili)
            # 等待正则捕获
            time.sleep(1)
            for j in range(15):
                ip_dic = {protocol[j]: IP[j] + ':' + PORT[j]}
                print(ip_dic, end='')
                ip_dic_list.append(ip_dic)
            print()

        except Exception as e:
            print('抓取失败！', e)
    print(f'kuaidaili代理抓取结束，共抓取{len(ip_dic_list)}个代理。')
    return ip_dic_list


def save_ip():
    try:
        print(f'正在保存代理ip...（共{len(proxies)}条）。', end='')
        with open('save/ips.txt', 'w') as f:
            for ip in proxies:
                f.write(str(ip).lower() + '\n')
        print('保存成功！')
    except Exception as e:
        print('保存失败！', e)


if __name__ == '__main__':
    # 抓取7yip和kuaidaili的代理ip，并合并
    proxies = get_7yip() + get_kuaidaili()
    # 保存ip
    save_ip()
