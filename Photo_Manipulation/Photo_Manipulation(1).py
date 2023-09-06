#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:40:38 2023
@author: sarthakgupta
"""

import os 
import sys
from PIL import Image, ImageFilter, ImageEnhance, ImageColor

# Display a user-friendly menu
print("Welcome to Photo Manipulation Studio\n\n"
      "Press 1 for Resizing an Image\n"
      "Press 2 to Convert between JPG and PNG\n"
      "Press 3 for Image Information\n"
      "Press 4 to List Images in the Current Folder\n"
      "Press 5 to Create a Blank Image\n"
      "Press 6 to Rotate an Image\n"
      "Press 7 to Flip an Image\n"
      "Press 8 to Increase the Size of an Image\n"
      "Press 9 to Enhance an Image\n"
      "Press 10 to Apply Filters\n"
      "Press 11 to Apply a Rank Filter\n"
      "Press 12 to Combine Filters")

# Get the user's choice
Task = int(input("Enter the input: "))

# Process user's choice
try:
    if Task == 1:
        # Resize the image
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        print("Pixels A*B")
        s = int(input("Enter A: "))
        a = int(input("Enter B: "))
        size = (s, a)
        img = image.resize(size)
        img.save("resized.jpg")
        print("Image successfully resized.")

    elif Task == 2:
        # Convert image format between JPG and PNG
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        if Img.endswith('.jpg'):
            image.save("Converted.png")
            print("Image successfully converted.")
        elif Img.endswith('.png'):
            image.save("Converted.jpg")
            print("Image successfully converted.")
        else:
            print("Unsupported file format. Please provide a JPG or PNG file.")

    elif Task == 3:
        # Display image information
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        print("File Name:", image.filename)
        print("Image Size:", image.size)
        print("File Format:", image.format)
        print("Format Description:", image.format_description)

    elif Task == 4:
        # List image files in the current folder
        i = 0
        j = 0
        for f in os.listdir():
            if f.endswith(".jpg"):
                i += 1
                print(f)
                print("Number of JPG files: " + str(i))
            elif f.endswith(".png"):
                j += 1
                print(f)
                print("Number of PNG files: " + str(j))

    elif Task == 5:
        # Create a blank image
        print("Pixels A*B")
        s = int(input("Enter A: "))
        a = int(input("Enter B: "))
        img = Image.new('RGBA', (s, a))
        img.save("Blank.png")
        print("Blank image successfully created.")

    elif Task == 6:
        # Rotate an image
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        a = float(input("Enter degrees to rotate: "))
        c = input("Enter background color: ")
        Expand = input("Do you want to expand [y]/[n]: ")
        if Expand == 'y':
            v = True
        elif Expand == 'n':
            v = False
        img = image.rotate(a, expand=v, fillcolor=ImageColor.getcolor(c, 'RGB'))
        img.save("Rotated.jpg")
        print("Image successfully rotated.")

    elif Task == 7:
        # Flip an image
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        print("Press 1 for Left to Right flip")
        print("Press 2 for Top to Bottom flip")
        print("Press 3 for Transpose")
        print("Press 4 for Transverse")
        print("Press 5 for Rotate 90 degrees")
        
        Task = int(input("Enter input:"))
        
        if Task == 1:
            imag = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            imag.save("Flip.jpg")
        elif Task == 2:
            imag = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            imag.save("Flip.jpg")
        elif Task == 3:
            imag = image.transpose(Image.Transpose.TRANSPOSE)   
            imag.save("Flip.jpg")
        elif Task == 4:
            imag = image.transpose(Image.Transpose.TRANSVERSE)
            imag.save("Flip.jpg")
        elif Task == 5:
            imag = image.transpose(Image.Transpose.ROTATE_90)
            imag.save("Flip.jpg")
        print("Image successfully flipped.")

    elif Task == 8:
        # Increase the size of an image
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        sf = int(input("Enter Scale Factor:"))
        new = (image.size[0] * sf, image.size[1] * sf)
        img = image.resize(new)
        img.save("Resized.jpg")
        print("Image successfully resized.")

    elif Task == 9:
        # Enhance the image
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        print("Press 1 for Grayscale")
        print("Press 2 for Brightness")
        print("Press 3 for Contrast")
        print("Press 4 for Color")
        print("Press 5 for Sharpness")
        
        Task = int(input("Enter input:"))
        
        if Task == 1:
            imag = image.convert('L')
            imag.save("Enhanced.jpg")
            print("Image successfully enhanced.")
        elif Task == 2:
            enhancer = ImageEnhance.Brightness(image)
            enhanced_img = enhancer.enhance(float(input("Enter Brightness Factor: ")))
            enhanced_img.save("Enhanced.jpg")
            print("Image successfully enhanced.")
        elif Task == 3:
            enhancer = ImageEnhance.Contrast(image)
            enhanced_img = enhancer.enhance(float(input("Enter Contrast Factor: ")))
            enhanced_img.save("Enhanced.jpg")
            print("Image successfully enhanced.")
        elif Task == 4:
            enhancer = ImageEnhance.Color(image)
            enhanced_img = enhancer.enhance(float(input("Enter Color Factor: ")))
            enhanced_img.save("Enhanced.jpg")
            print("Image successfully enhanced.")
        elif Task == 5:
            enhancer = ImageEnhance.Sharpness(image)
            enhanced_img = enhancer.enhance(float(input("Enter Sharpness Factor: ")))
            enhanced_img.save("Enhanced.jpg")
            print("Image successfully enhanced.")

    if Task == 10:
        # Apply various image filters
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        print("Press 1 for Blur")
        print("Press 2 for Contour")
        print("Press 3 for Detail")
        print("Press 4 for Edge Enhance")
        print("Press 5 for More Edge Enhance")
        print("Press 6 for Find Edges")
        print("Press 7 for Emboss")
        print("Press 8 for Sharpen")
        print("Press 9 for Smooth")
        
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
        print("Image successfully enhanced.")

    if Task == 11:
        # Apply rank filters to the image
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        print("Press 1 for Min Filter")
        print("Press 2 for Median Filter")
        print("Press 3 for Max Filter")
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
        print("Image successfully filtered.")

    if Task == 12:
        # Combine filters to the image
        Img = input("Enter the name of the file (case-sensitive): ")
        image = Image.open(Img)
        print("Press 1 for Emboss & Blur")
        print("Press 2 for Contour & Blur")
        Task = int(input("Enter number:"))
        if Task == 1:
            image_emboss = image.filter(ImageFilter.EMBOSS)
            image_embos_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius=3))
            image_embos_blur.save('99.jpg')
        elif Task == 2:
            image_emboss = image.filter(ImageFilter.CONTOUR())
            image_embos_blur = image_emboss.filter(ImageFilter.BLUR(radius=3))
            image_embos_blur.save('99.jpg')
        print("Image successfully processed.")
except Exception as e:
    print("An error occurred:", str(e))
