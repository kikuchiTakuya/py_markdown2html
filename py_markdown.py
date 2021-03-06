# 標準ライブラリ
import tkinter as tk
from tkinter import font
import ctypes


# 自作ライブラリ
from original_module import md_maker
from original_module import find_files as ff

# dpi調整
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# 色設定
bg_main = "#414141"
bg_btn = "#252525"
txt_yellow = "#d1d93d"
txt_white = "#788020"
error_txt = "#f57373"
succes_txt = "#73f587"

# 各種ウィジットの関数
def find_md(event):
    path_txt = ff.find_file('*.md')
    output2entry(event, md_entry, path_txt[0])
    
def find_css(event):
    path_txt = ff.find_file('*.css')
    output2entry(event, css_entry, path_txt[0])
    

def output2entry(event,entry, txt):
    entry.configure(state="normal")
    entry.delete(0, tk.END)
    entry.insert(tk.END, txt)
    entry.configure(state="readonly")
    event.widget['relief'] = "flat"

def exe(event):
    md = md_entry.get()
    css = css_entry.get()
    if md == "" and css == "":
        exe_label.configure(fg=error_txt)
        exe_txt.set("You have to read md file and css file.")
        return False
    elif md == "" and css != "":
        exe_label.configure(fg=error_txt)
        exe_txt.set("You have to read md file.")
        return False
    elif md != "" and css == "":
        exe_label.configure(fg=error_txt)
        exe_txt.set("You have to read css file.")
        return False
    else:
        html = md_maker.md_making(md, css)
        output_path = ff.save_file_path()
        with open(output_path, 'w', encoding='utf-8', errors='xmlcharrefreplace') as output_file:
            output_file.write(html)
        exe_label.configure(fg=succes_txt)
        exe_txt.set("[Succes] : " + output_path)
        return True

def hover_in(event):
    event.widget['bg'] = txt_yellow
    event.widget['fg'] = bg_btn

def hover_out(event):
    event.widget['bg'] = bg_btn
    event.widget['fg'] = txt_yellow


# rootメインウィンドウの設定
root = tk.Tk()
root.title("Markdown Maker")
root.geometry("1600x600")
root.configure(bg=bg_main)
# root.tk.call('tk', 'scaling', 1.2)
root.option_add("*font", ["Yu Gothic UI",12])

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=20, pady=50, ipadx=20)
frame.configure(bg="#414141")

# テキスト設定
exe_txt = tk.StringVar()
exe_txt.set("read a markdown file and css file.")

# ウィジットの幅設定
entry_width = 50
btn_width = 20

# 各種ウィジットの作成
md_entry = tk.Entry(
    frame, 
    width = entry_width,
    state = "readonly",
    relief = "flat",
    )

md_read_btn = tk.Button(
    frame, 
    text = "read md file  (Ctrl+1)", 
    width = btn_width,
    bg = bg_btn,
    fg = txt_yellow,
    relief = "flat",
    )

css_entry = tk.Entry(
    frame, 
    width = entry_width,
    state = "readonly",
    relief = "flat",
    )

css_read_btn = tk.Button(
    frame, 
    text = "read css file (Ctrl+2)", 
    width = btn_width, 
    bg = bg_btn,
    fg = txt_yellow,
    relief = "flat",
    )

exe_label = tk.Label(
    frame,
    width = entry_width,
    bg = bg_main,
    fg = "#f4f4f4",
    textvariable = exe_txt
)

exe_btn = tk.Button(
    frame, 
    text = "run      (Ctrl+r)",
    width = btn_width,
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

# ショートカットキーの設定
root.bind_all('<Control-Key-1>', find_md)
root.bind_all('<Control-Key-2>', find_css)
root.bind_all('<Control-Key-r>', exe)


# 各種ウィジットの設置
md_entry.grid(row=0, column=0)
md_read_btn.grid(row=0, column=1, padx=20)
css_entry.grid(row=1, column=0, pady=20)
css_read_btn.grid(row=1, column=1)
exe_label.grid(row=2, column=0)
exe_btn.grid(row=2, column=1)


root.mainloop()
