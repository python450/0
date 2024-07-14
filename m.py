import time
import pygame
import re
import requests
import threading
import tkinter as tk
from tkinter import ttk
import webbrowser
from lxml import etree
from tkinter import messagebox, scrolledtext
from tqdm import tqdm
from bs4 import BeautifulSoup
import os
import librosa
import soundfile as sf
import pyttsx3
import json
from PIL import Image
import torch.utils
import win32api
import win32con
import win32gui
import cv2
from tkinter import filedialog

def fn111():
    # 按钮的功能
    def an7():
        cn.insert(tk.END, "7")

    def an8():
        cn.insert(tk.END, "8")

    def an9():
        cn.insert(tk.END, "9")

    def an4():
        cn.insert(tk.END, "4")

    def an5():
        cn.insert(tk.END, "5")

    def an6():
        cn.insert(tk.END, "6")

    def an1():
        cn.insert(tk.END, "1")

    def an2():
        cn.insert(tk.END, "2")

    def an3():
        cn.insert(tk.END, "3")

    def an0():
        cn.insert(tk.END, "0")

    def an11():
        cn.insert(tk.END, "+")

    def an12():
        cn.insert(tk.END, "-")

    def an13():
        cn.insert(tk.END, "*")

    def an14():
        cn.insert(tk.END, "/")

    def an17():
        cn.delete("0", tk.END)

    def an18():
        cn.insert(tk.END, ".")

    def an15():
        try:
            s = cn.get()
            f = eval(s)
            cn.delete("0", tk.END)
            cn.insert(tk.END, f)
        except Exception:
            cn.delete("0", tk.END)
            cn.insert(tk.END, "请输入正确的算式！")

    root = tk.Tk()
    root.title("计算器")
    root.geometry("310x350")
    root.resizable(width=False, height=False)
    # 创建按钮和输入框
    cn = tk.Entry(root, font=("微软雅黑", 20))
    cn.pack()

    sn1 = tk.Button(root, text="7", width=6, height=2, command=an7)
    sn1.place(x=10, y=45)

    sn2 = tk.Button(root, text="8", width=6, height=2, command=an8)
    sn2.place(x=70, y=45)

    sn3 = tk.Button(root, text="9", width=6, height=2, command=an9)
    sn3.place(x=130, y=45)

    sn4 = tk.Button(root, text="4", width=6, height=2, command=an4)
    sn4.place(x=10, y=105)

    sn5 = tk.Button(root, text="5", width=6, height=2, command=an5)
    sn5.place(x=70, y=105)

    sn6 = tk.Button(root, text="6", width=6, height=2, command=an6)
    sn6.place(x=130, y=105)

    sn7 = tk.Button(root, text="1", width=6, height=2, command=an1)
    sn7.place(x=10, y=165)

    sn8 = tk.Button(root, text="2", width=6, height=2, command=an2)
    sn8.place(x=70, y=165)

    sn9 = tk.Button(root, text="3", width=6, height=2, command=an3)
    sn9.place(x=130, y=165)

    sn0 = tk.Button(root, text="0", width=23, height=2, command=an0)
    sn0.place(x=10, y=225)

    sn11 = tk.Button(root, text="+", width=6, height=2, command=an11)
    sn11.place(x=190, y=45)

    sn12 = tk.Button(root, text="-", width=6, height=2, command=an12)
    sn12.place(x=190, y=105)

    sn13 = tk.Button(root, text="*", width=6, height=2, command=an13)
    sn13.place(x=190, y=165)

    sn14 = tk.Button(root, text="/", width=6, height=2, command=an14)
    sn14.place(x=190, y=225)

    sn15 = tk.Button(root, text="=", width=23, height=2, command=an15)
    sn15.place(x=10, y=285)

    sn16 = tk.Button(root, text="c", width=6, height=2, command=an17)
    sn16.place(x=190, y=285)

    sn17 = tk.Button(root, text=".", width=6, height=2, command=an18)
    sn17.place(x=250, y=45)

    root.mainloop()


# 每一个按钮的功能
def fn112():
    def an1():
        if sn12.get().lower() in ["get", "post"]:
            try:
                timestamp = int(time.time())
                url = sn1.get()
                messagebox.showinfo("提示", "找到保存的位置")
                path = filedialog.askdirectory()
                path2 = f"{path}\\{timestamp}.png"
                method = sn12.get().lower()

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                    "Referer": url
                }

                request_method = getattr(requests, method)
                resp = request_method(url, headers=headers)

                with open(path2, "wb") as f:
                    f.write(resp.content)
                messagebox.showinfo("提示", "下载成功！")
            except Exception as e:
                messagebox.showerror("错误", f"下载失败:{e}")
        else:
            messagebox.showerror("警告", f"请输入get/post，而不是：{sn12.get()}")

    def an2():
        sn1.delete(0, tk.END)
        sn12.delete(0, tk.END)

    root = tk.Tk()
    root.title("照片下载")
    root.geometry("400x450")
    root.resizable(False, False)

    qn1 = ttk.Label(root, text="输入照片链接", font=("微软雅黑", 10))
    qn1.pack()
    sn1 = ttk.Entry(root, font=("微软雅黑", 20))
    sn1.pack()

    qn2 = ttk.Label(root, text="输入请求方式:get/post", font=("微软雅黑", 10))
    qn2.pack()
    sn12 = ttk.Entry(root, font=("微软雅黑", 20))
    sn12.pack()

    qn3 = ttk.Label(root, text="提示：链接要检查里的链接，也可以右键选择", font=("微软雅黑", 15))
    qn3.pack()

    qn4 = ttk.Label(root, text="复制图像链接（如果没有就用第一种方法）", font=("微软雅黑", 15))
    qn4.pack()

    dn1 = ttk.Button(root, text="开始", command=an1)
    dn1.pack(pady=10)

    dn2 = ttk.Button(root, text="清空", command=an2)
    dn2.pack(pady=10)

    root.mainloop()


