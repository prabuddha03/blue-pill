from tkinter import *
from tkinter import ttk
import ttkbootstrap as tkb
from ttkbootstrap.constants import *
from tkinter import messagebox as ms
import random
import time
import datetime
import requests
import json
from geopy.geocoders import Nominatim
from geopy import distance


class travel():
    
    def __init__(self,root):
        self.root=root
        self.root.title("Ambulance Booking System")
        self.root.geometry(geometry)
        
        
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        TotalCost=StringVar()
        
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        journeyType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0
        
        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Pincode=StringVar()
        Mobile=StringVar()

        Km=StringVar()
        Receipt=StringVar()
                        
        
        def iExit():
            iExit= ms.askyesno("Prompt!","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return
        
        def Reset():
            Km.set("")