import tkinter.filedialog as tf

def find_file(tp):
    type = [('', tp)]
    dir = 'C:'
    path = tf.askopenfilenames(filetypes=type, initialdir=dir)
    if not path:
        return
    print(path)
    return path

def save_file_path():
    type = [('', '.html')]
    dir = 'C:'
    path = tf.asksaveasfilename(
        filetypes = type, 
        initialdir = dir,
        defaultextension = "html"
        )
    if not path:
        return
    print(path)
    return path


