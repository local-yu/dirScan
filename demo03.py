# coding=utf-8
import demo02
if __name__ == '__main__':



    url = input("请输入需要处理的url地址：")
    zidian = demo02.Zidian(url=url, file_name="muben.txt", new_file_name="new_dict.txt")
    zidian.put_txt_contents()
