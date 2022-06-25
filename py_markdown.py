# 標準ライブラリ
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tf

# 自作ライブラリ
from original_module import md_maker

# 各種ウィジットの関数
def find_file(tp):
    type = [('', tp)]
    dir = 'C:'
    path = tf.askopenfilenames(filetypes=type, initialdir=dir)
    if not path:
        return
    print(path)
    return path

def find_md(event):
    path_txt = find_file('*.md')
    md_entry.delete(0, tk.END)
    md_entry.insert(tk.END, str(path_txt[0]))

def find_css(event):
    path_txt = find_file('*.css')
    css_entry.delete(0, tk.END)
    css_entry.insert(tk.END, str(path_txt[0]))

def exe(event):
    md_maker.md_making(md_entry.get(), css_entry.get())

# rootメインウィンドウの設定
root = tk.Tk()
root.title("Markdown Maker")
root.geometry("600x400")

# メインフレームの作成と設置
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

# 各種ウィジットの作成
md_entry = ttk.Entry(frame)
md_read_btn = ttk.Button(frame, text="Markdown読込")
md_read_btn.bind("<Button-1>", find_md)

css_entry = ttk.Entry(frame)
css_read_btn = ttk.Button(frame, text="css読込")
css_read_btn.bind("<Button-1>", find_css)

exe_btn = ttk.Button(frame, text="実行")
exe_btn.bind("<Button-1>", exe)

# 各種ウィジットの設置
md_entry.grid(row=0, column=0)
md_read_btn.grid(row=0, column=1)
css_entry.grid(row=1, column=0)
css_read_btn.grid(row=1, column=1)
exe_btn.grid(row=2, column=1)




root.mainloop()