def fn113():
    def an1111():
        if sn12.get().lower() in ["get", "post"]:
            try:
                url = sn11.get()
                method = sn12.get().lower()

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                    "Referer": url
                }

                request_method = getattr(requests, method)
                resp = request_method(url, headers=headers)

                source_code.delete(1.0, tk.END)
                source_code.insert(tk.END, resp.text)
                messagebox.showinfo("提示", "提取成功！")
            except Exception as d:
                messagebox.showerror("错误", f"提取失败{d}")
        else:
            messagebox.showerror("警告", f"请输入get/post，而不是：{sn12.get()}")

    def an1112():
        sn11.delete(0, tk.END)
        sn12.delete(0, tk.END)
        source_code.delete(1.0, tk.END)

    root = tk.Tk()
    root.title("页面源代码提取")
    root.geometry("400x450")

    qn1 = ttk.Label(root, text="输入源代码链接", font=("微软雅黑", 10))
    qn1.pack()
    sn11 = ttk.Entry(root, font=("微软雅黑", 20))
    sn11.pack()

    qn2 = ttk.Label(root, text="输入请求方式:get/post", font=("微软雅黑", 10))
    qn2.pack()
    sn12 = ttk.Entry(root, font=("微软雅黑", 20))
    sn12.pack()

    qn3 = ttk.Label(root, text="提示：直接用网页的链接就可以了", font=("微软雅黑", 15))
    qn3.pack()

    dn1 = ttk.Button(root, text="开始", command=an1111)
    dn1.pack(pady=10)

    dn2 = ttk.Button(root, text="清空", command=an1112)
    dn2.pack(pady=10)

    source_code = scrolledtext.ScrolledText(root, font=("微软雅黑", 10), height=15)
    source_code.pack(pady=10)

    root.mainloop()


def fn114():
    def an1111():
        if sn15.get().lower() in ["get", "post"]:
            timestamp2 = int(time.time())
            url = sn11.get()
            messagebox.showinfo("提示", "找到保存的位置")
            path = filedialog.askdirectory()
            path2 = f"{path}\\{timestamp2}.mp3"
            method = sn15.get().lower()

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                "Referer": "https://www.baidu.com"
            }

            requests_method = getattr(requests, method)
            resp = requests_method(url, headers=headers)

            with open(path2, "wb") as f:
                f.write(resp.content)
            messagebox.showinfo("提示", "下载成功！")
        else:
            messagebox.showerror("警告", f"请输入get/post，而不是：{sn15.get()}")

    def an1112():
        sn11.delete(0, tk.END)
        sn15.delete(0, tk.END)

    root = tk.Tk()
    root.title("音乐下载")
    root.geometry("400x450")
    root.resizable(False, False)

    qn1 = ttk.Label(root, text="输入音乐链接", font=("微软雅黑", 10))
    qn1.pack()
    sn11 = ttk.Entry(root, font=("微软雅黑", 20))
    sn11.pack()

    qn2 = ttk.Label(root, text="输入请求方式:get/post", font=("微软雅黑", 10))
    qn2.pack()
    sn15 = ttk.Entry(root, font=("微软雅黑", 20))
    sn15.pack()

    qn3 = ttk.Label(root, text="提示：链接要打开开发者模式中的网络", font=("微软雅黑", 15))
    qn3.pack()

    qn4 = ttk.Label(root, text="里面的mp3格式文件", font=("微软雅黑", 15))
    qn4.pack()

    dn1 = ttk.Button(root, text="开始", command=an1111)
    dn1.pack(pady=10)

    dn2 = ttk.Button(root, text="清空", command=an1112)
    dn2.pack(pady=10)

    root.mainloop()


