from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("AttendWise")

        # Load and resize background image
        img = Image.open(r"/Users/muditakothiala/Desktop/smart attendance system/images/bg.jpeg")
        img = img.resize((1530, 790))
        img = img.convert("RGBA")

        # Add black overlay (semi-transparent)
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 50))  
        img = Image.alpha_composite(img, overlay)

        # Convert to ImageTk
        self.photoimg = ImageTk.PhotoImage(img)

        # Background label
        bg_lbl = Label(self.root, image=self.photoimg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Title on top
        title_lbl = Label(self.root, text="AttendWise : Smart Attendance System",
                          font=("times new roman", 30, "bold"), fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # ---------------- Buttons Section ----------------
        # Button config: (ImagePath, Text, Command, x, y)
        buttons = [
            (r"/Users/muditakothiala/Desktop/smart attendance system/images/student.jpeg", "Student Details", self.student_button_clicked, 100, 100),
            (r"/Users/muditakothiala/Desktop/smart attendance system/images/face_detector.jpg", "Face Detector", self.face_detector, 400, 100),
            (r"/Users/muditakothiala/Desktop/smart attendance system/images/attendance.jpg", "Attendance", self.attendance, 700, 100),
            (r"/Users/muditakothiala/Desktop/smart attendance system/images/helpdesk.png.jpeg", "Help Desk", self.help_desk, 1000, 100),

            (r"/Users/muditakothiala/Desktop/smart attendance system/images/train.jpg", "Train Data", self.train_data, 100, 400),
            (r"/Users/muditakothiala/Desktop/smart attendance system/images/photos.png", "Photos", self.photos, 400, 400),
            (r"/Users/muditakothiala/Desktop/smart attendance system/images/developers.png", "Developer", self.developer, 700, 400),
            (r"/Users/muditakothiala/Desktop/smart attendance system/images/exit.jpg", "Exit", self.exit_app, 1000, 400),
        ]

        self.photo_refs = []  # to prevent garbage collection

        for path, text, cmd, x, y in buttons:
            img = Image.open(path)
            img = img.resize((180, 180))
            photo = ImageTk.PhotoImage(img)
            self.photo_refs.append(photo)

            btn = Button(self.root, image=photo, command=cmd, cursor="hand2", bd=0, highlightthickness=0)
            btn.place(x=x, y=y, width=180, height=180)

            lbl = Button(self.root, text=text, command=cmd,
                         font=("times new roman", 15, "bold"),
                         bg="blue", fg="black", cursor="hand2")
            lbl.place(x=x, y=y+180, width=180, height=40)




    

    # ---------------- Button Functions ----------------
    def student_button_clicked(self):
        print("🎓 Student button clicked!")
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def face_detector(self):
        print("👤 Face Detector button clicked!")
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def attendance(self):
        print("📝 Attendance button clicked!")

    def help_desk(self):
        print("❓ Help Desk button clicked!")

    def train_data(self):
        print("📊 Train Data button clicked!")
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def photos(self):
        print("🖼️ Photos button clicked!")

    def developer(self):
        print("👨‍💻 Developer button clicked!")

    def exit_app(self):
        self.root.quit()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
