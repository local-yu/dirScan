# coding=utf-8
from IPy import IP
import requests
from scapy.all import *
from scapy.layers.l2 import Ether, ARP


def save_txt(dict_list, filename="dict.txt"):
    with open(filename, "a") as f:
        for dict in dict_list:
            f.write(f"{dict}\n")

# ips = IP("172.16.116.0/24")

# ip里面是ip地址
# for ip in ips:
#     if ip == "172.16.116.0" or ip == "172.16.116.255":
#         continue
#     else:
#         print(ip)

# 先判断主机是否存活  ping arp      nmap
# arp去判断是否主机存活
# 构造arp包
arp_req = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst="172.16.116.0/24")

# 发送arp请求
arp_resq = srp(arp_req, timeout=2, verbose=0)[0]


dicts = {}
# 遍历ARP响应
for arp in arp_resq:
    mac = arp[1].hwsrc
    ip = arp[1].psrc
    # print(mac, ip)
    # 字典赋值
    dicts[ip] = mac

print(dicts)

# 再去进行端口测试
# 发请求80 443 8000 - 9000    1-65535
# 遍历字典

dict_list = []
for ip, mac in dicts.items():
    print(f"正在请求{ip}的80端口")
    try:
        res = requests.get("http://"+ip, timeout=0.5, verify=True)
        if res.status_code == 200:
            print(ip, "开放了80端口")
            dict_list.append(f"{ip}:80")
            print(dict_list)


# 协程  ===》 轻量级别的线程


        # res_2 = requests.get("https://" + ip, timeout=2, verify=True)
        # if res_2.status_code == 200:
        #     print(ip, "开放了443端口")
    except:
        pass

save_txt(dict_list)