def fn115():
    def an1111():
        if sn10.get().lower() in ["get", "post"]:
            try:
                timestamp2 = int(time.time())
                url = sn11.get()
                messagebox.showinfo("提示", "找到保存的位置")
                path = filedialog.askdirectory()
                path2 = f"{path}\\{timestamp2}.mp4"
                method = sn10.get().lower()

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                    "Referer": "https://www.baidu.com"
                }

                requests_method = getattr(requests, method)
                resp = requests_method(url, headers=headers)

                with open(path2, "wb") as f:
                    f.write(resp.content)
                messagebox.showinfo("提示", "下载成功！")
            except Exception as e:
                messagebox.showerror("错误", f"下载失败:{e}")
        else:
            messagebox.showerror("警告", f"请输入get/post，而不是{sn10.get()}")

    def an1112():
        sn11.delete(0, tk.END)
        sn10.delete(0, tk.END)

    root = tk.Tk()
    root.title("视频下载")
    root.geometry("400x450")
    root.resizable(False, False)

    qn1 = ttk.Label(root, text="输入视频链接", font=("微软雅黑", 10))
    qn1.pack()
    sn11 = ttk.Entry(root, font=("微软雅黑", 20))
    sn11.pack()

    qn2 = ttk.Label(root, text="输入请求方式:get/post", font=("微软雅黑", 10))
    qn2.pack()
    sn10 = ttk.Entry(root, font=("微软雅黑", 20))
    sn10.pack()

    qn3 = ttk.Label(root, text="提示：链接要打开开发者模式中的网络", font=("微软雅黑", 15))
    qn3.pack()

    qn4 = ttk.Label(root, text="里面的mp4格式文件", font=("微软雅黑", 15))
    qn4.pack()

    qn5 = tk.Label(root, text="提示：一部分视频可能会因为反爬无法下载！", font=("微软雅黑", 15), fg="red")
    qn5.pack()

    dn1 = ttk.Button(root, text="开始", command=an1111)
    dn1.pack(pady=10)

    dn2 = ttk.Button(root, text="清空", command=an1112)
    dn2.pack(pady=10)

    root.mainloop()


def fn116():
    def bth11():
        try:
            # 按钮的功能
            a = en1.get()
            b = en2.get()
            c = en3.get()

            unm_max = max(a, b, c)
            messagebox.showinfo("提示", f"最大的数是{unm_max}")
        # 程序出错的代码
        except Exception as v:
            messagebox.showerror("错误", v)

    def bth12():
        en1.delete(0, tk.END)
        en2.delete(0, tk.END)
        en3.delete(0, tk.END)

    # 创建窗口
    root2 = tk.Tk()
    root2.title("三个数取最大值")
    root2.geometry("400x450")
    root2.resizable(width=False, height=False)
    # 创建界面
    le = ttk.Label(root2, text="请在下面的输入框内输入三个数", font=("微软雅黑", 15))
    le.pack()

    en1 = ttk.Entry(root2, width=10, font=("微软雅黑", 10))
    en1.place(x=60, y=30)

    en2 = ttk.Entry(root2, width=10, font=("微软雅黑", 10))
    en2.place(x=155, y=30)

    en3 = ttk.Entry(root2, width=10, font=("微软雅黑", 10))
    en3.place(x=250, y=30)

    bth1 = ttk.Button(root2, text="开始", command=bth11)
    bth1.place(x=157, y=80)

    bth2 = ttk.Button(root2, text="清空", command=bth12)
    bth2.place(x=157, y=120)

    root2.mainloop()


def fn117():
    def bth1():
        # 计算数量
        text = sor.get("1.0", "end-1c")
        count = len(text.replace(" ", ""))
        messagebox.showinfo("提示", f"这个文本一共有{count}个字")

    # 点击清空后
    def an1112():
        sor.delete("1.0", "end-1c")

    # 创建窗口
    root = tk.Tk()
    root.title("文本字数计算")
    root.geometry("400x450")
    root.resizable(width=False, height=False)
    # 创建界面
    la1 = ttk.Label(root, text="在下面输入文本", font=("微软雅黑", 20))
    la1.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    dn2 = ttk.Button(root, text="清空", command=an1112)
    dn2.pack(pady=10)

    sor = scrolledtext.ScrolledText(root, font=("微软雅黑", 10), height=15)
    sor.pack(pady=10)

    root.mainloop()


def fn118():
    # 创建按钮功能
    def bth1():
        a = en1.get()
        url = f"https://cn.bing.com/images/search?q={a}&form=HDRSC2&first=1"
        messagebox.showinfo("提示", "找到保存的位置")
        path = filedialog.askdirectory()
        print(a)
        print(path)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            "Referer": "https://www.baidu.com"
        }
        resp = requests.get(url, headers=headers)
        text = resp.text

        url2 = []
        obj = re.compile(r'<a class="iusc".*?src="(?P<url1>.*?)"', re.S)
        obj2 = obj.finditer(text)

        for i in obj2:
            url1 = i.group("url1")
            if url1.startswith('http://') or url1.startswith('https://'):
                url2.append(url1)
            else:
                pass
        try:
            for a, url21 in enumerate(url2):
                if url21.startswith("http://") or url21.startswith("https://"):
                    resp2 = requests.get(url21)
                    size = int(resp2.headers.get('content-length', 0))

                    if size > 1024:
                        path2 = f"{path}\\{int(time.time())}_{a + 1}.png"
                        if resp2.status_code == 200:
                            with open(path2, "wb") as f:
                                f.write(resp2.content)
                        else:
                            messagebox.showerror("错误", f"第{a + 1}个图片下载失败！")
                    else:
                        continue
                else:
                    continue
            messagebox.showinfo("提示", "下载完成！")
        except Exception as e:
            messagebox.showerror("错误", f"下载失败，原因：{e}")

    def bth2():
        en1.delete(0, tk.END)

    # 创建界面
    root = tk.Tk()
    root.title("照片批量下载")
    root.geometry("400x450")
    root.resizable(width=False, height=False)

    la1 = ttk.Label(root, text="请输入照片名", font=("微软雅黑", 10))
    la1.pack()

    en1 = ttk.Entry(root, font=("微软雅黑", 20))
    en1.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    bth2 = ttk.Button(root, text="清空", command=bth2)
    bth2.pack(pady=10)

    la3 = tk.Label(root, text="有些照片可能无法打开！", font=("微软雅黑", 15), fg="red")
    la3.pack()

    root.mainloop()

