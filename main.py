from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        #ist image
        img = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\clgimg.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        #2nd img
        img1 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\images.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        
        #3rd img
        img2 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\Techno_India_University.jpg")
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
        
        title_lbl=Label(b_img,text="FACE RECOGNITAION STUDENT MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student button
        img4 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\techostudents")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(b_img,command=self.student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(b_img,command=self.student_details,text="Student details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        

        #detect face button
        img5 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\facedetect")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(b_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(b_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
         

        #attendance button
        img6 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\attendance")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(b_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(b_img,text="Attendace",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40) 
        

        #help button
        img7 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\helpdesk")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(b_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(b_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40) 
        

        #train button
        img8 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\datatraing")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(b_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(b_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40) 
       
       #photo button
        img9 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\photo_collect")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(b_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(b_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40) 
        

        #dev button
        img10 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\dev")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(b_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(b_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40) 
       
        #exit button
        img11 = Image.open(r"C:\Users\91750\Documents\face_recognitaion\images\exit")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(b_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(b_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40) 


# =============Functions buttons===========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)







if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
