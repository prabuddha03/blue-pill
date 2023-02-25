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
from PIL import ImageTk, Image  
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
        
        btn=IntVar()
        
        pickup_loc=StringVar()
        drop_loc=StringVar()
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
            
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Pincode.set("")
            Mobile.set("")
            
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            

            btn.set(0)
            pickup_loc.set("")
            drop_loc.set("")
            
            self.txtKm.configure(state=DISABLED)
            self.reset_counter=1
            
            
        def Receiptt():
            if reset_counter == 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Pincode.get()!="" and Mobile.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)
                
                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Ambulance No:\n')
                self.txtReceipt2.insert(END, 'WB ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Postal Code:\n')
                self.txtReceipt2.insert(END, Pincode.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'From:\n')
                self.txtReceipt2.insert(END, pickup_loc.get() + "\n")
                self.txtReceipt1.insert(END,'To:\n')
                self.txtReceipt2.insert(END, drop_loc.get() + "\n")
                self.txtReceipt1.insert(END,"Distance:\n")
                self.txtReceipt2.insert(END, str(Km.get()) + " KM \n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
            
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                
        
        def Kilo():
            geocoder=Nominatim(user_agent="Blue-Pill")
            location1=pickup_loc.get()
            location2=drop_loc.get()

            coordinates1=geocoder.geocode(location1)
            coordinates2=geocoder.geocode(location2)
            lat1,lon1=(coordinates1.latitude),(coordinates1.longitude)
            lat2,lon2=(coordinates2.latitude),(coordinates2.longitude)


            r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon1},{lat1};{lon2},{lat2}?overview=false""")
            routes = json.loads(r.content)
            route_1 = routes.get('routes')[0]
            distance = (route_1['distance'])/1000
            Km.set(("%.3f" % distance))
            
        
        def Total_Paid():
                Item2=Km.get()
                Cost_of_fare = (float(Item2)*50)
                TT = "Rs " + str('%.2f'%(Cost_of_fare))

                TotalCost.set(TT)
                
        
        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = tkb.Frame(MainFrame,bootstyle='light', width=1350,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.Title=tkb.Label(Tops,bootstyle='inverse-light',font=('arial',50,'bold',),text="Ambulance Booking System", justify='center')
        self.Title.grid()
        
        
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=500,bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=400,bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)
        
        CustomerName=LabelFrame(FrameDetails, width=150,height=250,bd=10, font=('arial',12,'bold'),text="Patient Info", relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=10, width=300,height=250, font=('arial',12,'bold'),text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0,column=1)
        
        Book_Frame=LabelFrame(FrameDetails,width=400,height=400,relief=FLAT)
        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,width=150,height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)
        
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10, width=450,height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=550,height=300, font=('arial',12,'bold'),text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=450,height=200, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)
        
        #Patient Info
        self.Firstname=tkb.Label(CustomerName,bootstyle='primary',font=('arial',14,'bold'),text="Firstname")
        self.Firstname.grid(row=0,column=0,sticky=W, padx=20,pady=20)
        self.txtFirstname=tkb.Entry(CustomerName,bootstyle='primary',font=('arial',14,'bold'),textvariable=Firstname,justify=LEFT)
        self.txtFirstname.grid(row=0,column=1)
        
        self.Surname=tkb.Label(CustomerName,bootstyle='primary',font=('arial',14,'bold'),text="Surname")
        self.Surname.grid(row=1,column=0,sticky=W, padx=20,pady=20)
        self.txtSurname=tkb.Entry(CustomerName,bootstyle='primary',font=('arial',14,'bold'),textvariable=Surname,justify=LEFT)
        self.txtSurname.grid(row=1,column=1,sticky=W)
        
        self.Address=tkb.Label(CustomerName,bootstyle='primary',font=('arial',14,'bold'),text="Address")
        self.Address.grid(row=2,column=0,sticky=W, padx=20,pady=20)
        self.txtAddress=tkb.Entry(CustomerName,bootstyle='primary',font=('arial',11,'bold'),width=27,textvariable=Address,justify=LEFT)
        self.txtAddress.grid(row=2,column=1)
        
        self.Pincode=tkb.Label(CustomerName,bootstyle='primary',font=('arial',14,'bold'),text="Pincode")
        self.Pincode.grid(row=3,column=0,sticky=W, padx=20,pady=20)
        self.txtPincode=tkb.Entry(CustomerName,bootstyle='primary',font=('arial',14,'bold'),textvariable=Pincode,justify=LEFT)
        self.txtPincode.grid(row=3,column=1)
        
        self.Mobile=tkb.Label(CustomerName,bootstyle='primary',font=('arial',14,'bold'),text="Mobile")
        self.Mobile.grid(row=5,column=0,sticky=W, padx=20,pady=20)
        self.txtMobile=tkb.Entry(CustomerName,bootstyle='primary',font=('arial',14,'bold'),textvariable=Mobile,justify=LEFT)
        self.txtMobile.grid(row=5,column=1)
        
        
        #Booking Info
        self.Pickup=tkb.Label(TravelFrame,bootstyle='primary',font=('arial',14,'bold'),text="Pickup")
        self.Pickup.grid(row=0,column=0,sticky=W, padx=20,pady=20)
        self.ambPickup=tkb.Entry(TravelFrame,bootstyle='primary',font=('arial',14,'bold'),textvariable=pickup_loc,justify=LEFT)
        self.ambPickup.grid(row=0,column=1)
        
        self.Drop=tkb.Label(TravelFrame,bootstyle='primary',font=('arial',14,'bold'),text="Drop")
        self.Drop.grid(row=1,column=0,sticky=W, padx=20,pady=20)
        self.ambDrop=tkb.Entry(TravelFrame,bootstyle='primary',font=('arial',14,'bold'),textvariable=drop_loc,justify=LEFT)
        self.ambDrop.grid(row=1,column=1)
        
        
        #Distance between pickup point and hospital
        self.chkKm=tkb.Checkbutton(TravelFrame,bootstyle='primary-round-toggle',text="Distance(KMs) *",variable = btn, onvalue=1, offvalue=0,command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm=tkb.Label(TravelFrame,bootstyle='primary',font=('arial',14,'bold'),textvariable=Km,width=18,state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtKm.grid(row=4,column=1, padx=20,pady=20)
        
        
        
        #Costings
        self.TotalCost=tkb.Label(CostFrame,bootstyle='primary',font=('arial',14,'bold'),text="Total Cost: ")
        self.TotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost=Label(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7, width=10, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=3)
        
        #Receipt
        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 30, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)

        #Buttons
        self.btnTotal = tkb.Button(ButtonFrame,bootstyle='primary-outline',width = 7,text='Total', command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = tkb.Button(ButtonFrame,bootstyle='primary-outline',width = 7,text='Receipt',command=Receiptt).grid(row=0,column=1)
        self.btnReset = tkb.Button(ButtonFrame,bootstyle='primary-outline',width = 7,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit = tkb.Button(ButtonFrame,bootstyle='primary-outline',width = 7,text='Exit', command=iExit).grid(row=0,column=3)
        
        #blue-pill logo on the side
        image1 = Image.open("logo.png")
        image1 = image1.resize((320, 320))
        logo = ImageTk.PhotoImage(image1)
        label1 = Label(image=logo)
        label1.image=logo
        label1.place(x=50,y=450)
                              
        
if __name__=='__main__':
    
    root = tkb.Window(themename='cyborg')
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry="%dx%d+%d+%d"%(w,h,0,0)
    
    
    application = travel(root)
    root.mainloop()