def fn119():

    def download_file(url, path):
        try:
            resp = requests.get(url, stream=True)
            con = int(resp.headers.get("content-length")) / 1024
            with open(path, "wb") as f:
                for data in tqdm(iterable=resp.iter_content(1024), total=con, unit="K", desc="下载中"):
                    f.write(data)
            return True
        except Exception as e:
            messagebox.showerror("错误", f"下载失败，原因：{e}")
            return False

    def bth1():
        try:
            verset = en2.get()
            url = f"https://www.python.org/ftp/python/{verset}/python-{verset}.exe"
            messagebox.showinfo("提示", "找到保存的位置")
            path = filedialog.askdirectory()
            ti = int(time.time())
            path2 = f"{path}\\{ti}_python.exe"
            path3 = f"{path}\\{ti}_pycharm.exe"

            if download_file(url, path2):
                messagebox.showinfo("提示", "python安装包下载成功！")
                messagebox.showinfo("提示", "接下来下载编译器安装包。")

                url2 = "https://download.jetbrains.com/python/pycharm-community-2024.1.2.exe?_gl=1*1i8t8t4*_ga*MTk4NTM3ODMzMC4xNzA2OTQwODc4*_ga_9J976DJZ68*MTcxNzkwNTY4Ny4xNS4xLjE3MTc5MDc1NjQuMC4wLjA.&_ga=2.94781471.2042606514.1717905687-1985378330.1706940878"
                if download_file(url2, path3):
                    messagebox.showinfo("提示", "编译器安装包下载成功！")
                    messagebox.showinfo("提示", "所有文件下载完成！")
        except Exception as e:
            messagebox.showerror("错误", f"下载失败！原因：{e}")

    def bth2():
        try:
            url = "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=249851_43d62d619be4e416215729597d70b8ac"
            messagebox.showinfo("提示", "找到保存的位置")
            path = filedialog.askdirectory()
            ti = int(time.time())
            path2 = f"{path}\\{ti}_java.exe"
            path3 = f"{path}\\{ti}_idea.exe"

            if download_file(url, path2):
                messagebox.showinfo("提示", "java安装下载完成！")
                messagebox.showinfo("提示", "接下来下载编译器安装包。")

                url2 = "https://download.jetbrains.com/idea/ideaIC-2024.1.4-aarch64.exe?_gl=1*scpizs*_gcl_au*ODEwNTY1MzE5LjE3MTg5NzM1MDU.*_ga*MTk4NTM3ODMzMC4xNzA2OTQwODc4*_ga_9J976DJZ68*MTcxOTMyMzcxMS4yMS4xLjE3MTkzMjM3MzAuNDEuMC4w&_ga=2.65444078.1936443986.1719323711-1985378330.1706940878"
                if download_file(url2, path3):
                    messagebox.showinfo("提示", "编译器安装包下载成功！")
                    messagebox.showinfo("提示", "所有文件下载完成！")

        except Exception as e:
            messagebox.showerror("错误", f"下载失败，原因：{e}")

    def bth3():
        try:
            url = "https://zenlayer.dl.sourceforge.net/project/orwelldevcpp/Setup%20Releases/Dev-Cpp%205.11%20TDM-GCC%204.9.2%20Setup.exe?viasf=1"
            messagebox.showinfo("提示", "找到保存的位置")
            path = filedialog.askdirectory()
            ti = int(time.time())
            path2 = f"{path}\\{ti}_devcpp.exe"

            if download_file(url, path2):
                messagebox.showinfo("提示", "编译器安装包下载成功！")
                messagebox.showinfo("提示", "所有文件下载完成！")

        except Exception as e:
            messagebox.showerror("错误", f"下载失败，原因：{e}")

    def bth4():
        en2.delete(0, tk.END)

    root = tk.Tk()
    root.title("编程环境配置")
    root.geometry("400x450")
    root.resizable(width=False, height=False)

    la2 = ttk.Label(root, text="如果选择python，则需要输入python要下载的版本", font=("微软雅黑", 10))
    la2.pack()

    en2 = ttk.Entry(root, font=("微软雅黑", 15))
    en2.pack()

    bth1 = ttk.Button(root, text="python下载", command=bth1)
    bth1.pack(pady=5)

    bth2 = ttk.Button(root, text="java下载", command=bth2)
    bth2.pack(pady=5)

    bth3 = ttk.Button(root, text="c++下载", command=bth3)
    bth3.pack(pady=5)

    bth4 = ttk.Button(root, text="清空", command=bth4)
    bth4.pack(pady=10)

    root.mainloop()


