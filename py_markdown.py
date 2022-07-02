# 標準ライブラリ
import tkinter as tk
from tkinter import font
from turtle import back, bgcolor

# 自作ライブラリ
from original_module import md_maker
from original_module import find_files as ff

# 各種ウィジットの関数
def find_md(event):
    path_txt = ff.find_file('*.md')
    md_entry.configure(state="normal")
    md_entry.delete(0, tk.END)
    md_entry.insert(tk.END, str(path_txt[0]))
    md_entry.configure(state="readonly")

def find_css(event):
    path_txt = ff.find_file('*.css')
    css_entry.configure(state="normal")
    css_entry.delete(0, tk.END)
    css_entry.insert(tk.END, str(path_txt[0]))
    css_entry.configure(state="readonly")

def exe(event):
    md = md_entry.get()
    css = css_entry.get()
    if md == "" and css == "":
        exe_txt.set("You have to read md file and css file.")
        return False
    elif md == "" and css != "":
        exe_txt.set("You have to read md file.")
        return False
    elif md != "" and css == "":
        exe_txt.set("You have to read css file.")
        return False
    else:
        html = md_maker.md_making(md, css)
        output_path = ff.save_file_path()
        # output_path = dic + '/test.html'
        # htmlをhtmlファイルに書き込み
        with open(output_path, 'w', encoding='utf-8', errors='xmlcharrefreplace') as output_file:
            output_file.write(html)
        exe_txt.set("[Succes] : " + output_path)
        return True

def hover_in(event):
    event.widget['bg'] = txt_yellow
    event.widget['fg'] = bg_btn

def hover_out(event):
    event.widget['bg'] = bg_btn
    event.widget['fg'] = txt_yellow

# 色設定
bg_main = "#414141"
bg_btn = "#252525"
txt_yellow = "#d1d93d"
txt_white = "#788020"


# rootメインウィンドウの設定
root = tk.Tk()
root.title("Markdown Maker")
root.geometry("800x400")
root.configure(bg=bg_main)

# ショートカットキーの設定
root.bind_all('<Control-Key-1>', find_md)
root.bind_all('<Control-Key-2>', find_css)
root.bind_all('<Control-Enter>', exe)
root.option_add("*font", ["Yu Gothic UI",12])

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=20, pady=50, ipadx=20)
frame.configure(bg="#414141")

# テキスト設定
exe_txt = tk.StringVar()
exe_txt.set("read a markdown file and css file.")

# 各種ウィジットの作成
md_entry = tk.Entry(
    frame, 
    width = 60,
    state = "readonly",
    relief = "flat",
    )

md_read_btn = tk.Button(
    frame, 
    text = "read md file  (Ctrl+1)", 
    width = 20,
    bg = bg_btn,
    fg = txt_yellow,
    relief = "flat",
    )

css_entry = tk.Entry(
    frame, 
    width = 60,
    state = "readonly",
    relief = "flat",
    )

css_read_btn = tk.Button(
    frame, 
    text = "read css file (Ctrl+2)", 
    width = 20, 
    bg = bg_btn,
    fg = txt_yellow,
    relief = "flat",
    )

exe_label = tk.Label(
    frame,
    width = 60,
    bg = bg_main,
    fg = "#f4f4f4",
    textvariable = exe_txt
)

exe_btn = tk.Button(
    frame, 
    text = "run      (Ctrl+Enter)",
    width = 20,
    bg = bg_btn,
    fg = txt_yellow,
    relief = "flat",
    )

# 各種ウィジットのbind
md_read_btn.bind("<Button-1>", find_md)
md_read_btn.bind("<Enter>", hover_in)
md_read_btn.bind("<Leave>", hover_out)
css_read_btn.bind("<Button-1>", find_css)
css_read_btn.bind("<Enter>", hover_in)
css_read_btn.bind("<Leave>", hover_out)
exe_btn.bind("<Button-1>", exe)
exe_btn.bind("<Enter>", hover_in)
exe_btn.bind("<Leave>", hover_out)


# 各種ウィジットの設置
md_entry.grid(row=0, column=0)
md_read_btn.grid(row=0, column=1, padx=20)
css_entry.grid(row=1, column=0, pady=20)
css_read_btn.grid(row=1, column=1)
exe_label.grid(row=2, column=0)
exe_btn.grid(row=2, column=1)


root.mainloop()
