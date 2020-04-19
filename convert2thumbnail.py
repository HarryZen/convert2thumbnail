import tkinter
from tkinter import filedialog, StringVar
import glob
from PIL import Image

class Directory():
    def __init__(self, dir=''):
        self.__dir__ = dir
    
    @property
    def dir(self):
        return self.__dir__

    def get_dir(self):
        self.__dir__ = filedialog.askdirectory()
        source_label['text'] = self.__dir__

    
def get_img(directory):
    if directory:
        filename = directory.dir + '/*.txt'
        img_list = glob.glob(filename)
        for img in img_list:
            convert(img)
    

def convert(img):
    ori_image = Image.open(img)
    ori_image.thumbnail((128,128), Image.ANTIALIAS)

top = tkinter.Tk()
source_directory = Directory()
source_label = tkinter.Label(top)
source_label.pack()
source_button = tkinter.Button(top, text='选择文件夹', command=source_directory.get_dir)
source_button.pack()
convert_button = tkinter.Button(top, text='转换', command=lambda: get_img(source_directory))
convert_button.pack()
top.mainloop()