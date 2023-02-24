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
                        