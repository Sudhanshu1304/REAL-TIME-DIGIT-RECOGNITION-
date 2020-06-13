# IMPORTING LIBRARIES

from tkinter import *
import pyautogui
from skimage.color import rgb2gray
from skimage.transform import resize, rotate
import numpy as np

import tensorflow as tf
#                                                    SAVED MODEL                                                       #

nm = tf.keras.models.load_model('Hand_Written.h5')

#                                                 TKINTER CLASS                                                       #


class INPUT_WINDOW:


    def __init__(self):

        self.width = 300
        self.height = 320
        self.counti=0

    #                                            MAIN WINDOW                                                           #

    def win(self):
        self.win = Tk()
        self.win.geometry('320x380+20+20')
        self.c = Canvas(self.win, width= 300, height= 300, bg='black')
        self.c.pack(expand=YES, fill=BOTH)
        self.c.bind('<B1-Motion>', self.paint)
        self.b = Button(self.win, bg='gray', text='Clear', fg='black',font=('bold'),
                        command=lambda: self.clear_win())
        self.b.pack(expand=YES, fill=BOTH)
        self.b2 = Button(self.win, bg='gray', text='Run', fg='black',font=('bold'),
                         command=lambda: self.Run())
        self.b2.pack(expand=YES, fill=BOTH)


    def predict(self,data):

        self.win2=Tk()
        self.win2.geometry('350x350+20+500')
        self.c2 = Canvas(self.win2, width=350, height=350, bg='black')
        self.c2.create_text(175, 50, text='PREDICTION ', fill="white", font=('bold', 25))
        self.c2.create_text(150, 180, text=data[1], fill="white", font=('bold', 80))
        self.b3=Button(self.win2,text=str(data[0]*100)[:5]+' '+'%',fg='white',bg='black',font=(7),relief='raised')
        self.c2.create_window(150, 320, window=self.b3)
        self.c2.pack(expand=YES, fill=BOTH)


    def paint(self, cord):
        color = 'white'
        x1, y1 = (cord.x - 1), (cord.y - 1)
        x2, y2 = (cord.x + 1), (cord.y + 1)
        self.c.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=30)


    def clear_win(self):
        if self.counti>=1:
            self.win2.destroy()
        self.win.destroy()
        o2 = INPUT_WINDOW()
        o2.win()


    def Run(self):

        self.counti=self.counti+1
        image = pyautogui.screenshot(region=(12.4 + 16.7 + 5 + 3.5, 66.4, 300 + 16 - 5, 300 + 1))
        image = np.asarray(image)
        image = rgb2gray(image)
        image = resize(image, (20, 20))
        aa = nm.predict(image.reshape([-1, 20, 20, 1], order='F'))
        data=[max(aa[0]), list(aa[0]).index(max(aa[0]))]
        self.predict(data)


o = INPUT_WINDOW()
o.win()
mainloop()