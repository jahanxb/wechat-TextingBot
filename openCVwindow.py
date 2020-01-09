import numpy as np
from PIL import ImageGrab,Image
import cv2
import time
import nltk
import os
import tempfile
import subprocess
import pytesseract
from ChatterBot import ai_chat
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\Tesseract-OCR\\tesseract.exe'

def screen_record():
    last_time = time.time()
    i=0
    while True:
        # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
        # 40 px accounts for title bar.
        printscreen = np.array(ImageGrab.grab(bbox=(10, 370, 420, 480)))
        print('loop took {} seconds'.format(time.time() - last_time))
        #print(printscreen)
        time.sleep(10)
        last_time = time.time()

        #print(text)
        img = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)

        im_pil = Image.fromarray(img)
        img2= im_pil.getpixel((10,10))
        #img2=cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_RGB2GRAY))
        #print(type(img2))
        #cv2.imread(img,0)

        print(type(im_pil))

        im_pil.save("result.png")
        cv2.imshow('result.png',cv2.COLOR_RGB2GRAY)
        #cv2.imwrite("exp.pil",img2)
        #cv2.imwrite(r'E:\\PycharmProjects\wechat-TextingBot\\',im_pil)
        text = pytesseract.image_to_string('result.png')

        print(str(text))

        if str(text) is '':
            print("Empty String")
            time.sleep(10)
        else:
            ai_chat(text)
            print("message sent!")

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


#nltk.download()
screen_record()
