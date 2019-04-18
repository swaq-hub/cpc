from django.shortcuts import render
from django.contrib import auth
from django.template import Template, Context
from model import Main, color
import os
import cv2





def home(request):
    #commingsoon
    

    return render(request,"index.html")


    #######################################################################
def testcar(request):
    #This is user authentication section
    #Authenticate or Validate users login data
	# license_no = request.POST.get("license_no")
	# car_color = request.POST.get("car_color")
	# car_image = request.POST.get("car_image") #To-DO get car_image

	# try:
	# check_plate = Main.main(car_image) #TO-DO pass car_image to check for plate
	# except Exception as e:
	# 	print("Image Not Found_ " + str(e))
	

	
	

    

	return render(request,"result.html")
    #-----------------------------


