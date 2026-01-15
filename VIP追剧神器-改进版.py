import tkinter
import webbrowser
import urllib.parse
from tkinter import ttk, messagebox

class VIPVideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('VIP追剧神器')
        self.root.geometry('480x240')
        self.create_widgets()

    def create_widgets(self):
        # 提示标签
        label_movie_link = tkinter.Label(self.root, text='输入视频网址：')
        label_movie_link.place(x=20, y=30, width=100, height=30)

        # 输入框
        self.entry_movie_link = tkinter.Entry(self.root)
        self.entry_movie_link.place(x=125, y=30, width=260, height=30)

        # 清空按钮
        button_movie_link = tkinter.Button(self.root, text='清空', command=self.empty)
        button_movie_link.place(x=400, y=30, width=50, height=30)

        # 解析接口选择
        self.parser_endpoints = [
            'https://jx.jsonplayer.com/player/?url=',
            'https://jx.playerjy.com/?url=',
            'https://jx.xmflv.cc/?url=',
            'https://www.yemu.xyz/?url=',
            'https://okjx.cc/?url=',
            'https://www.8090g.cn/jiexi/?url=',
            'https://jx.bozrc.com:4433/player/?url=',
            'https://www.ckplayer.vip/jiexi/?url='
        ]
        label_parser = tkinter.Label(self.root, text='选择解析接口：')
        label_parser.place(x=20, y=80, width=100, height=30)
        self.parser_var = tkinter.StringVar(value=self.parser_endpoints[0])
        combo_parser = ttk.Combobox(self.root, textvariable=self.parser_var, values=self.parser_endpoints, state='readonly')
        combo_parser.place(x=125, y=80, width=260, height=30)

        # 按钮控件
        button_movie1 = tkinter.Button(self.root, text='爱奇艺', command=self.open_iqy)
        button_movie1.place(x=25, y=120, width=80, height=40)

        button_movie2 = tkinter.Button(self.root, text='腾讯视频', command=self.open_tx)
        button_movie2.place(x=125, y=120, width=80, height=40)

        button_movie3 = tkinter.Button(self.root, text='优酷视频', command=self.open_yq)
        button_movie3.place(x=225, y=120, width=80, height=40)

        button_movie = tkinter.Button(self.root, text='播放VIP视频', command=self.play_video)
        button_movie.place(x=325, y=120, width=125, height=40)

        # 提示标签
        text = '提示：本案例仅供学习使用，不可作为他用。'
        lab_remind = tkinter.Label(self.root, text=text, fg='red', font=('Arial', 15, 'bold'))
        lab_remind.place(x=50, y=190, width=400, height=30)

        # 设置窗口大小
        self.root.resizable()

    def open_iqy(self):
        webbrowser.open('https://www.iqiyi.com')

    def open_tx(self):
        webbrowser.open('https://v.qq.com')

    def open_yq(self):
        webbrowser.open('https://www.youku.com/')

    def play_video(self):
        video = self.entry_movie_link.get().strip()
        if not video:
            try:
                messagebox.showwarning('提示', '请先输入完整的视频播放页链接')
            except Exception:
                pass
            return
        if not (video.startswith('http://') or video.startswith('https://')):
            video = 'https://' + video
        encoded_url = urllib.parse.quote(video, safe='')
        parse_api = 'https://jx.xmflv.cc/?url='
        if hasattr(self, 'parser_var'):
            try:
                value = self.parser_var.get()
                if value:
                    parse_api = value
            except Exception:
                pass
        webbrowser.open(parse_api + encoded_url)

    # https://jx.xmflv.cc/?url=
    def empty(self):
        self.entry_movie_link.delete(0, 'end')


if __name__ == '__main__':
    root = tkinter.Tk()
    app = VIPVideoApp(root)
    root.mainloop()