def fn120():
    # 按钮功能
    def bth1():
        a = en1.get()
        url1 = f"https://jx.xmflv.com/?url={a}"
        webbrowser.open(url1)

    def bth2():
        en1.delete(0, tk.END)

    # 创建界面
    root = tk.Tk()
    root.title("vip破解")
    root.geometry("300x155")
    root.resizable(width=False, height=False)

    la1 = ttk.Label(root, text="输入视频链接", font=("微软雅黑", 15))
    la1.pack()

    en1 = ttk.Entry(root, font=("微软雅黑", 18))
    en1.place(x=1, y=50)

    bth1 = ttk.Button(root, text="播放", command=bth1)
    bth1.place(x=180, y=100)

    bth2 = ttk.Button(root, text="清空", command=bth2)
    bth2.place(x=70, y=100)

    root.mainloop()

def fn121():
    def bth1():
        url = f"https://dict.youdao.com/dictvoice?audio={en1.get()}&type={en2.get()}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            "Referer": "https://www.baidu.com"
        }
        resp = requests.get(url, headers=headers)
        messagebox.showinfo("提示", "找到保存的位置")
        path1 = filedialog.askdirectory()
        ti = int(time.time())
        path2 = f"{path1}\\{ti}.mp3"

        with open(path2, "wb") as f:
            f.write(resp.content)

        url2 = f"https://dict.youdao.com/result?word={en1.get()}&lang=en"
        resp2 = requests.get(url2, headers=headers)
        text = resp2.text

        etree_text = etree.HTML(text)
        r_list = etree_text.xpath('//*[@id="catalogue_author"]/div[2]/div/div[1]/ul/li[1]/span[2]/text()')
        sor.delete(1.0, tk.END)
        sor.insert(tk.END, r_list)

        def play_audio_with_pygame(path3):
            # 播放单词发音
            pygame.mixer.init()

            pygame.mixer.music.load(path3)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        path4 = f"{path1}\\{ti}.mp3"
        play_audio_with_pygame(path4)

    def bth2():
        en1.delete(0, tk.END)
        en2.delete(0, tk.END)
        sor.delete(1.0, tk.END)

    root = tk.Tk()
    root.title("英文单词发音")
    root.geometry("600x700")
    root.resizable(width=False, height=False)

    la1 = ttk.Label(root, text="输入单词", font=("微软雅黑", 15))
    la1.pack()

    en1 = ttk.Entry(root, font=("微软雅黑", 20))
    en1.pack()

    la2 = ttk.Label(root, text="输入发音，1为英式发音，2为美式发音", font=("微软雅黑", 15))
    la2.pack()

    en2 = ttk.Entry(root, font=("微软雅黑", 20))
    en2.pack()

    la4 = ttk.Label(root, text="中文显示", font=("微软雅黑", 15))
    la4.pack()

    sor = scrolledtext.ScrolledText(root, font=("微软雅黑", 10), height=10)
    sor.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    bth2 = ttk.Button(root, text="清空", command=bth2)
    bth2.pack(pady=10)

    root.mainloop()


def fn122():
    def bth1():
        def download_file(url1, path3):
            resp = requests.get(url1, headers=headers, stream=True)
            con = int(resp.headers.get("content-length")) / 1024
            with open(path3, "wb") as f:
                for data in tqdm(iterable=resp.iter_content(1024), total=con, unit="K", desc="下载中"):
                    f.write(data)

        url = en1.get()
        messagebox.showinfo("提示", "找到保存的位置")
        path = filedialog.askdirectory()
        ti = int(time.time())
        path2 = f"{path}\\{ti}.{en2.get()}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            "Referer": "https://www.baidu.com"
        }

        # 启用多线程
        download_thread = threading.Thread(target=download_file, args=(url, path2))
        download_thread.start()

        download_thread.join()

    def bth2():
        en1.delete(0, tk.END)
        en2.delete(0, tk.END)

    root = tk.Tk()
    root.title("文件下载")
    root.geometry("400x450")
    root.resizable(width=False, height=False)

    la1 = ttk.Label(root, text="输入文件链接", font=("微软雅黑", 15))
    la1.pack()

    en1 = ttk.Entry(root, font=("微软雅黑", 20))
    en1.pack()

    la2 = ttk.Label(root, text="输入文件后缀名", font=("微软雅黑", 15))
    la2.pack()

    en2 = ttk.Entry(root, font=("微软雅黑", 20))
    en2.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    bth2 = ttk.Button(root, text="清空", command=bth2)
    bth2.pack(pady=10)

    root.mainloop()


