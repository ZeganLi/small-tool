import requests
from tkinter import *
import hashlib
import time
from openpyxl import Workbook
import _thread as thread
import os.path
#获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time

'''读取http请求的地址信息'''
def read_request_address():
    try:
        request_file = open(os.path.join(os.getcwd(),"address.txt") ,'r');
        return request_file.readlines()
    except IOError as e:
        print(e)
    finally:
        request_file.close()

def start_monitor():
    re_list = read_request_address()
    try:
        create_dir()
        join = os.path.join(os.getcwd(), '监控日志', time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.txt')
        log_file = open(join, 'a+')
        log_file.writelines("读取到" + str(len(re_list)) + "个URL地址。" + "开始对其进行监控" + '\n')
        while True:
            content = ""
            for re in re_list:
                replace_re = re.replace('\n', '')
                try:
                    r = requests.get(replace_re,timeout=5)
                    content = log_content(r.status_code, replace_re)
                    log_file.write(content)
                    log_file.flush()
                except:
                    content = log_content("连接失败！",replace_re)
                    log_file.write(content)
                    log_file.flush()
            time.sleep(2)
    except Exception as e:
        log_file.write(e.__context__ + '\n')
    finally:
        log_file.close()


def log_content(r, replace_re):
    return str(get_current_time() + ":" + '\t'  + replace_re + '\t' + str(r) + '\n')


def create_dir():
    if not os.path.exists(os.path.join(os.getcwd(), '监控日志')):
        os.mkdir(os.path.join(os.getcwd(), '监控日志'))


if __name__ == '__main__':
    print("监控工具已启动，请查看日志文件。。。")
    start_monitor()