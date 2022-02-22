
import random
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk
import csv
from Table_viewer import Get_DET
import os



mainsub={"PSPP":100,"Chem":101,"Maths":102,"Phy":103,"Eng":104,'Phy/Chem Lab':105,'Library':106,'PT':107,'VAC':108,'PSPP Lab':109,'TWM':110,'Club':111}
revmainsub={100:'PSPP',101:"Chem",102:"Maths",103:"Phy",104:"Eng",0:"-",105:'Phy/Chem Lab',106:'Library',107:'PT',108:'VAC',109:'PSPP Lab',110:'TWM',111:'Club'}
day={"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4}
revday={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday"}

maindept={"CSE":1001,"ECE":1002,"EEE":1003,"Civil":1004,"Mech":1005}
revmaindept={1001:'CSE',1002:"ECE",1003:"EEE",1004:"Civil",1005:"Mech"}




#creating login page
def loginpage():
        global img_1,user_entry,pwd_entry,root
        root=Tk()
        root.geometry("1024x700")
        root.config(bg="#8DBEF9")
        root.resizable(width=False,height=False)
        root.title('Zetiplan')
        #root.iconbitmap('semssmall.ico')

        img_1=ImageTk.PhotoImage(Image.open("zetiplan.jpg"))
        img_label1=Label(root,image=img_1)
        img_label1.place(x=0,y=0)

        #welcome label
        myfont0 = font.Font(family='Bodoni MT Black', size=30, weight='bold')
        label2=Label(root,text='''Welcome
To Zetiplan''',padx='180',pady='100',bg="#8DBEF9",)
        label2['font']=myfont0
        label2.place(x=540,y=100)

        #login frame,label and buttons
        loginframe=LabelFrame(root,text='Login',bg='#8DBEF9',height=250,width=500,)
        loginframe['font']=myfont0
        loginframe.place(x=520,y=400)

        myfont1 = font.Font(family='Aerial', size=12, weight='bold')
        user_label=Label(loginframe,text='Admin ID',bg='#8DBEF9')
        pwd_label=Label(loginframe,text='Password',bg='#8DBEF9')
        user_label['font']=myfont1
        pwd_label['font']=myfont1

        user_entry=Entry(loginframe,width=30,relief=SUNKEN,bd=2)
        pwd_entry=Entry(loginframe,width=30,show='*',relief=SUNKEN,bd=2)

        login_button=Button(loginframe,text='Login',bg='#8DBEF9',command=lambda:login(user_entry.get(),pwd_entry.get()))
        login_button['font']=myfont1


        user_label.place(x=75,y=25)
        pwd_label.place(x=75,y=65)
        user_entry.place(x=200,y=25)
        pwd_entry.place(x=200,y=65)
        login_button.place(x=400,y=130)

        root.mainloop()


#login button command
def login(a,b):
        user_entry.delete(0,END)
        pwd_entry.delete(0,END)
        username=a
        pwd=b
        if username=='admin':
                if pwd=='123':
                        root.destroy()
                        mainwindow()
                else:
                        messagebox.showerror("Warning","Incorrect Password")
        else:
                messagebox.showerror("Warning","Incorrect Username")


def logout():
        root1.destroy()
        loginpage()

def mainwindow():
        global root1,img_2,img_3,img_4,img_5,img_6,img_7,main_frame
        root1=Tk()
        root1.geometry("1424x750")
        root1.resizable(width=False,height=False)
        root1.config(bg="#8DBEF9")
        root1.title('Zetiplan')
        #root1.iconbitmap('semssmall.ico')
        mainpage()

def mainpage():
        global img_2,img_3,img_4,img_5,img_6,img_7,main_frame,staffmng_button


 #creating all the frames and placeing them
        left_frame=LabelFrame(root1,height=740,width=180,bg="#8DBEF9")
        top_frame=LabelFrame(root1,height=120,width=1230,bg="#8DBEF9")
        main_frame=LabelFrame(root1,height=665,width=1230,bg="#8DBEF9")

        
        left_frame.place(x=5,y=5)
        top_frame.place(x=190,y=5)
        main_frame.place(x=190,y=80)

#left frame
        img_2=ImageTk.PhotoImage(Image.open("z1.jpg"))
        img_label2=Label(left_frame,image=img_2)
        img_label2.place(x=35,y=25)

    #font for all button in left frame
        myfont3 = font.Font(family='Bodoni MT Black', size=10, weight='bold')

    #Time Table Creater
        img3=PhotoImage(file='pic1.png')
        img_3=img3.subsample(6,6)
        staffmng_button=Button(left_frame,text='''Time Table
Creater''',image=img_3,compound=LEFT,bg="#8DBEF9",padx=9,command=timetable
)
        staffmng_button['font']=myfont3
        staffmng_button.place(x=12,y=200)

        #Time Table Viewer
        img4=PhotoImage(file="pic2.png")
        img_4=img4.subsample(6,6)
        staffmng_button=Button(left_frame,text='''Time Table 
Viewer''',image=img_4,compound=LEFT,bg="#8DBEF9",command=lambda:Table_Viewer(Get_DET(0)))
        staffmng_button['font']=myfont3
        staffmng_button.place(x=12,y=280)

        #Attendace
#       img5=PhotoImage(file="attendance.png")
#       img_5=img5.subsample(6,6)
#       staffmng_button=Button(left_frame,text='''Attendance
# management''',image=img_5,compound=LEFT,bg="#8DBEF9",padx=8,)
#       staffmng_button['font']=myfont3
#       staffmng_button.place(x=12,y=360)

        #top frame
        myfont4 = font.Font(family='Bodoni MT Black', size=30, weight='bold')
        head=Label(top_frame,text='Zetiplan',bg="#8DBEF9")
        head['font']=myfont4
        head.place(x=10,y=10)

    #logout button
        img7=PhotoImage(file="logout 3.png")
        img_7=img7.subsample(5,5)
        logout_button=Button(top_frame,bg="#8DBEF9",padx=8,command=logout,image=img_7)
        logout_button.place(x=1160,y=10,)

        if os.path.isfile('CSE_details.csv'):
                pass
        else:
                staffmng_button['state']=DISABLED

        


#----------------------------------------------------------------------------------------------------------


def timetable():
	global maths_noperiods, CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det

	CSE_Det={}
	ECE_Det={}
	EEE_Det={}
	Civil_Det={}
	Mech_Det={}
	maths_noperiods={}
	teachername_list=[]
	

	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:

		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='Maths Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=450,y=10)


		myfont4 = font.Font(family='Bodoni MT Black', size=18, weight='bold')
		heading_subject=Label(main_frame,text='Departmemt',bg="#8DBEF9")
		heading_subject['font']=myfont4

		heading_periods=Label(main_frame,text='''No. of
Periods''',bg="#8DBEF9")
		heading_periods['font']=myfont4



		heading_teacher=Label(main_frame,text='''Teacher name''',bg="#8DBEF9")
		heading_teacher['font']=myfont4


		heading_addteacher=Label(main_frame,text='''Add Teacher''',bg="#8DBEF9")
		heading_addteacher['font']=myfont4




		heading_subject.place(x=300,y=150)
		heading_periods.place(x=550,y=150)
		heading_teacher.place(x=730,y=150)
		heading_addteacher.place(x=300,y=80)

		Entry_addteachers=Entry(main_frame,width=20,relief=SUNKEN,bd=2)

		Entry_addteachers.place(x=550,y=80)
		


		x=300
		y=250

		for i in ['CSE','ECE','EEE','Civil','Mech']:
			yfont5 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont4
			name_subject.place(x=x,y=y)
			y+=60

		x=550
		y=260

		for i in ['CSE','ECE','EEE','Civil','Mech']:
		 	maths_noperiods["Entry"+i]=Entry(main_frame,width=15,relief=SUNKEN,bd=2)

		 	maths_noperiods["Entry"+i].place(x=x,y=y)
		 	y+=60

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
		add_button=Button(main_frame,text='ADD',bg="#8DBEF9",command=lambda:check_math(teacher_name,maths_noperiods))
		add_button['font']=myfont9
		add_button.place(x=880,y=530)


		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		addteacher_button=Button(main_frame,text='Add Teacher',bg="#8DBEF9",command=lambda:addteacher(Entry_addteachers.get(),teachername_list,add_button))
		addteacher_button['font']=myfont9
		addteacher_button.place(x=730,y=80)

		add_button["state"] = DISABLED


		







def addteacher(teachernameget,teachername_list,add_button):
	global teacher_name
	if teachernameget=='':
		messagebox.showerror("Warning","Incorrect Input")
	else:
		teacher_combobox={}
		teacher_name={}
		


		teachername_list.append(teachernameget)
		teachername=StringVar()
		teachername.set(teachername_list[0])

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)


		x=740
		y=260

		for i in ['CSE','ECE','EEE','Civil','Mech']:	

			teacher_name[i]=StringVar()
			teacher_name[i].set(teachername_list[0])
			menu_width = len(max(teachername_list, key=len))
		        
			teacher_combobox['teacher'+i] = OptionMenu(main_frame,teacher_name[i],*teachername_list,)
			teacher_combobox['teacher'+i]['menu'].config(bg="#8DBEF9")
			teacher_combobox['teacher'+i]['menu'].config(font=myfont9)
			teacher_combobox['teacher'+i]['menu'].config(activebackground="Black")  
			teacher_combobox['teacher'+i].config(width=menu_width)            
			teacher_combobox['teacher'+i].place(x=x, y=y)

			y+=60

		if len(teachername_list)>=2: 
			add_button["state"] = NORMAL


		
		
def check_math(teacher_name,maths_noperiods):

	templist=[]
	for i in maths_noperiods:
		templist.append(maths_noperiods[i].get())
	if '' in templist:
		messagebox.showerror("Warning","Entry box is not filled")
	else:


		for j in templist:
			if j.isnumeric() :
				if int(j)<=7:
					tempbool=True
				else:
					messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
					tempbool=False
					break

			else:
				messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
				tempbool=False
				break


		tempname=[]
		if tempbool:
			no_periodlist=[int(x) for x in templist]
			for i in ['CSE','ECE','EEE','Civil','Mech']:
				tempname.append(teacher_name[i].get())


			var=0
			for i in [CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det]:
				tempdict={}
				tempdict[tempname[var]]=no_periodlist[var]
				i['Maths']=tempdict
				var+=1






			PSPPdet()
		else:
			pass

	#========PSPP=====================

def PSPPdet():
	global pspp_noperiods

	pspp_noperiods={}
	teachername_list=[]
	

	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:

		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='PSPP Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=450,y=10)


		myfont4 = font.Font(family='Bodoni MT Black', size=18, weight='bold')
		heading_subject=Label(main_frame,text='Departmemt',bg="#8DBEF9")
		heading_subject['font']=myfont4

		heading_periods=Label(main_frame,text='''No. of
Periods''',bg="#8DBEF9")
		heading_periods['font']=myfont4



		heading_teacher=Label(main_frame,text='''Teacher name''',bg="#8DBEF9")
		heading_teacher['font']=myfont4


		heading_addteacher=Label(main_frame,text='''Add Teacher''',bg="#8DBEF9")
		heading_addteacher['font']=myfont4




		heading_subject.place(x=300,y=150)
		heading_periods.place(x=550,y=150)
		heading_teacher.place(x=730,y=150)
		heading_addteacher.place(x=300,y=80)

		Entry_addteachers=Entry(main_frame,width=20,relief=SUNKEN,bd=2)

		Entry_addteachers.place(x=550,y=80)
		


		x=300
		y=250

		for i in ['CSE','ECE','EEE','Civil','Mech']:
			yfont5 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont4
			name_subject.place(x=x,y=y)
			y+=60

		x=550
		y=260

		for i in ['CSE','ECE','EEE','Civil','Mech']:
		 	pspp_noperiods["Entry"+i]=Entry(main_frame,width=15,relief=SUNKEN,bd=2)

		 	pspp_noperiods["Entry"+i].place(x=x,y=y)
		 	y+=60

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
		add_button=Button(main_frame,text='ADD',bg="#8DBEF9",command=lambda:check_pspp(teacher_name,pspp_noperiods))
		add_button['font']=myfont9
		add_button.place(x=980,y=530)


		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		addteacher_button=Button(main_frame,text='Add Teacher',bg="#8DBEF9",command=lambda:addteacher(Entry_addteachers.get(),teachername_list,add_button))
		addteacher_button['font']=myfont9
		addteacher_button.place(x=730,y=80)

		add_button["state"] = DISABLED

def check_pspp(teacher_name,pspp_noperiods):

	templist=[]
	for i in pspp_noperiods:
		templist.append(pspp_noperiods[i].get())
	if '' in templist:
		messagebox.showerror("Warning","Entry box is not filled")
	else:


		for j in templist:
			if j.isnumeric() :
				if int(j)<=7:
					tempbool=True
				else:
					messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
					tempbool=False
					break

			else:
				messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
				tempbool=False
				break


		tempname=[]
		if tempbool:
			no_periodlist=[int(x) for x in templist]
			for i in ['CSE','ECE','EEE','Civil','Mech']:
				tempname.append(teacher_name[i].get())


			var=0
			for i in [CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det]:
				tempdict={}
				tempdict[tempname[var]]=no_periodlist[var]
				i['PSPP']=tempdict
				var+=1





			chemdet()
		else:
			pass

			#========Chem====================

def chemdet():
	global chem_noperiods

	chem_noperiods={}
	teachername_list=[]
	

	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:

		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='Chem Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=450,y=10)


		myfont4 = font.Font(family='Bodoni MT Black', size=18, weight='bold')
		heading_subject=Label(main_frame,text='Departmemt',bg="#8DBEF9")
		heading_subject['font']=myfont4

		heading_periods=Label(main_frame,text='''No. of
Periods''',bg="#8DBEF9")
		heading_periods['font']=myfont4



		heading_teacher=Label(main_frame,text='''Teacher name''',bg="#8DBEF9")
		heading_teacher['font']=myfont4


		heading_addteacher=Label(main_frame,text='''Add Teacher''',bg="#8DBEF9")
		heading_addteacher['font']=myfont4



		heading_subject.place(x=300,y=150)
		heading_periods.place(x=550,y=150)
		heading_teacher.place(x=730,y=150)
		heading_addteacher.place(x=300,y=80)

		Entry_addteachers=Entry(main_frame,width=20,relief=SUNKEN,bd=2)

		Entry_addteachers.place(x=550,y=80)
		


		x=300
		y=250

		for i in ['CSE','ECE','EEE','Civil','Mech']:
			yfont5 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont4
			name_subject.place(x=x,y=y)
			y+=60

		x=550
		y=260

		for i in ['CSE','ECE','EEE','Civil','Mech']:
		 	chem_noperiods["Entry"+i]=Entry(main_frame,width=15,relief=SUNKEN,bd=2)

		 	chem_noperiods["Entry"+i].place(x=x,y=y)
		 	y+=60

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
		add_button=Button(main_frame,text='ADD',bg="#8DBEF9",command=lambda:check_chem(teacher_name,chem_noperiods))
		add_button['font']=myfont9
		add_button.place(x=980,y=530)


		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		addteacher_button=Button(main_frame,text='Add Teacher',bg="#8DBEF9",command=lambda:addteacher(Entry_addteachers.get(),teachername_list,add_button))
		addteacher_button['font']=myfont9
		addteacher_button.place(x=730,y=80)

		add_button["state"] = DISABLED

def check_chem(teacher_name,chem_noperiods):

	templist=[]
	for i in chem_noperiods:
		templist.append(chem_noperiods[i].get())
	if '' in templist:
		messagebox.showerror("Warning","Entry box is not filled")
	else:


		for j in templist:
			if j.isnumeric() :
				if int(j)<=7:
					tempbool=True
				else:
					messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
					tempbool=False
					break

			else:
				messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
				tempbool=False
				break


		tempname=[]
		if tempbool:
			no_periodlist=[int(x) for x in templist]
			for i in ['CSE','ECE','EEE','Civil','Mech']:
				tempname.append(teacher_name[i].get())


			var=0
			for i in [CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det]:
				tempdict={}
				tempdict[tempname[var]]=no_periodlist[var]
				i['Chem']=tempdict
				var+=1






			phydet()
		else:
			pass

			#========PHY=====================

def phydet():
	global phy_noperiods

	phy_noperiods={}
	teachername_list=[]
	

	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:

		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='Phy Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=450,y=10)


		myfont4 = font.Font(family='Bodoni MT Black', size=18, weight='bold')
		heading_subject=Label(main_frame,text='Departmemt',bg="#8DBEF9")
		heading_subject['font']=myfont4

		heading_periods=Label(main_frame,text='''No. of
Periods''',bg="#8DBEF9")
		heading_periods['font']=myfont4



		heading_teacher=Label(main_frame,text='''Teacher name''',bg="#8DBEF9")
		heading_teacher['font']=myfont4


		heading_addteacher=Label(main_frame,text='''Add Teacher''',bg="#8DBEF9")
		heading_addteacher['font']=myfont4



		heading_subject.place(x=300,y=150)
		heading_periods.place(x=550,y=150)
		heading_teacher.place(x=730,y=150)
		heading_addteacher.place(x=300,y=80)

		Entry_addteachers=Entry(main_frame,width=20,relief=SUNKEN,bd=2)

		Entry_addteachers.place(x=550,y=80)
		


		x=300
		y=250

		for i in ['CSE','ECE','EEE','Civil','Mech']:
			yfont5 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont4
			name_subject.place(x=x,y=y)
			y+=60

		x=550
		y=260

		for i in ['CSE','ECE','EEE','Civil','Mech']:
		 	phy_noperiods["Entry"+i]=Entry(main_frame,width=15,relief=SUNKEN,bd=2)

		 	phy_noperiods["Entry"+i].place(x=x,y=y)
		 	y+=60

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
		add_button=Button(main_frame,text='ADD',bg="#8DBEF9",command=lambda:check_phy(teacher_name,phy_noperiods))
		add_button['font']=myfont9
		add_button.place(x=980,y=530)


		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		addteacher_button=Button(main_frame,text='Add Teacher',bg="#8DBEF9",command=lambda:addteacher(Entry_addteachers.get(),teachername_list,add_button))
		addteacher_button['font']=myfont9
		addteacher_button.place(x=730,y=80)

		add_button["state"] = DISABLED

def check_phy(teacher_name,phy_noperiods):

	templist=[]
	for i in phy_noperiods:
		templist.append(phy_noperiods[i].get())
	if '' in templist:
		messagebox.showerror("Warning","Entry box is not filled")
	else:


		for j in templist:
			if j.isnumeric() :
				if int(j)<=7:
					tempbool=True
				else:
					messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
					tempbool=False
					break

			else:
				messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
				tempbool=False
				break


		tempname=[]
		if tempbool:
			no_periodlist=[int(x) for x in templist]
			for i in ['CSE','ECE','EEE','Civil','Mech']:
				tempname.append(teacher_name[i].get())


			var=0
			for i in [CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det]:
				tempdict={}
				tempdict[tempname[var]]=no_periodlist[var]
				i['Phy']=tempdict
				var+=1

			





			engdet()
		else:
			pass

			#========Eng=====================


def engdet():
	global eng_noperiods

	eng_noperiods={}
	teachername_list=[]
	

	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:

		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='Eng Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=450,y=10)


		myfont4 = font.Font(family='Bodoni MT Black', size=18, weight='bold')
		heading_subject=Label(main_frame,text='Departmemt',bg="#8DBEF9")
		heading_subject['font']=myfont4

		heading_periods=Label(main_frame,text='''No. of
Periods''',bg="#8DBEF9")
		heading_periods['font']=myfont4



		heading_teacher=Label(main_frame,text='''Teacher name''',bg="#8DBEF9")
		heading_teacher['font']=myfont4


		heading_addteacher=Label(main_frame,text='''Add Teacher''',bg="#8DBEF9")
		heading_addteacher['font']=myfont4




		heading_subject.place(x=300,y=150)
		heading_periods.place(x=550,y=150)
		heading_teacher.place(x=730,y=150)
		heading_addteacher.place(x=300,y=80)

		Entry_addteachers=Entry(main_frame,width=20,relief=SUNKEN,bd=2)

		Entry_addteachers.place(x=550,y=80)
		


		x=300
		y=250

		for i in ['CSE','ECE','EEE','Civil','Mech']:
			yfont5 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont4
			name_subject.place(x=x,y=y)
			y+=60

		x=550
		y=260

		for i in ['CSE','ECE','EEE','Civil','Mech']:
		 	eng_noperiods["Entry"+i]=Entry(main_frame,width=15,relief=SUNKEN,bd=2)

		 	eng_noperiods["Entry"+i].place(x=x,y=y)
		 	y+=60

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold')
		add_button=Button(main_frame,text='ADD',bg="#8DBEF9",command=lambda:check_eng(teacher_name,eng_noperiods))
		add_button['font']=myfont9
		add_button.place(x=980,y=530)


		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		addteacher_button=Button(main_frame,text='Add Teacher',bg="#8DBEF9",command=lambda:addteacher(Entry_addteachers.get(),teachername_list,add_button))
		addteacher_button['font']=myfont9
		addteacher_button.place(x=730,y=80)

		add_button["state"] = DISABLED

def check_eng(teacher_name,eng_noperiods):

	templist=[]
	for i in eng_noperiods:
		templist.append(eng_noperiods[i].get())
	if '' in templist:
		messagebox.showerror("Warning","Entry box is not filled")
	else:


		for j in templist:
			if j.isnumeric() :
				if int(j)<=7:
					tempbool=True
				else:
					messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
					tempbool=False
					break

			else:
				messagebox.showerror("Warning","No. of periods exceeds the limit(7) and input has to be an integer")
				tempbool=False
				break


		tempname=[]
		if tempbool:
			no_periodlist=[int(x) for x in templist]
			for i in ['CSE','ECE','EEE','Civil','Mech']:
				tempname.append(teacher_name[i].get())


			var=0
			for i in [CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det]:
				tempdict={}
				tempdict[tempname[var]]=no_periodlist[var]
				i['Eng']=tempdict
				var+=1






			Totalperioddet()
		else:
			pass




#checking for total no of periods for

def Totalperioddet():


	total_periods=[]
	for i in [CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det]:
		templist=[]
		for j in i:
			for k in i[j]:
				templist.append(i[j][k])

		total_periods.append([int(x) for x in templist])

	print(total_periods)


	if sum(total_periods[0])>23 or sum(total_periods[1])>23 or sum(total_periods[2])>23 or sum(total_periods[3])>23 or sum(total_periods[4])>23:
		messagebox.showerror("Warning","No. of periods exceeds the total limit(23) ")
		timetable()

	else:
		Labdet()









#Getting CSE lab,lib,pt and Valur course
def Labdet():
	global CSE_TT,ECE_TT,EEE_TT,Civil_TT,Mech_TT
	CSE_TT=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	EEE_TT=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	ECE_TT=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	Civil_TT=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	Mech_TT=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:


		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='Phy/Chem Lab Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=440,y=20)

		x=320
		y=150

		for i in ["CSE","ECE","EEE","Civil","Mech"]:

			myfont5 = font.Font(family='Bodoni MT Black', size=20, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont5

			name_subject.place(x=x,y=y)
			y+=80


		myfont5 = font.Font(family='Bodoni MT Black', size=15, weight='bold')

		CSE_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
		CSE_day=StringVar()
		CSE_day.set(CSE_list[0])
		        

		combo_CSE = OptionMenu(main_frame,CSE_day,*CSE_list)
		#combo_lab['values']=labs_list
		combo_CSE['menu'].config(bg="#8DBEF9")
		combo_CSE['menu'].config(font=myfont5)
		combo_CSE['menu'].config(activebackground="Black")                
		combo_CSE.place(x=700, y=155)
		


		ECE_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
		ECE_day=StringVar()
		ECE_day.set(ECE_list[0])
		        

		combo_ECE = OptionMenu(main_frame,ECE_day,*ECE_list)
		combo_ECE['menu'].config(bg="#8DBEF9")
		combo_ECE['menu'].config(font=myfont5)
		combo_ECE['menu'].config(activebackground="Black")
		combo_ECE.place(x=700, y=225)
		


		EEE_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
		EEE_day=StringVar()
		EEE_day.set(EEE_list[0])
		        

		combo_EEE = OptionMenu(main_frame,EEE_day,*EEE_list)
		combo_EEE['menu'].config(bg="#8DBEF9")
		combo_EEE['menu'].config(font=myfont5)
		combo_EEE['menu'].config(activebackground="Black")
		combo_EEE.place(x=700, y=305)

		Civil_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
		Civil_day=StringVar()
		Civil_day.set(Civil_list[0])
		        

		combo_Civil = OptionMenu(main_frame,Civil_day,*Civil_list)
		combo_Civil['menu'].config(bg="#8DBEF9")
		combo_Civil['menu'].config(font=myfont5)
		combo_Civil['menu'].config(activebackground="Black")
		combo_Civil.place(x=700, y=385)

		Mech_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
		Mech_day=StringVar()
		Mech_day.set(Mech_list[0])
		        

		combo_Mech = OptionMenu(main_frame,Mech_day,*Mech_list)
		combo_Mech['menu'].config(bg="#8DBEF9")
		combo_Mech['menu'].config(font=myfont5)
		combo_Mech['menu'].config(activebackground="Black")
		combo_Mech.place(x=700, y=465)

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		add_button=Button(main_frame,text='Next',bg="#8DBEF9",command=lambda:Lab_checkdet(CSE_day.get(),ECE_day.get(),EEE_day.get(),Civil_day.get(),Mech_day.get(),CSE_list,ECE_list,EEE_list,Civil_list,Mech_list))
		add_button['font']=myfont9
		add_button.place(x=980,y=530)

def Lab_checkdet(CSE_day,ECE_day,EEE_day,Civil_day,Mech_day,CSE_list,ECE_list,EEE_list,Civil_list,Mech_list):
	checklist=[CSE_day,ECE_day,EEE_day,Civil_day,Mech_day]
	if len(list(set(checklist)))!=len(checklist):
		messagebox.showerror("Warning","Incorrect Input")


	else:
		CSE_TT[day[CSE_day]][4],CSE_TT[day[CSE_day]][5],CSE_TT[day[CSE_day]][6]=mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab']
		ECE_TT[day[ECE_day]][4],ECE_TT[day[ECE_day]][5],ECE_TT[day[ECE_day]][6]=mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab']
		EEE_TT[day[EEE_day]][4],EEE_TT[day[EEE_day]][5],EEE_TT[day[EEE_day]][6]=mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab']
		Civil_TT[day[Civil_day]][4],Civil_TT[day[Civil_day]][5],Civil_TT[day[Civil_day]][6]=mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab']
		Mech_TT[day[Mech_day]][4],Mech_TT[day[Mech_day]][5],Mech_TT[day[Mech_day]][6]=mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab'],mainsub['Phy/Chem Lab']



		CSE_list.remove(CSE_day)
		EEE_list.remove(EEE_day)
		ECE_list.remove(ECE_day)
		Civil_list.remove(Civil_day)
		Mech_list.remove(Mech_day)

		PSPP_det(CSE_list,ECE_list,EEE_list,Civil_list,Mech_list)
		
def PSPP_det(CSE_list,ECE_list,EEE_list,Civil_list,Mech_list):
	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:


		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='PSPP Lab Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=440,y=20)

		x=320
		y=150

		for i in ["CSE","ECE","EEE","Civil","Mech"]:

			myfont5 = font.Font(family='Bodoni MT Black', size=20, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont5

			name_subject.place(x=x,y=y)
			y+=80


		myfont5 = font.Font(family='Bodoni MT Black', size=15, weight='bold')

		CSE_day=StringVar()
		CSE_day.set(CSE_list[0])
		        

		combo_CSE = OptionMenu(main_frame,CSE_day,*CSE_list)
		#combo_lab['values']=labs_list
		combo_CSE['menu'].config(bg="#8DBEF9")
		combo_CSE['menu'].config(font=myfont5)
		combo_CSE['menu'].config(activebackground="Black")                
		combo_CSE.place(x=700, y=155)
		


		ECE_day=StringVar()
		ECE_day.set(ECE_list[0])
		        

		combo_ECE = OptionMenu(main_frame,ECE_day,*ECE_list)
		combo_ECE['menu'].config(bg="#8DBEF9")
		combo_ECE['menu'].config(font=myfont5)
		combo_ECE['menu'].config(activebackground="Black")
		combo_ECE.place(x=700, y=225)
		


		EEE_day=StringVar()
		EEE_day.set(EEE_list[0])
		        

		combo_EEE = OptionMenu(main_frame,EEE_day,*EEE_list)
		combo_EEE['menu'].config(bg="#8DBEF9")
		combo_EEE['menu'].config(font=myfont5)
		combo_EEE['menu'].config(activebackground="Black")
		combo_EEE.place(x=700, y=305)

		Civil_day=StringVar()
		Civil_day.set(Civil_list[0])
		        

		combo_Civil = OptionMenu(main_frame,Civil_day,*Civil_list)
		combo_Civil['menu'].config(bg="#8DBEF9")
		combo_Civil['menu'].config(font=myfont5)
		combo_Civil['menu'].config(activebackground="Black")
		combo_Civil.place(x=700, y=385)

		Mech_day=StringVar()
		Mech_day.set(Mech_list[0])
		        

		combo_Mech = OptionMenu(main_frame,Mech_day,*Mech_list)
		combo_Mech['menu'].config(bg="#8DBEF9")
		combo_Mech['menu'].config(font=myfont5)
		combo_Mech['menu'].config(activebackground="Black")
		combo_Mech.place(x=700, y=465)

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		add_button=Button(main_frame,text='Next',bg="#8DBEF9",command=lambda:PSPP_checkdet(CSE_day.get(),ECE_day.get(),EEE_day.get(),Civil_day.get(),Mech_day.get(),CSE_list,ECE_list,EEE_list,Civil_list,Mech_list))
		add_button['font']=myfont9
		add_button.place(x=980,y=530)

def PSPP_checkdet(CSE_day,ECE_day,EEE_day,Civil_day,Mech_day,CSE_list,ECE_list,EEE_list,Civil_list,Mech_list):
	checklist=[CSE_day,ECE_day,EEE_day,Civil_day,Mech_day]
	if len(list(set(checklist)))!=len(checklist):
		messagebox.showerror("Warning","Incorrect Input")


	else:
		CSE_TT[day[CSE_day]][4],CSE_TT[day[CSE_day]][5],CSE_TT[day[CSE_day]][6]=mainsub['PSPP Lab'],mainsub['PSPP Lab'],mainsub['PSPP Lab']
		ECE_TT[day[ECE_day]][4],ECE_TT[day[ECE_day]][5],ECE_TT[day[ECE_day]][6]=mainsub['PSPP Lab'],mainsub['PSPP Lab'],mainsub['PSPP Lab']
		EEE_TT[day[EEE_day]][4],EEE_TT[day[EEE_day]][5],EEE_TT[day[EEE_day]][6]=mainsub['PSPP Lab'],mainsub['PSPP Lab'],mainsub['PSPP Lab']
		Civil_TT[day[Civil_day]][4],Civil_TT[day[Civil_day]][5],Civil_TT[day[Civil_day]][6]=mainsub['PSPP Lab'],mainsub['PSPP Lab'],mainsub['PSPP Lab']
		Mech_TT[day[Mech_day]][4],Mech_TT[day[Mech_day]][5],Mech_TT[day[Mech_day]][6]=mainsub['PSPP Lab'],mainsub['PSPP Lab'],mainsub['PSPP Lab']



		CSE_list.remove(CSE_day)
		EEE_list.remove(EEE_day)
		ECE_list.remove(ECE_day)
		Civil_list.remove(Civil_day)
		Mech_list.remove(Mech_day)

		PTdet(CSE_list,ECE_list,EEE_list,Civil_list,Mech_list)

def PTdet(CSE_list,ECE_list,EEE_list,Civil_list,Mech_list):
	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:


		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='PT Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=440,y=20)

		x=320
		y=150

		for i in ["CSE","ECE","EEE","Civil","Mech"]:

			myfont5 = font.Font(family='Bodoni MT Black', size=20, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont5

			name_subject.place(x=x,y=y)
			y+=80


		myfont5 = font.Font(family='Bodoni MT Black', size=15, weight='bold')

		CSE_day=StringVar()
		CSE_day.set(CSE_list[0])
		        

		combo_CSE = OptionMenu(main_frame,CSE_day,*CSE_list)
		#combo_lab['values']=labs_list
		combo_CSE['menu'].config(bg="#8DBEF9")
		combo_CSE['menu'].config(font=myfont5)
		combo_CSE['menu'].config(activebackground="Black")                
		combo_CSE.place(x=700, y=155)
		


		ECE_day=StringVar()
		ECE_day.set(ECE_list[0])
		        

		combo_ECE = OptionMenu(main_frame,ECE_day,*ECE_list)
		combo_ECE['menu'].config(bg="#8DBEF9")
		combo_ECE['menu'].config(font=myfont5)
		combo_ECE['menu'].config(activebackground="Black")
		combo_ECE.place(x=700, y=225)
		


		EEE_day=StringVar()
		EEE_day.set(EEE_list[0])
		        

		combo_EEE = OptionMenu(main_frame,EEE_day,*EEE_list)
		combo_EEE['menu'].config(bg="#8DBEF9")
		combo_EEE['menu'].config(font=myfont5)
		combo_EEE['menu'].config(activebackground="Black")
		combo_EEE.place(x=700, y=305)

		Civil_day=StringVar()
		Civil_day.set(Civil_list[0])
		        

		combo_Civil = OptionMenu(main_frame,Civil_day,*Civil_list)
		combo_Civil['menu'].config(bg="#8DBEF9")
		combo_Civil['menu'].config(font=myfont5)
		combo_Civil['menu'].config(activebackground="Black")
		combo_Civil.place(x=700, y=385)

		Mech_day=StringVar()
		Mech_day.set(Mech_list[0])
		        

		combo_Mech = OptionMenu(main_frame,Mech_day,*Mech_list)
		combo_Mech['menu'].config(bg="#8DBEF9")
		combo_Mech['menu'].config(font=myfont5)
		combo_Mech['menu'].config(activebackground="Black")
		combo_Mech.place(x=700, y=465)

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		add_button=Button(main_frame,text='Next',bg="#8DBEF9",command=lambda:PT_checkdet(CSE_day.get(),ECE_day.get(),EEE_day.get(),Civil_day.get(),Mech_day.get(),CSE_list,ECE_list,EEE_list,Civil_list,Mech_list))
		add_button['font']=myfont9
		add_button.place(x=980,y=530)

def PT_checkdet(CSE_day,ECE_day,EEE_day,Civil_day,Mech_day,CSE_list,ECE_list,EEE_list,Civil_list,Mech_list):
	checklist=[CSE_day,ECE_day,EEE_day,Civil_day,Mech_day]
	if len(list(set(checklist)))!=len(checklist):
		messagebox.showerror("Warning","Incorrect Input")


	else:
		CSE_TT[day[CSE_day]][6]=mainsub['PT']
		EEE_TT[day[EEE_day]][6]=mainsub['PT']
		ECE_TT[day[ECE_day]][6]=mainsub['PT']
		Civil_TT[day[Civil_day]][6]=mainsub['PT']
		Mech_TT[day[Mech_day]][6]=mainsub['PT']



		CSE_list.remove(CSE_day)
		EEE_list.remove(EEE_day)
		ECE_list.remove(ECE_day)
		Civil_list.remove(Civil_day)
		Mech_list.remove(Mech_day)

		Libdet(CSE_list,ECE_list,EEE_list,Civil_list,Mech_list)

def Libdet(CSE_list,ECE_list,EEE_list,Civil_list,Mech_list):
	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:


		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='Library Details',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=440,y=20)

		x=320
		y=150

		for i in ["CSE","ECE","EEE","Civil","Mech"]:

			myfont5 = font.Font(family='Bodoni MT Black', size=20, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont5

			name_subject.place(x=x,y=y)
			y+=80


		myfont5 = font.Font(family='Bodoni MT Black', size=15, weight='bold')

		CSE_day=StringVar()
		CSE_day.set(CSE_list[0])
		        

		combo_CSE = OptionMenu(main_frame,CSE_day,*CSE_list)
		#combo_lab['values']=labs_list
		combo_CSE['menu'].config(bg="#8DBEF9")
		combo_CSE['menu'].config(font=myfont5)
		combo_CSE['menu'].config(activebackground="Black")                
		combo_CSE.place(x=700, y=155)
		


		ECE_day=StringVar()
		ECE_day.set(ECE_list[0])
		        

		combo_ECE = OptionMenu(main_frame,ECE_day,*ECE_list)
		combo_ECE['menu'].config(bg="#8DBEF9")
		combo_ECE['menu'].config(font=myfont5)
		combo_ECE['menu'].config(activebackground="Black")
		combo_ECE.place(x=700, y=225)
		


		EEE_day=StringVar()
		EEE_day.set(EEE_list[0])
		        

		combo_EEE = OptionMenu(main_frame,EEE_day,*EEE_list)
		combo_EEE['menu'].config(bg="#8DBEF9")
		combo_EEE['menu'].config(font=myfont5)
		combo_EEE['menu'].config(activebackground="Black")
		combo_EEE.place(x=700, y=305)

		Civil_day=StringVar()
		Civil_day.set(Civil_list[0])
		        

		combo_Civil = OptionMenu(main_frame,Civil_day,*Civil_list)
		combo_Civil['menu'].config(bg="#8DBEF9")
		combo_Civil['menu'].config(font=myfont5)
		combo_Civil['menu'].config(activebackground="Black")
		combo_Civil.place(x=700, y=385)

		Mech_day=StringVar()
		Mech_day.set(Mech_list[0])
		        

		combo_Mech = OptionMenu(main_frame,Mech_day,*Mech_list)
		combo_Mech['menu'].config(bg="#8DBEF9")
		combo_Mech['menu'].config(font=myfont5)
		combo_Mech['menu'].config(activebackground="Black")
		combo_Mech.place(x=700, y=465)

		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		add_button=Button(main_frame,text='Next',bg="#8DBEF9",command=lambda:Lib_checkdet(CSE_day.get(),ECE_day.get(),EEE_day.get(),Civil_day.get(),Mech_day.get(),CSE_list,ECE_list,EEE_list,Civil_list,Mech_list))
		add_button['font']=myfont9
		add_button.place(x=980,y=530)

def Lib_checkdet(CSE_day,ECE_day,EEE_day,Civil_day,Mech_day,CSE_list,ECE_list,EEE_list,Civil_list,Mech_list):
	checklist=[CSE_day,ECE_day,EEE_day,Civil_day,Mech_day]
	if len(list(set(checklist)))!=len(checklist):
		messagebox.showerror("Warning","Incorrect Input")


	else:
		CSE_TT[day[CSE_day]][5]=mainsub['Library']
		EEE_TT[day[EEE_day]][5]=mainsub['Library']
		ECE_TT[day[ECE_day]][5]=mainsub['Library']
		Civil_TT[day[Civil_day]][5]=mainsub['Library']
		Mech_TT[day[Mech_day]][5]=mainsub['Library']



		CSE_list.remove(CSE_day)
		EEE_list.remove(EEE_day)
		ECE_list.remove(ECE_day)
		Civil_list.remove(Civil_day)
		Mech_list.remove(Mech_day)


		TWD(CSE_list[0],ECE_list[0],EEE_list[0],Civil_list[0],Mech_list[0])

def TWD(CSE_day,ECE_day,EEE_day,Civil_day,Mech_day):
    checklist=[CSE_day,ECE_day,EEE_day,Civil_day,Mech_day]
    if len(list(set(checklist)))!=len(checklist):
        messagebox.showerror("Warning","Incorrect Input")


    else:
        CSE_TT[day[CSE_day]][5]=mainsub['TWM']
        EEE_TT[day[EEE_day]][5]=mainsub['TWM']
        ECE_TT[day[ECE_day]][5]=mainsub['TWM']
        Civil_TT[day[Civil_day]][5]=mainsub['TWM']
        Mech_TT[day[Mech_day]][5]=mainsub['TWM']


        VAC()

        

def VAC():
	global VAC_dict,club_day
	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:

		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text='Value Added Course and Club',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=440,y=20)


		CSE_VAC_Var=StringVar()
		ECE_VAC_Var=StringVar()
		EEE_VAC_Var=StringVar()
		Civil_VAC_Var=StringVar()
		Mech_VAC_Var=StringVar()

		VAC_dict={}
		VAC_check={}

		x=450
		y=110

		for i in ["CSE","ECE","EEE","Civil","Mech"]:

			myfont5 = font.Font(family='Bodoni MT Black', size=20, weight='bold')
			name_subject=Label(main_frame,text=i,bg="#8DBEF9")
			name_subject['font']=myfont5

			name_subject.place(x=x,y=y)
			y+=80



		x=650
		y=110

		for i in ['CSE','ECE','EEE','Civil','Mech']:	

			VAC_dict[i]=StringVar()
			VAC_dict[i].set('No')
			

			myfont5 = font.Font(family='Bodoni MT Black', size=16, weight='bold')
		        
			VAC_check['teacher'+i] =Checkbutton(main_frame,text='Yes',variable=VAC_dict[i],onvalue='Yes',offvalue='No',bg="#8DBEF9")
			VAC_check['teacher'+i]['font']=myfont5
           
			VAC_check['teacher'+i].place(x=x, y=y)
			

			y+=80



		myfont9 = font.Font(family='Bodoni MT Black', size=12, weight='bold',)
		add_button=Button(main_frame,text='Next',bg="#8DBEF9",command=VAC_checkdet)
		add_button['font']=myfont9
		add_button.place(x=980,y=530)

		myfont4 = font.Font(family='Bodoni MT Black', size=20, weight='bold')
		heading_subject=Label(main_frame,text='Club',bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=450,y=520)



		daylist=['Monday','Tuesday','Wednesday','Thursday','Friday']
		club_day=StringVar()
		club_day.set(daylist[0])
	
		myfont9 = font.Font(family='Bodoni MT Black', size=16, weight='bold')
		club_daybox = OptionMenu(main_frame,club_day,*daylist,)
		club_daybox.config(font=myfont9)
		club_daybox['menu'].config(bg="#8DBEF9")
		club_daybox['menu'].config(font=myfont9)
		club_daybox['menu'].config(activebackground="Black")  

		club_daybox.place(x=650, y=520)


		



def VAC_checkdet():


	templist=[]
	for i in [VAC_dict['CSE'].get(),VAC_dict['ECE'].get(),VAC_dict['EEE'].get(),VAC_dict['Civil'].get(),VAC_dict['Mech'].get()]:
		templist.append(i)


	k=0

	for i in templist:
		tempdict={}
		if i=='Yes':
			if k ==0:
				tempdict['VAC Teacher']=2
				CSE_Det['VAC']=tempdict

			if k==1:
				tempdict['VAC Teacher']=2
				ECE_Det['VAC']=tempdict

			if k ==2:
				tempdict['VAC Teacher']=2
				EEE_Det['VAC']=tempdict

			if k ==3:
				tempdict['VAC Teacher']=2
				Civil_Det['VAC']=tempdict

			if k ==4:
				tempdict['VAC Teacher']=2
				Mech_Det['VAC']=tempdict	
		k+=1


		for dept in [CSE_TT,ECE_TT,EEE_TT,Civil_TT,Mech_TT]:
			dept[day[club_day.get()]][3]=111






	save_det()


#CSE_Det={'Maths': {'Kay': 7}, 'PSPP': {'Molo': 4}, 'Chem': {'pistu': 4}, 'Phy': {'huios': 4}, 'Eng': {'rusk': 3},}
# ECE_Det={'Maths': {'Jay': 3}, 'PSPP': {'Molo': 4}, 'Chem': {'pistu': 4}, 'Phy': {'huios': 4}, 'Eng': {'rusk': 3},}
# EEE_Det={'Maths': {'Jay': 4}, 'PSPP': {'Molo': 4}, 'Chem': {'pistu': 4}, 'Phy': {'huios': 4}, 'Eng': {'rusk': 3},}
# Civil_Det={'Maths': {'Jay': 5}, 'PSPP': {'Molo': 4}, 'Chem': {'pistu': 4}, 'Phy': {'huios': 4}, 'Eng': {'rusk': 3},}
# Mech_Det={'Maths': {'Jay': 7}, 'PSPP': {'Molo': 4}, 'Chem': {'pistu': 4}, 'Phy': {'huios': 4}, 'Eng': {'rusk': 3}}



# CSE_TT=[[0, 0, 0, 0, 105, 105, 105], [0, 0, 0, 0, 0, 106, 0], [0, 0, 0, 0, 109, 109, 109], [0, 0, 0, 0, 0, 110, 0], [0, 0, 0, 0, 0, 0, 107]]
# ECE_TT=[[0, 0, 0, 0, 0, 110, 0], [0, 0, 0,0, 0, 0, 107], [0, 0, 0, 0, 105, 105, 105], [0, 0, 0, 0, 0, 106, 0], [0, 0, 0, 0, 109, 109, 109]]
# EEE_TT=[[0, 0, 0, 0, 0, 0, 107], [0, 0, 0, 0, 105, 105, 105], [0, 0, 0, 0, 0, 106, 0], [0, 0, 0, 0, 109, 109, 109], [0, 0, 0, 0, 0, 110, 0]]
# Civil_TT=[[0, 0, 0, 0, 109, 109, 109], [0, 0, 0, 0, 0, 110, 0], [0, 0, 0, 0, 0, 0, 107], [0, 0, 0, 0, 105, 105, 105], [0, 0, 0, 0, 0, 106, 0]]
# Mech_TT=[[0, 0, 0, 0, 0, 106, 0], [0, 0, 0, 0, 109, 109, 109], [0, 0, 0, 0, 0, 110, 0], [0, 0, 0, 0, 0, 0, 107], [0, 0, 0, 0, 105, 105, 105]]







def save_det():

	k=0

	for i in ['CSE_details.csv','ECE_details.csv','EEE_details.csv','Civil_details.csv','Mech_details.csv']:
		if k==0:
			dept_tt=CSE_TT
		elif k==1:
			dept_tt=ECE_TT
		elif k==2:
			dept_tt=EEE_TT
		elif k==3:
			dept_tt=Civil_TT
		elif k==4:
			dept_tt=Mech_TT


		fileobject=open(i,'w')
		filewriter=csv.writer(fileobject)
		filewriter.writerows(dept_tt)
		fileobject.close()

		k+=1


	

	generate_table()



def generate_table():


	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:
		myfont9 = font.Font(family='Bodoni MT Black', size=22, weight='bold',)
		label_button=Label(main_frame,text='Time Table Generator',bg="#8DBEF9")
		label_button['font']=myfont9
		label_button.place(x=440,y=20)



		myfont9 = font.Font(family='Bodoni MT Black', size=20, weight='bold',)
		add_button=Button(main_frame,text='Generate Table',bg="#8DBEF9",command=get_detcheck)
		add_button['font']=myfont9
		add_button.place(x=500,y=300)




def get_detcheck():

	try:
		get_det()
	except RecursionError:
		messagebox.showinfo("Time table generator","Try Again Please")
		generate_table()




def get_det():

	global 	subdict,subjuct_dept

	subdict={}
	subjuct_dept=[]


	k=0

	for i in ['CSE_details.csv','ECE_details.csv','EEE_details.csv','Civil_details.csv','Mech_details.csv']:
		if k==0:
			dept_tt=CSE_TT
		elif k==1:
			dept_tt=ECE_TT
		elif k==2:
			dept_tt=EEE_TT
		elif k==3:
			dept_tt=Civil_TT
		elif k==4:
			dept_tt=Mech_TT


		fileobject=open(i,'r')
		filereader=csv.reader(fileobject)



		dept_tt.clear()
		for i in filereader:
			if i!=[]:

				dept_tt.append([int(x) for x in i])
		fileobject.close()

		k+=1

		

	subdict.clear()
	subjuct_dept.clear()
	create_tt()









def checkavail(templist3,day_var):
	temp_index=0
	free_periodlist=[]
	for period in templist3[day_var%5]:
		if period==0:
			free_periodlist.append(temp_index)
			temp_index+=1
		else:
			temp_index+=1
	if len(free_periodlist)==0:
		day_var+=1
		return checkavail(templist3,day_var)
		
	else:
		return free_periodlist,day_var



def array():
	arraylist=[]
	for i in range(5):
		array1=[]
		for j in range(7):
			array1.append(0)
		arraylist.append(array1)
	return arraylist





def create_tt():

	print(CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det)



	day_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]

	day_var=0
	cc=0
	dd=0
	
	for dept in [CSE_TT,ECE_TT,EEE_TT,Civil_TT,Mech_TT]:
		if dd==0:
			departmemt='CSE'
			no_periodlist=[]
			sublist=[]
			subjuct_dept=[]
			for i in CSE_Det:
				subjuct_dept.append(i)
				for j in CSE_Det[i]:
					if j not in subdict:

						subdict[j]=array()

					sublist.append(j)
					no_periodlist.append(CSE_Det[i][j])
#CSE_Det={'Maths': {'Kay': 7}, 'PSPP': {'Molo': 4}, 'Chem': {'pistu': 4}, 'Phy': {'huios': 4}, 'Eng': {'rusk': 3},}

				
		elif dd==1:
		
			departmemt='ECE'
			no_periodlist=[]
			sublist=[]
			subjuct_dept=[]
			for i in ECE_Det:
				subjuct_dept.append(i)
				for j in ECE_Det[i]:
					if j not in subdict:
						subdict[j]=array()
					sublist.append(j)
					no_periodlist.append(ECE_Det[i][j])

		elif dd==2:
			departmemt="EEE"
			no_periodlist=[]
			sublist=[]
			subjuct_dept=[]
			for i in EEE_Det:
				subjuct_dept.append(i)
				for j in EEE_Det[i]:
					if j not in subdict:
						subdict[j]=array()
					sublist.append(j)
					no_periodlist.append(EEE_Det[i][j])

		elif dd==3:
			departmemt="Civil"
			no_periodlist=[]
			sublist=[]
			subjuct_dept=[]
			for i in Civil_Det:
				subjuct_dept.append(i)
				for j in Civil_Det[i]:
					if j not in subdict:
						subdict[j]=array()
					sublist.append(j)
					no_periodlist.append(Civil_Det[i][j])
		elif dd==4:
			departmemt='Mech'
			no_periodlist=[]
			sublist=[]
			subjuct_dept=[]
			for i in Mech_Det:
				subjuct_dept.append(i)
				for j in Mech_Det[i]:
					if j not in subdict:
						subdict[j]=array()
					sublist.append(j)
					no_periodlist.append(Mech_Det[i][j])

		cc=0
		for sub in sublist:	
			subject=subjuct_dept[cc]

			templist4=[]

			for k in range(no_periodlist[cc]):#no, of periods 0 asume 7 no_periodlist=[7,4,4,4,3]
				templist3=[]
				free_periodlist=[]
				for i in range(5):
					templist2=[]
					for j in range(7):

						templist2.append(dept[i][j]-subdict[sub][i][j])
					templist3.append(templist2)

				# count=0
				# for i in range(5):
				# 	for j in range(7):
				# 		if dept[i][j]==0:
				# 			count+=1

				free_periodlist,day_var=checkavail(templist3,day_var)



				rand_index=random.choice(free_periodlist)
				dept[day_var%5][rand_index]=mainsub[subject]
				subdict[sub][day_var%5][rand_index]=maindept[departmemt]

				day_var+=1
			cc+=1
		dd+=1



	last=[]
	for i in CSE_TT:
		final=[]
		for j in i:
			final.append(revmainsub[j])
		last.append(final)
	last1=[]
	for i in EEE_TT:
		final=[]
		for j in i:
			final.append(revmainsub[j])
		last1.append(final)
	last2=[]
	for i in ECE_TT:
		final=[]
		for j in i:
			final.append(revmainsub[j])
		last2.append(final)
	last3=[]
	for i in Civil_TT:
		final=[]
		for j in i:
			final.append(revmainsub[j])
		last3.append(final)
	last4=[]
	for i in Mech_TT:
		final=[]
		for j in i:
			final.append(revmainsub[j])
		last4.append(final)




	print(last,last1,last2,last3,last4)

	save_finaldata([last,last1,last2,last3,last4])





def save_finaldata(Complete_TT):

	

	k=0

	for i in ['CSE_TT.csv','ECE_TT.csv','EEE_TT.csv','Civil_TT.csv','Mech_TT.csv']:
##		if k==0:
##			dept_tt=CSE_TT
##		elif k==1:
##			dept_tt=ECE_TT
##		elif k==2:
##			dept_tt=EEE_TT
##		elif k==3:
##			dept_tt=Civil_TT
##		elif k==4:
##			dept_tt=Mech_TT


		fileobject=open(i,'w')
		filewriter=csv.writer(fileobject)
		filewriter.writerows(Complete_TT[k])
		fileobject.close()

		k+=1


	n=0
	detailslist=[CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det]
	fileobject=open('Teachers_list.csv','w')
	filewriter=csv.writer(fileobject)
	for i in [CSE_Det,ECE_Det,EEE_Det,Civil_Det,Mech_Det]:
		
		templist=[]
		for j in i:
			templist.append([str(x) for x in i[j].keys()])
		filewriter.writerow(templist[:5])
		n+=1

	fileobject.close()


	staffmng_button['state']=NORMAL




                
                



        

	Table_Viewer(Get_DET(0))


def Table_Viewer(fullinfo):


	try:
		for widget in main_frame.winfo_children():
			widget.destroy()
	finally:


		myfont4 = font.Font(family='Bodoni MT Black', size=22, weight='bold')
		heading_subject=Label(main_frame,text=fullinfo[2],bg="#8DBEF9")
		heading_subject['font']=myfont4
		heading_subject.place(x=440,y=5)






		bottom_frame=LabelFrame(main_frame,bg="#8DBEF9")
		bottom_frame.place(x=7,y=70)






		templist=fullinfo[0]


		finallist=[]
		n=0
		for i in templist:
			i=[revday[n]]+i
			finallist.append(i)
			finallist.append(['','','','','','','',''])
			n+=1

		finallist=[["Day/Period",'1','2','3','4','5','6','7']]+[['','','','','','','','']]+finallist



		total_rows = len(finallist) 
		total_columns = len(finallist[0]) 



		for i in range(total_rows): 
			for j in range(total_columns):
				a = Label(bottom_frame,width=12,bg="#8DBEF9", font=('Bodoni MT Black',14,'bold'))
				a.grid(row=i, column=j) 
				a.config(text=finallist[i][j])
		main_frame.grid_propagate(0)



		myfont4 = font.Font(family='Bodoni MT Black', size=18, weight='bold')
		maths_label=Label(main_frame,text='Maths        :',bg="#8DBEF9")
		maths_label['font']=myfont4
		maths_label.place(x=200,y=430)

		PSPP_label=Label(main_frame,text='PSPP         :',bg="#8DBEF9")
		PSPP_label['font']=myfont4
		PSPP_label.place(x=200,y=500)

		Chem_label=Label(main_frame,text='Chemistry  :',bg="#8DBEF9")
		Chem_label['font']=myfont4
		Chem_label.place(x=200,y=570)

		Phy_label=Label(main_frame,text='Physics :',bg="#8DBEF9")
		Phy_label['font']=myfont4
		Phy_label.place(x=700,y=430)

		English_label=Label(main_frame,text='English  :',bg="#8DBEF9")
		English_label['font']=myfont4
		English_label.place(x=700,y=500)


		maths1_label=Label(main_frame,text=fullinfo[1][0],bg="#8DBEF9")
		maths1_label['font']=myfont4
		maths1_label.place(x=350,y=430)

		PSPP1_label=Label(main_frame,text=fullinfo[1][1],bg="#8DBEF9")
		PSPP1_label['font']=myfont4
		PSPP1_label.place(x=350,y=500)

		Chem_label1=Label(main_frame,text=fullinfo[1][2],bg="#8DBEF9")
		Chem_label1['font']=myfont4
		Chem_label1.place(x=350,y=570)

		Phy_label1=Label(main_frame,text=fullinfo[1][3],bg="#8DBEF9")
		Phy_label1['font']=myfont4
		Phy_label1.place(x=820,y=430)

		English_label1=Label(main_frame,text=fullinfo[1][4],bg="#8DBEF9")
		English_label1['font']=myfont4
		English_label1.place(x=820,y=500)


		position_add=abs(fullinfo[3]+1)%5
		position_prev=abs((fullinfo[3]-1)%5)


		myfont9 = font.Font(family='Bodoni MT Black', size=18, weight='bold',)
		add_button=Button(main_frame,text='Prev',bg="#8DBEF9",command=lambda:Table_Viewer(Get_DET(position_prev)))
		add_button['font']=myfont9
		add_button.place(x=10,y=600)


		myfont9 = font.Font(family='Bodoni MT Black', size=18, weight='bold',)
		back_button=Button(main_frame,text='Next',bg="#8DBEF9",command=lambda:Table_Viewer(Get_DET(position_add)))
		back_button['font']=myfont9
		back_button.place(x=1100,y=600)



              
loginpage()
root1.mainloop()
 