def fn123():
    def bth1():
        # 对目标链接查找照片链接
        url = f"https://unsplash.com/s/photos/{en1.get()}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            "Referer": "https://www.baidu.com"
        }
        messagebox.showinfo("提示", "找到保存的位置")
        path = filedialog.askdirectory()
        ti = int(time.time())
        resp = requests.get(url, headers=headers)
        text = resp.text
        url2 = []

        soup = BeautifulSoup(text, "html.parser")
        img_tags = soup.find_all("img")

        for img_tag in img_tags[22:160]:
            src = img_tag.get("src")
            if src not in url2:
                url2.append(src)  # 将找到的链接存入列表中

        for a, url3 in enumerate(url2):
            try:
                if url3.startswith('data:image'):
                    continue  # 跳过gif图片
                else:
                    # 批量下载图片
                    resp2 = requests.get(url3, headers=headers)
                    if resp2.status_code == 200:
                        path2 = os.path.join(path, f"{ti}_{a + 1}.png")
                        with open(path2, "wb") as f:
                            f.write(resp2.content)
                    else:
                        continue
            except Exception:
                messagebox.showerror("错误", "下载失败！")

    def bth2():
        en1.delete(0, tk.END)

    root = tk.Tk()
    root.title("高清图片下载")
    root.geometry("400x450")
    root.resizable(width=False, height=False)

    la1 = ttk.Label(root, text="输入照片名称", font=("微软雅黑", 15))
    la1.pack()

    en1 = ttk.Entry(root, font=("微软雅黑", 20))
    en1.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    bth2 = ttk.Button(root, text="清空", command=bth2)
    bth2.pack(pady=10)

    root.mainloop()


def fn124():
    def bth1():
        # 读取输入框内容
        messagebox.showinfo("提示", "找到音频的位置")
        path1 = filedialog.askopenfilename()
        time_interval = int(en2.get())

        # 切割音频
        def split_audio(input_file, output_folder, segment_length_sec):
            y, sr = librosa.load(input_file, sr=None)
            segment_length_samples = int(segment_length_sec * sr)

            for i, start_sample in enumerate(range(0, len(y), segment_length_samples)):
                segment = y[start_sample: start_sample + segment_length_samples]
                output_file = os.path.join(output_folder, f"{i}.wav")
                sf.write(output_file, segment, sr)

        # 输出分割后的音频文件
        messagebox.showinfo("提示", "找到分割后音频存放的位置")
        output_folder = filedialog.askdirectory()
        split_audio(path1, output_folder, time_interval)

    def bth2():
        # 清空输入框内容
        en2.delete(0, tk.END)
    root = tk.Tk()
    root.title("音频切片")
    root.geometry("400x450")
    root.resizable(width=False, height=False)

    la2 = ttk.Label(root, text="输入切片时间(秒)", font=("微软雅黑", 15))
    la2.pack()

    en2 = ttk.Entry(root, font=("微软雅黑", 20))
    en2.pack()

    la3 = ttk.Label(root, text="仅支持wav格式", font=("微软雅黑", 15))
    la3.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    bth2 = ttk.Button(root, text="清空", command=bth2)
    bth2.pack(pady=10)

    root.mainloop()


def fn125():
    def bth1():
        # 读取输入框内容
        text = en1.get()

        engine = pyttsx3.init()

        # 设置发音速度
        engine.setProperty('rate', 150)

        # 设置发音音量
        engine.setProperty('volume', 1.0)

        # 设置发音语调
        engine.setProperty('voice', 'english+f4')

        # 读出文本
        engine.say(text)

        # 等待语音播报完毕
        engine.runAndWait()

    def bth2():
        # 清空输入框内容
        en1.delete(0, tk.END)

    root = tk.Tk()
    root.title("文本转语音")
    root.geometry("400x450")
    root.resizable(width=False, height=False)

    la1 = ttk.Label(root, text="输入文本", font=("微软雅黑", 15))
    la1.pack()

    en1 = ttk.Entry(root, font=("微软雅黑", 20))
    en1.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    bth2 = ttk.Button(root, text="清空", command=bth2)
    bth2.pack(pady=10)

    root.mainloop()


