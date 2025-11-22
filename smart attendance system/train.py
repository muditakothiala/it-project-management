from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.conector
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")
        
        # Load background image
        bg_img = Image.open(r"/Users/muditakothiala/Desktop/smart attendance system/images/bg.jpeg")
        bg_img = bg_img.resize((1530, 790))  # Resize to fill the window
        self.bg_photo = ImageTk.PhotoImage(bg_img)

        # Set as background label covering entire window
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title text label on top of background
        title_lbl = Label(self.root, text="TRAIN DATA", font=("times new roman", 35, "bold"),
                          bg="#1e3a8a", fg="#ffffff")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Add a clickable button in the center
        btn = Button(self.root, text="Click Me", font=("times new roman", 20, "bold"),bg="red", fg="white", command=self.train_classifier)
        btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
    
        faces = []
        ids = []
    
        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ========== Train the classifier And save ==========
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")

        


        

    




        

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
