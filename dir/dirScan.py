# coding=utf-8
import requests
# 面向对象的思维来写
class Mulu:
    def __init__(self):
        pass

    # 取出字典内容
    """
    返回的是一个列表
    """
    def get_contents(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            # 去除\n换行方法
            dict_list = f.read().splitlines()
        return dict_list

    """
    拼接url
    返回值是一个列表，是我们测试能够访问到的url
    """
    def get_url(self, url, dict_list):
        new_url_list = []
        for value in dict_list:
            new_url = "http://" + url + '/' + value
            res = requests.get(new_url)

            # 对请求的结果进行识别
            if res.status_code == 200 or res.status_code == 403 or res.status_code == 302:
                new_url_list.append(new_url)
        return new_url_list

if __name__ == '__main__':
    # 实例化对象
    mulu = Mulu()
    dict_list = mulu.get_contents('./php.txt')
    url = input("请输入你需要扫描的url（不含协议）")
    for i in mulu.get_url(url, dict_list):
        print(i)