def fn126():
    def bth1():
        # 读取输入框内容
        song_name = en1.get()
        page_num = int(en2.get())
        song_num = int(en3.get())
        messagebox.showinfo("提示", "找到存放的位置")
        save_path = filedialog.askdirectory()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            "Referer": "https://www.baidu.com"
        }

        def get_music_info():
            music_info_list = []

            # 获取音乐链接
            url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p={page_num}&n={song_num}&w={song_name}'
            resp = requests.get(url, headers=headers).text
            music_json = resp[9:-1]  # 去掉前9位和后1位
            music_data = json.loads(music_json)
            music_list = music_data['data']['song']['list']
            for music in music_list:
                name = music["songname"]
                singer = music["singer"][0]["name"]
                songmid = music["songmid"]
                music_info_list.append((name, singer, songmid))
            return music_info_list

        def get_purl(music_info_list):
            music_data = []

            for music in music_info_list:
                name = music[0]
                singer = music[1]
                songmid = music[2]
                url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8846039534","songmid":["%s"],"songtype":[0],"uin":"1152921504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152921504784213523","format":"json","ct":24,"cv":0}}' % songmid
                resp = requests.get(url, headers=headers).json()
                purl = resp['req_0']['data']['midurlinfo'][0]['purl']
                full_media_url = 'http://dl.stream.qqmusic.qq.com/' + purl
                music_data.append({
                    "name": name,
                    "singer": singer,
                    "full_media_url": full_media_url
                })
            return music_data

        def save_music_mp3(music_data):
            for music in music_data:
                name = music["name"]
                singer = music["singer"]
                full_url = music["full_media_url"]

                # 使用多线程下载音乐文件
                try:
                    def download_music(full_url2, save_path3):
                        music_resp = requests.get(full_url2, headers=headers, stream=True)
                        con = int(music_resp.headers.get("content-length")) / 1024

                        with open(save_path3, "wb") as f:
                            for data in tqdm(iterable=music_resp.iter_content(1024), total=con, unit="K", desc="下载中"):
                                f.write(data)
                        print(f"{name}_{singer}.mp3 下载完成！")

                    if "()" in name or "/" in name or "\\" in name or ":" in name or "*" in name or "?" in name or "\"" in name or "<" in name or ">" in name or "|" in name:
                        name = int(time.time())
                        save_path2 = os.path.join(f"{save_path}\\{name}_{singer}.mp3")
                    else:
                        save_path2 = f"{save_path}\\{name}_{singer}.mp3"

                    # 启用多线程
                    download_thread = threading.Thread(target=download_music, args=(full_url, save_path2))
                    download_thread.start()

                    download_thread.join()
                except Exception:
                    print(f"{name}_{singer}.mp3 下载失败！")

        if __name__ == "__main__":
            # 调用函数
            music_info_list = get_music_info()
            music_data = get_purl(music_info_list)
            save_music_mp3(music_data)

    def bth2():
        en1.delete(0, tk.END)
        en2.delete(0, tk.END)
        en3.delete(0, tk.END)

    root = tk.Tk()
    root.title("音乐搜索下载")
    root.geometry("400x450")
    root.resizable(width=False, height=False)

    la1 = ttk.Label(root, text="输入歌名/歌手名", font=("微软雅黑", 15))
    la1.pack()

    en1 = ttk.Entry(root, font=("微软雅黑", 20))
    en1.pack()

    la2 = ttk.Label(root, text="下载的页数", font=("微软雅黑", 15))
    la2.pack()

    en2 = ttk.Entry(root, font=("微软雅黑", 20))
    en2.pack()

    la3 = ttk.Label(root, text="下载的音乐数量", font=("微软雅黑", 15))
    la3.pack()

    en3 = ttk.Entry(root, font=("微软雅黑", 20))
    en3.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    bth2 = ttk.Button(root, text="清空", command=bth2)
    bth2.pack(pady=10)

    root.mainloop()


def fn127():
    def bth1():
        # 读取输入框内容
        messagebox.showinfo("提示", "找到图片的位置")
        pictures_path = filedialog.askopenfilename()
        messagebox.showinfo("提示", "找到存放的位置")
        path = filedialog.askdirectory()
        ti = int(time.time())
        path3 = os.path.join(f"{path}\\{ti}.jpg")

        # 压缩图片
        def comperss_picture(pictures_path2, path2, quality):
            pictures = Image.open(pictures_path2)
            pictures.save(path2, optimize=True, quality=quality)

        # 设置图片质量和参数
        quality = 50
        comperss_picture(pictures_path, path3, quality)

    root = tk.Tk()
    root.title("照片压缩")
    root.geometry("400x450")
    root.resizable(width=False, height=False)

    la3 = ttk.Label(root, text="仅支持jpg/jpeg/png格式", font=("微软雅黑", 15))
    la3.pack()

    bth1 = ttk.Button(root, text="开始", command=bth1)
    bth1.pack(pady=10)

    root.mainloop()

