import requests
from tkinter import *
import hashlib
import time

LOG_LINE_NUM = 0
class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("应用监控小工具_v1.0")                           #窗口名
        self.init_window_name.geometry('1068x681+10+10')
        # self.init_window_name["bg"] = "black"                                   #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #文本框
        self.log_data_Text = Text(self.init_window_name, width=1068, height=681)  # 日志框
        self.log_data_Text.grid(row=1, column=0, columnspan=10)

        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="开始监控",bg="lightblue", width=10,command=self.start_monitor)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=0, column=0)

    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        self.log_data_Text.insert(END, logmsg_in)
        LOG_LINE_NUM = LOG_LINE_NUM + 1

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time

    def start_monitor(self):
        re_list = read_request_address()
        print("读取到" + str(len(re_list)) + "URL地址。" + "开始对其进行监控")
        # while True:
        for re in re_list:
            replace_re = re.replace('\n', '')
            r = requests.get(replace_re)
            self.write_log_to_Text(r.status_code)

'''读取http请求的地址信息'''
def read_request_address():
    try:
        request_file = open("./address.txt",'r');
        return request_file.readlines()
    except IOError as e:
        print(e)
    finally:
        request_file.close()

if __name__ == '__main__':

    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)

    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    # 开始监控
    # start_monitor()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示