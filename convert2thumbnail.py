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
        filename = directory.dir + '/*[.jpg|.jpeg|.png]'
        img_list = glob.glob(filename)
        for index, img in enumerate(img_list):
            img.replace('\\','/')
            thumbnail_img_name = des_directory + \
                '/' + str(index) + '_tn.jpg'
            print(img, thumbnail_img_name)
            convert(img, thumbnail_img_name)
        result = tkinter.messagebox.showinfo(title='转换完成', message='转换完成')
        if result:
            top.destroy()
   
def convert(img, name):
    ori_image = Image.open(img)
    out_image = ori_image.resize((640,480), Image.ANTIALIAS)
    out_image.save(name)


top = tkinter.Tk()
top.title('女王专用图片转换工具，比较丑多见谅')
top.geometry('640x480')
source_directory = Directory()
# preview_canvas = tkinter.Canvas(top, bg='white', bd=5, height=300, width=300)
# canvas_img = tkinter.PhotoImage(file='./flower.jpg')
# preview_canvas.create_image(100, 100, image=canvas_img)
# preview_canvas.pack(anchor = 'center')
source_label = tkinter.Label(top)
source_label.pack()
source_button = tkinter.Button(top, text='选择文件夹', command=source_directory.get_dir)
source_button.pack()
convert_button = tkinter.Button(top, text='转换', command=lambda: convert_img(source_directory))
convert_button.pack()
top.mainloop()
