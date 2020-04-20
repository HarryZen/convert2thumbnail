import tkinter
from tkinter import filedialog, StringVar, messagebox
import glob
from PIL import Image
import os


class Directory():
    def __init__(self, dir=''):
        self.__dir__ = dir
    
    @property
    def dir(self):
        return self.__dir__

    def get_dir(self):
        self.__dir__ = filedialog.askdirectory()
        source_label['text'] = self.__dir__

    
def convert_img(directory):
    if directory:
        des_directory = directory.dir + '/thumbnail'
        if not os.path.exists(des_directory):
            os.mkdir(des_directory)
        filename = directory.dir + '/*'
        img_list = glob.glob(filename)[0:-1]
        for img in img_list:
            thumbnail_img_name = des_directory + \
                '/' + img[img.rfind('/')+1: img.rfind('.')] + '_tn.jpg'
            thumbnail_img = convert(img, thumbnail_img_name)
        result = tkinter.messagebox.showinfo(title='转换完成', message='转换完成')
        # if result:
        #     os.system('start explorer'+des_directory) 
   
def convert(img, name):
    ori_image = Image.open(img)
    ori_image.thumbnail((128,128), Image.ANTIALIAS)
    ori_image.save(name)


top = tkinter.Tk()
top.title('女王专用图片转换工具，比较丑多见谅')
top.geometry('640x480')
source_directory = Directory()
preview_canvas = tkinter.Canvas(top, bg='white', bd=5, height=300, width='300')
preview_canvas.pack(anchor = 'center')
source_label = tkinter.Label(top)
source_label.pack()
source_button = tkinter.Button(top, text='选择文件夹', command=source_directory.get_dir)
source_button.pack()
convert_button = tkinter.Button(top, text='转换', command=lambda: convert_img(source_directory))
convert_button.pack()
top.mainloop()
