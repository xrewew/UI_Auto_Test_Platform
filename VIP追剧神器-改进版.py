# -*- coding: utf-8 -*-
"""
VIP追剧神器 - 视频解析工具
功能：通过多种解析接口解析VIP视频，支持爱奇艺、腾讯视频、优酷等平台
注意：本工具仅用于学习交流，请勿用于非法用途
"""

# 导入必要的库
import tkinter  # Python标准GUI库，用于创建图形界面
import webbrowser  # 用于打开网页
import urllib.parse  # 用于URL编码
from tkinter import ttk, messagebox  # 导入tkinter的高级组件和消息框


class VIPVideoApp:
    """VIP视频解析应用程序类"""

    def __init__(self, root):
        """
        构造函数，初始化应用程序

        参数:
            root: 主窗口对象
        """
        self.root = root  # 保存主窗口引用
        self.root.title('牢谢的看片神器')  # 设置窗口标题
        self.root.geometry('480x240')  # 设置窗口大小(宽度x高度)
        self.create_widgets()  # 调用方法创建界面组件

    def create_widgets(self):
        """创建界面组件和布局"""

        # 1. 视频网址输入区域
        # 提示标签：显示"输入视频网址："文本
        label_movie_link = tkinter.Label(self.root, text='输入视频网址：')
        label_movie_link.place(x=20, y=30, width=100, height=30)  # 设置标签位置和大小

        # 输入框：用于用户输入视频网址
        self.entry_movie_link = tkinter.Entry(self.root)
        self.entry_movie_link.place(x=125, y=30, width=260, height=30)  # 设置输入框位置和大小

        # 清空按钮：点击后清空输入框内容
        button_movie_link = tkinter.Button(self.root, text='清空', command=self.empty)
        button_movie_link.place(x=400, y=30, width=50, height=30)  # 设置按钮位置和大小

        # 2. 解析接口选择区域
        # 定义可用的视频解析接口列表
        self.parser_endpoints = [
            'https://jx.jsonplayer.com/player/?url=',  # 解析接口1
            'https://jx.playerjy.com/?url=',  # 解析接口2
            'https://jx.xmflv.cc/?url=',  # 解析接口3
            'https://www.yemu.xyz/?url=',  # 解析接口4
            'https://okjx.cc/?url=',  # 解析接口5
            'https://www.8090g.cn/jiexi/?url=',  # 解析接口6
            'https://jx.bozrc.com:4433/player/?url=',  # 解析接口7
            'https://www.ckplayer.vip/jiexi/?url='  # 解析接口8
        ]

        # 解析接口标签：显示"选择解析接口："文本
        label_parser = tkinter.Label(self.root, text='选择解析接口：')
        label_parser.place(x=20, y=80, width=100, height=30)  # 设置标签位置和大小

        # 创建字符串变量，用于存储选择的解析接口，默认值为第一个接口
        self.parser_var = tkinter.StringVar(value=self.parser_endpoints[0])

        # 创建下拉选择框：用于选择解析接口，设置为只读模式
        combo_parser = ttk.Combobox(
            self.root,
            textvariable=self.parser_var,  # 绑定变量
            values=self.parser_endpoints,  # 设置选项列表
            state='readonly'  # 设置为只读
        )
        combo_parser.place(x=125, y=80, width=260, height=30)  # 设置下拉框位置和大小

        # 3. 快捷访问按钮区域
        # 爱奇艺按钮：点击后打开爱奇艺官网
        button_movie1 = tkinter.Button(self.root, text='爱奇艺', command=self.open_iqy)
        button_movie1.place(x=25, y=120, width=80, height=40)  # 设置按钮位置和大小

        # 腾讯视频按钮：点击后打开腾讯视频官网
        button_movie2 = tkinter.Button(self.root, text='腾讯视频', command=self.open_tx)
        button_movie2.place(x=125, y=120, width=80, height=40)  # 设置按钮位置和大小

        # 优酷视频按钮：点击后打开优酷视频官网
        button_movie3 = tkinter.Button(self.root, text='优酷视频', command=self.open_yq)
        button_movie3.place(x=225, y=120, width=80, height=40)  # 设置按钮位置和大小

        # 播放VIP视频按钮：点击后执行视频解析和播放
        button_movie = tkinter.Button(self.root, text='播放VIP视频', command=self.play_video)
        button_movie.place(x=325, y=120, width=125, height=40)  # 设置按钮位置和大小

        # 4. 提示信息区域
        # 提示文本：提醒用户本工具仅供学习使用
        text = '提示：本脚本牢谢所有，不可作为商用。'
        lab_remind = tkinter.Label(
            self.root,
            text=text,
            fg='red',  # 设置文本颜色为红色
            font=('Arial', 15, 'bold')  # 设置字体样式：Arial字体，15号大小，粗体
        )
        lab_remind.place(x=50, y=190, width=400, height=30)  # 设置提示标签位置和大小

        # 设置窗口是否可调整大小(默认可以调整)
        self.root.resizable()

    def open_iqy(self):
        """打开爱奇艺官网"""
        webbrowser.open('https://www.iqiyi.com')  # 使用默认浏览器打开爱奇艺官网

    def open_tx(self):
        """打开腾讯视频官网"""
        webbrowser.open('https://v.qq.com')  # 使用默认浏览器打开腾讯视频官网

    def open_yq(self):
        """打开优酷视频官网"""
        webbrowser.open('https://www.youku.com/')  # 使用默认浏览器打开优酷视频官网

    def play_video(self):
        """解析并播放视频的核心方法"""

        # 1. 获取用户输入的视频网址并去除首尾空格
        video = self.entry_movie_link.get().strip()

        # 2. 验证输入是否为空
        if not video:
            try:
                messagebox.showwarning('提示', '请先输入完整的视频播放页链接')  # 弹出警告提示
            except Exception:
                pass  # 忽略可能的异常
            return  # 输入为空，直接返回

        # 3. 确保视频网址包含协议头(http://或https://)
        if not (video.startswith('http://') or video.startswith('https://')):
            video = 'https://' + video  # 自动添加https://协议头

        # 4. 对视频网址进行URL编码
        encoded_url = urllib.parse.quote(video, safe='')  # safe=''表示对所有特殊字符进行编码

        # 5. 设置默认解析接口
        parse_api = 'https://jx.xmflv.cc/?url='

        # 6. 如果用户选择了其他解析接口，则使用用户选择的接口
        if hasattr(self, 'parser_var'):
            try:
                value = self.parser_var.get()  # 获取用户选择的解析接口
                if value:
                    parse_api = value  # 更新解析接口
            except Exception:
                pass  # 忽略可能的异常

        # 7. 拼接解析接口URL和编码后的视频网址，然后使用浏览器打开
        webbrowser.open(parse_api + encoded_url)

    def empty(self):
        """清空视频网址输入框"""
        self.entry_movie_link.delete(0, 'end')  # 删除输入框中从位置0到末尾的所有内容


# 程序入口
if __name__ == '__main__':
    root = tkinter.Tk()  # 创建主窗口对象
    app = VIPVideoApp(root)  # 创建应用程序实例
    root.mainloop()  # 启动主窗口消息循环，等待用户交互
