#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:40:38 2023

@author: sarthakgupta
"""

import os 
import sys
from PIL import Image, ImageFilter, ImageEnhance, ImageColor


print("Welcome to Photo manipulation Studio\n\n"
      "Press 1 for Resizing of the Image\n"
      "Press 2 for jpg to png or png to jpg\n"
      "Press 3 for Image Information\n"
      "Press 4 for to Get all image from the folder with same extension\n"
      "Press 5 to Create a blank image\n"
      "Press 6 to Rotate an image\n"
      "Press 7 to Flip an Image\n"
      "Press 8 to Increse the size of Image\n"
      "Press 9 to Enhance the Image\n"
      "Press 10 to Apply Filters\n"
      "Press 11 to Apply rank Filter"
      "Press 12 to Combine Filters")

Task=int(input("Enter the input: "))

if Task==1:
    Img= input("Enter the name of file with same case: ")
    image=Image.open(Img)
    print("Pixels A*B")
    s=int(input("Enter A: "))
    a=int(input("Enter B: "))
    size=(s,a)
    img=image.resize(size)
    img.save("resized.jpg")
    print("Successfull")

elif Task==2:
    Img= input("Enter the name of file with same case: ")
    image=Image.open(Img)
    if Img.endswith('.jpg'):
        image.save("Converted.png")
        print("Successfull")
    if Img.endswith('.png'):
        image.save("Converted.jpg")
        print("Successfull")
        
elif Task==3:
    Img= input("Enter the name of file with same case: ")
    image=Image.open(Img)
    print(image.filename)
    print(image.size)
    print(image.format)
    print(image.format_description)
    
elif Task == 4:
    i=0
    j=0
    for f in os.listdir():
        if f.endswith(".jpg"):
            i += 1
            print(f)
            print("Number of jpg files: " + str(i))
            
        elif f.endswith(".png"):
            j += 1
            print(f)
            print("Number of png files: " + str(j))
            
elif Task == 5:
    print("Pixels A*B")
    s = int(input("Enter A: "))
    a = int(input("Enter B: "))
    img = Image.new('RGBA', (s, a))
    img.save("Blank.png")
    print("Successful")

elif Task== 6:
    Img= input("Enter the name of file with same case: ")
    image=Image.open(Img)
    a=float(input("enter degrees to rotate:"))
    c=input("enter background color: ")
    Expand=input("do you want to expand[y]/[n]: ")
    if Expand == 'y':
        v=True
    elif Expand == 'n':
        v=False
    img= image.rotate(a, expand = v, fillcolor = ImageColor.getcolor(c, 'RGB') )
    img.save("Rotated.jpg")
    print("Succesful")

elif Task == 7:
    Img= input("Enter the name of file with same case: ")
    image=Image.open(Img)
    print("Press 1 for L to R flip")
    print("Press 2 for T to B flip")
    print("Press 3 for transpose")
    print("Press 4 for transverse")
    print("Press 5 for rotate 90")
    
    Task=int(input("Enter input:"))
    
    if Task==1:
        imag=image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        imag.save("Flip.jpg")
    if Task==2:
        imag=image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        imag.save("Flip.jpg")
    if Task==3:
        imag=image.transpose(Image.Transpose.TRANSPOSE)   
        imag.save("Flip.jpg")
    if Task==4:
        imag=image.transpose(Image.Transpose.TRANSVERSE)
        imag.save("Flip.jpg")
    if Task==5:
        imag=image.transpose(Image.Transpose.ROTATE_90)
        imag.save("Flip.jpg")
    print("succesful")

elif Task==8:
    Img= input("Enter the name of file with same case: ")
    image=Image.open(Img)
    sf=int(input("enter Scale Factor:"))
    new = (image.size[0]*sf , image.size[1]*sf)
    img=image.resize(new)
    img.save("Resized.jpg")
    print("Successful")
    
elif Task==9:
    Img= input("Enter the name of file with same case: ")
    image=Image.open(Img)
    print("Press 1 for Grayscale")
    print("Press 2 for Brightness")
    print("Press 3 for contrast")
    print("Press 4 for color")
    print("Press 5 for sharpness")
    
    Task=int(input("Enter input:"))
    
    if Task==1:
        imag=image.convert('L')
        imag.save("Enhanced.jpg")
    if Task==2:
        imag=ImageEnhance.Brightness(image)
        imag.save("Enhanced.jpg")
    if Task==3:
        imag=ImageEnhance.Contrast(image)
        imag.save("Enhanced.jpg")
    if Task==4:
        imag=ImageEnhance.Color(image)
        imag.save("Enhanced.jpg")
    if Task==5:
        imag=ImageEnhance.Sharpness(image)
        imag.save("Enhanced.jpg")
    print("succesful")

if Task == 10:
    Img = input("Enter the name of the file with the same case: ")
    image = Image.open(Img)

    print("Press 1 for Blur")
    print("Press 2 for Contour")
    print("Press 3 for Detail")
    print("Press 4 for Edge_enhance")
    print("Press 5 for Edge_enhance_more")
    print("Press 6 for Find edges")
    print("Press 7 for emboss")
    print("Press 8 for sharpen")
    print("Press 9 for smooth")
    
    Task = int(input("Enter input:"))
    
    if Task == 1:
        image = image.filter(ImageFilter.BLUR)
    elif Task == 2:
        image = image.filter(ImageFilter.CONTOUR)
    elif Task == 3:
        image = image.filter(ImageFilter.DETAIL)
    elif Task == 4:
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif Task == 5:
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif Task == 6:
        image = image.filter(ImageFilter.FIND_EDGES)
    elif Task == 7:
        image = image.filter(ImageFilter.EMBOSS)
    elif Task == 8:
        image = image.filter(ImageFilter.SHARPEN)
    elif Task == 9:
        image = image.filter(ImageFilter.SMOOTH)

    image.save("Enhanced.jpg")
    print("Successful")

if Task == 11:
    Img = input("Enter the name of the file with the same case: ")
    image = Image.open(Img)
    print("Press 1 for Min")
    print("Press 2 for Median")
    print("Press 3 for Median")
    Task = int(input("Enter input:"))
    if Task == 1:
        imag = image.filter(ImageFilter.MinFilter(size=5))
        imag.save("Rank.jpg")
    elif Task == 2:
        imag = image.filter(ImageFilter.MedianFilter(size=5))   
        imag.save("Rank.jpg")
    elif Task == 3:
        imag = image.filter(ImageFilter.MaxFilter(size=5))  
        imag.save("Rank.jpg")
    print("successful")

if Task == 12:
    Img = input("Enter the name of the file with the same case: ")
    image = Image.open(Img)
    print("Press 1 for Emboss & Blur")
    print("Press 2 for Contour & Blur")
    Task==int(input("Enter number:"))
    if Task==1:
        image_emboss = image.filter(ImageFilter.EMBOSS)
        image_embos_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius = 3))
        image_embos_blur.save('99.jpg')
    if Task==2:
         image_emboss = image.filter(ImageFilter.CONTOUR())
         image_embos_blur = image_emboss.filter(ImageFilter.BLUR(radius = 3))
         image_embos_blur.save('99.jpg')
    print("successful")
