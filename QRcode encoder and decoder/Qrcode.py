#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:47:12 2023

@author: sarthakgupta
"""

import qrcode
import cv2

print("Enter 1 to encode qrcode")
print("Enter 2 to decode qrcode")

a=int(input("Enter:"))
if a==1:
    link=input("Enter A Valid URL OR DATA: ")
    print("do you want to customise your qr code, if yes press 1 else enter anything")
    b=int(input("enter input: "))
    if b==1:
        bc=input("enter the back colour: ").lower()
        fc=input("enter the front colour: ").lower()
        qr=qrcode.QRCode()
        qr.add_data(link)
        qr.make()
        img=qr.make_image(fill_color=fc, back_color=bc)
        img.save("Qrcode.png")
    else:
        qr=qrcode.make(link)
        qr.save("Qrcode.png")
elif a==2:
    b=input("enter file name: ")
    img=cv2.imread(b)
    detector=cv2.QRCodeDetector()
    data=detector.detectAndDecode(img)
    print(data[0])
else:
    print("wrong input")
