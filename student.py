from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        # ==============variables==========
        self.var_dep=StringVar()
        self.var_couse=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_phnno=StringVar()
        self.var_address=StringVar()
        self.var_cordin=StringVar()
        self.var_photos=StringVar()


        #ist image
        img = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\techno_india_group_cover.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        #2nd img
        img1 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\labstudent")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        
        #3rd img
        img2 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\classstudents")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130) 
        

        #bg img
        img3 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\bg_img")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b_img = Label(self.root, image=self.photoimg3)
        b_img.place(x=0, y=130, width=1530, height=710)   
        
        title_lbl=Label(b_img,text="Students Management System",font=("times new roman",35,"bold"),bg="skyblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=41)

        main_frame=Frame(b_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        ##left rfame img
        img_left = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\leftframestu")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130) 
        
        ##current course information
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=135,width=720,height=150)
          
        ##department  
        dep_lebel=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white") 
        dep_lebel.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="read only")
        dep_combo["values"]=("select department","CSE","IT","Civil","Mechanical","ECE","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        

        ##course
        course_lebel=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white") 
        course_lebel.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_couse,font=("times new roman",12,"bold"),width=20,state="read only")
        course_combo["values"]=("select course","B.Tech","Bio-Tech","BCA","BBA","B.COM","B.SC")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        ##year
        year_lebel=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white") 
        year_lebel.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="read only")
        year_combo["values"]=("select year","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         ##semester
        sem_lebel=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white") 
        sem_lebel.grid(row=1,column=2,padx=10,sticky=W)
        sem_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=20,state="read only")
        sem_combo["values"]=("select semester","semester-1","semester-2","semester-3","semester-4","semester-5","semester-6","semester-7","semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        

        #class student information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=720,height=300)

        ##student id
        Student_ID_lebel=Label(Class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white") 
        Student_ID_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Student_ID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        Student_ID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        ##student name
        Student_name_lebel=Label(Class_Student_frame,text="StudentName:",font=("times new roman",12,"bold"),bg="white") 
        Student_name_lebel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Student_name_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        Student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         ##student class divison
        Student_div_lebel=Label(Class_Student_frame,text="StudentSec:",font=("times new roman",12,"bold"),bg="white") 
        Student_div_lebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # Student_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # Student_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="read only")
        div_combo["values"]=("select section","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        ##roll no
        Student_roll_lebel=Label(Class_Student_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white") 
        Student_roll_lebel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Student_roll_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Student_roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        ##Gender
        gender_lebel=Label(Class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white") 
        gender_lebel.grid(row=2,column=0,padx=10,sticky=W)
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="read only")
        gender_combo["values"]=("select gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

       ##Dob
        Student_Dob_lebel=Label(Class_Student_frame,text="Date Of Birth:",font=("times new roman",12,"bold"),bg="white") 
        Student_Dob_lebel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Student_Dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        Student_Dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        ##eamil
        Student_email_lebel=Label(Class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white") 
        Student_email_lebel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Student_email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Student_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        ##phnno
        Student_phnno_lebel=Label(Class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white") 
        Student_phnno_lebel.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Student_phnno_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phnno,width=20,font=("times new roman",12,"bold"))
        Student_phnno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        ## ADress
        Student_add_lebel=Label(Class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white") 
        Student_add_lebel.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Student_add_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Student_add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

       ## Cordinator
        Student_Cordinator_lebel=Label(Class_Student_frame,text="Co-ordinator:",font=("times new roman",12,"bold"),bg="white") 
        Student_Cordinator_lebel.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Student_Cordinator_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_cordin,width=20,font=("times new roman",12,"bold"))
        Student_Cordinator_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take A Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Delete",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)
         
        #last frame 
        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        Take_A_Pic_btn=Button(btn_frame1,text="Take Photo Sample",width=39,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Take_A_Pic_btn.grid(row=0,column=0)
        
        Update_A_pic_btn=Button(btn_frame1,text="Update Photo Sample ",width=39,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Update_A_pic_btn.grid(row=0,column=1)






       

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        
        ##right rfame img
        img_Right = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\labstudent")
        img_Right = img_Right.resize((720, 130), Image.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

        f_lbl = Label(Right_frame, image=self.photoimg_Right)
        f_lbl.place(x=5, y=0, width=720, height=130) 

        # =========search system====
        Serach_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Serach_frame.place(x=5,y=135,width=710,height=70)

        Serach_lebel=Label(Serach_frame,text="Search By:",font=("times new roman",15,"bold"),bg="Blue",fg="white") 
        Serach_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Serach_frame,font=("times new roman",12,"bold"),width=15,state="read only")
        search_combo["values"]=("select Options","Phn_No","Student_Id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=1,pady=9,sticky=W)
        
        Serach_entry=ttk.Entry(Serach_frame,width=14,font=("times new roman",12,"bold"))
        Serach_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Serach_frame,text="Serach",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        ShowAll_btn=Button(Serach_frame,text="ShowAll",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)
        
        # =====table system====
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=210,width=720,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Dept","course","year","sem","id","name","div","roll","Dob","Email","Gender","Phnno","Address","Co-ordinator","Photo",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="Semeter")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Section")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("Dob",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Phnno",text="Phnno")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Co-ordinator",text="Co-ordinator")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("Dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Phnno",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Co-ordinator",width=100)
        self.student_table.column("Photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #======func decl=========
    def add_data(self):
        if self.var_dep.get()=="select department" or self.var_name.get()=="" or self.var_id=="":
            messagebox.showerror("Error!","All fileds arev required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root",password="Sounak@07",database="face_recong")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(
                                                                                                  
                                                                                                   self.var_dep.get(),
                                                                                                   self.var_couse.get(),
                                                                                                   self.var_year.get(),
                                                                                                   self.var_sem.get(),
                                                                                                   self.var_id.get(),
                                                                                                   self.var_name.get(),
                                                                                                   self.var_div.get(),
                                                                                                   self.var_roll.get(),
                                                                                                   self.var_gender.get(),
                                                                                                   self.var_dob.get(),
                                                                                                   self.var_email.get(),
                                                                                                   self.var_phnno.get(),
                                                                                                   self.var_address.get(),
                                                                                                   self.var_cordin.get(),
                                                                                                   self.var_radio1.get()
                                                                                                 ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","student details has been added sucessfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)   

        

    #=========fetch data========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root",password="Sounak@07",database="face_recong")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
    

    #=======get cursor========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_couse.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phnno.set(data[11]),
        self.var_address.set(data[12]),
        self.var_cordin.set(data[13]),
        self.var_radio1.set(data[14])

    #======update func======
    def update_data(self):
        if self.var_dep.get()=="select department" or self.var_name.get()=="" or self.var_id=="":
            messagebox.showerror("Error!","All fileds arev required",parent=self.root)
        else:
            try:
                Updte = messagebox.askyesno("Update","Do u want to update student details",parent=self.root)
                if Updte>0:
                    conn=mysql.connector.connect(host="localhost", username="root",password="Sounak@07",database="face_recong")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,course=%s,year=%s,sem=%s,name=%s,div=%s,roll=%s,Gender=%s,Dob=%s,Email=%s,Phnno=%s,Address=%s,Co-ordinator=%s,PhotoSampleStatus=%s where id=%s",(
                                                                                                                                                                                       self.var_dep.get(),
                                                                                                                                                                                       self.var_couse.get(),
                                                                                                                                                                                       self.var_year.get(),
                                                                                                                                                                                       self.var_sem.get(),
                                                                                                                                                                                       self.var_name.get(),
                                                                                                                                                                                       self.var_div.get(),
                                                                                                                                                                                       self.var_roll.get(),
                                                                                                                                                                                       self.var_gender.get(),
                                                                                                                                                                                       self.var_dob.get(),
                                                                                                                                                                                       self.var_email.get(),
                                                                                                                                                                                       self.var_phnno.get(),
                                                                                                                                                                                       self.var_address.get(),
                                                                                                                                                                                       self.var_cordin.get(),
                                                                                                                                                                                       self.var_radio1.get(),        
                                                                                                                                                                                       self.var_id.get()
                                                                                                                                                                                     ))   
                else:
                    if not Updte:
                        return
                messagebox.showinfo("Success","Student details sucessfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)   

    #======delete func======

   








if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