def fn128():
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    import torch.optim as optim
    from torchvision import datasets, transforms
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    from tkinter import messagebox

    # 检查是否有可用的 GPU
    messagebox.showinfo("提示", "程序已在后台运行，请注意查看。")

    # 数据预处理
    transforms = transforms.Compose([transforms.ToTensor()])
    trainset = datasets.MNIST(root="./datasets", train=True, download=True, transform=transforms)
    testset = datasets.MNIST(root="./datasets", train=False, download=True, transform=transforms)

    # 定义训练参数
    batch_size = 64
    steps = int(input("请输入要训练的步数："))
    learning_rate = 0.01

    # 定义神经网络
    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
            self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
            self.conv2_drop = nn.Dropout2d()
            self.fc1 = nn.Linear(320, 50)
            self.fc2 = nn.Linear(50, 10)

        def forward(self, x):
            x = F.relu(F.max_pool2d(self.conv1(x), 2))
            x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
            x = x.view(-1, 320)
            x = F.relu(self.fc1(x))
            x = F.dropout(x, training=self.training)
            x = self.fc2(x)
            return F.log_softmax(x, dim=1)

    # 实例化神经网络并将其移动到设备
    model = Net()

    # 数据加载器
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True)
    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False)

    # 定义损耗函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # 训练模型
    train_losses = []
    for epoch in range(steps):
        for i, (images, labels) in enumerate(trainloader):
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            train_losses.append(loss.item())
            if (i + 1) % 100 == 0:
                print(f"[{epoch + 1}/{steps}] iteration: {i + 1}/{len(trainloader)}, loss: {loss.item()}")

    # 测试模型
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in testloader:
            images, labels = images
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f"网络在10000张图片的准确度：{100 * correct / total}%")

    # 绘制训练损失
    plt.plot(range(len(train_losses)), train_losses)
    plt.xlabel("iteration")
    plt.ylabel("loss")
    plt.show()

    # 推理模型
    def recognize_number(image_path, model):
        image = Image.open(image_path).convert("L")
        image = image.resize((28, 28))
        image = np.array(image)
        image = image.astype(np.float32) / 255.0
        image_tensor = torch.from_numpy(image).unsqueeze(0).unsqueeze(0)
        model.eval()
        with torch.no_grad():
            output = model(image_tensor)
            _, predicted = torch.max(output, 1)
            print(f"识别结果：{predicted.item()}")

    # 使用训练好的模型推理和获取图片
    while True:
        image_path = input("请输入图片的路径：")
        recognize_number(image_path, model)

def fn129():
    def bth1():
        from moviepy.editor import VideoFileClip

        # 开始进行转换操作
        def mp4_to_gif(input_file, output_file, fps=10):
            # 加载视频文件
            video_clip = VideoFileClip(input_file)

            # 将视频转换为GIF
            video_clip.write_gif(output_file, fps=fps)

            # 关闭视频剪辑
            video_clip.close()
            messagebox.showinfo("提示", "转换完成！")

        # 读取输入框内容
        messagebox.showinfo("提示", "找到视频的位置")
        input_mp4 = filedialog.askopenfilename()
        messagebox.showinfo("提示", "找到存放的位置")
        output_gif = filedialog.askdirectory()
        ti = int(time.time())
        output_gif = f"{output_gif}/{ti}.gif"

        mp4_to_gif(input_mp4, output_gif)

    root = tk.Tk()
    root.title("mp4转gif文件")
    root.geometry("400x100")
    root.resizable(width=False, height=False)

    bth1 = ttk.Button(root, text="开始转换", command=bth1)
    bth1.pack(pady=10)

    root.mainloop()

# 创建主窗口
root1 = tk.Tk()
root1.title("工具")
root1.geometry("500x650")
root1.resizable(width=False, height=False)

# 创建按钮
sn111 = tk.Button(root1, text="计算器", width=12, height=5, command=fn111)
sn111.place(x=20, y=5)

sn112 = tk.Button(root1, text="照片下载", width=12, height=5, command=fn112)
sn112.place(x=20, y=125)

sn113 = tk.Button(root1, text="页面源代码提取", width=12, height=5, command=fn113)
sn113.place(x=20, y=245)

sn114 = tk.Button(root1, text="音乐下载", width=12, height=5, command=fn114)
sn114.place(x=140, y=5)

sn115 = tk.Button(root1, text="视频下载", width=12, height=5, command=fn115)
sn115.place(x=140, y=125)

sn116 = tk.Button(root1, text="三个数取最大值", width=12, height=5, command=fn116)
sn116.place(x=140, y=245)

sn117 = tk.Button(root1, text="文本字数计算", width=12, height=5, command=fn117)
sn117.place(x=260, y=5)

sn118 = tk.Button(root1, text="照片批量下载", width=12, height=5, command=fn118)
sn118.place(x=260, y=125)

sn119 = tk.Button(root1, text="编程环境配置", width=12, height=5, command=fn119)
sn119.place(x=260, y=245)

sn120 = tk.Button(root1, text="vip破解", width=12, height=5, command=fn120)
sn120.place(x=380, y=5)

sn121 = tk.Button(root1, text="英文单词发音", width=12, height=5, command=fn121)
sn121.place(x=380, y=125)

sn122 = tk.Button(root1, text="文件下载", width=12, height=5, command=fn122)
sn122.place(x=380, y=245)

sn123 = tk.Button(root1, text="高清图片下载", width=12, height=5, command=fn123)
sn123.place(x=20, y=365)

sn124 = tk.Button(root1, text="音频切片", width=12, height=5, command=fn124)
sn124.place(x=140, y=365)

sn125 = tk.Button(root1, text="文本转语音", width=12, height=5, command=fn125)
sn125.place(x=260, y=365)

sn126 = tk.Button(root1, text="音乐搜索下载", width=12, height=5, command=fn126)
sn126.place(x=380, y=365)

sn127 = tk.Button(root1, text="照片压缩", width=12, height=5, command=fn127)
sn127.place(x=20, y=485)

sn128 = tk.Button(root1, text="数字识别", width=12, height=5, command=fn128)
sn128.place(x=140, y=485)

sn129 = tk.Button(root1, text="mp4转gif文件", width=12, height=5, command=fn129)
sn129.place(x=260, y=485)

root1.mainloop()
