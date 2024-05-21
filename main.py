import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
from facedetector import detectFace


def main():
    img1 = None
    img2 = None

    def selectPic1():
        btn_run.place_forget()
        img1_filename = filedialog.askopenfilename(parent = root, initialdir = "C:/Users/", title = "Select Face or Signature Image", filetypes = [("Image files", "*.png *.jpeg *.jpg")])
        nonlocal img1, img2

        try:
            img1 = cv2.imread(img1_filename)
            if img1 is None:
                raise ValueError
            btn_image_slt1['text'] = "Image uploaded successfully!"
            btn_image_slt1.place(x = window_width/2 - 180, y = window_height/2 - 30)

        except:
            btn_image_slt1['text'] = "Could not open image!!"
            btn_image_slt1.place(x = window_width/2 - 160, y = window_height/2 - 30)

        validate()

    def selectPic2():
        btn_run.place_forget()
        img2_filename = filedialog.askopenfilename(parent = root, initialdir = "C:/Users/", title = "Select Face or Signature Image", filetypes = [("Image files", "*.png *.jpeg *.jpg")])
        nonlocal img1, img2

        try:
            img2 = cv2.imread(img2_filename)
            if img2 is None:
                raise ValueError
            btn_image_slt2['text'] = "Image uploaded successfully!"
            btn_image_slt2.place(x = window_width/2 - 180, y = window_height/2 + 30)

        except:
            btn_image_slt2['text'] = "Could not open image!!"
            btn_image_slt1.place(x = window_width/2 - 160, y = window_height/2 - 30)

        validate()

    def validate():
        if img1 is not None and img2 is not None:
            btn_run.place(x = window_width/2 - 25, y = window_height/2 + 160)

    def run():
        res1 = detectFace(img1)
        res2 = detectFace(img2)

        if res1:
            cv2.imwrite("./Output/FaceImage/face.png", img1)
        else:
            cv2.imwrite("./Output/SignatureImage/sig.png", img1)

        if not res2:
            cv2.imwrite("./Output/SignatureImage/sig.png", img2)
        else:
            cv2.imwrite("./Output/FaceImage/face.png", img2)

        tk.messagebox.showinfo(title = "Result", message = "Images successfully processed. Check Output Folder!")
        root.destroy()

    root = Tk()
    root.title("Face Detector")
    root.resizable(False, False)
    root.focus_force()

    window_height = 500
    window_width = 700

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cord = int((screen_width/2) - (window_width/2))
    y_cord = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cord, y_cord))

    frame = tk.Frame(root, width = window_width, height = window_height, bg = "#D2E9E9")

    lbl_title = tk.Label(root, text = "Face Detector", font = ("Jokerman", 35), bg = "#D2E9E9", fg = "#00B7C2")

    btn_image_slt1 = tk.Button(frame, text = "Upload Image", bg = "#060047", fg = "#E8A0BF",
                                 activebackground = "#E384FF", activeforeground = "#2F58CD", font = ("Verdana", 16, "bold"), bd = 3, relief = SUNKEN)
    btn_image_slt2 = tk.Button(frame, text = "Upload Image", bg = "#060047", fg = "#E8A0BF",
                                 activebackground = "#E384FF", activeforeground = "#2F58CD", font = ("Verdana", 16, "bold"), bd = 3, relief = SUNKEN)
    btn_run = tk.Button(frame, text = "RUN!", bg = "#00B7C2", fg = "#D2E9E9",
                                 activebackground = "#E384FF", activeforeground = "#2F58CD", font = ("Tekton Pro", 14, "bold"), bd = 3)

    btn_image_slt1['command'] = selectPic1
    btn_image_slt2['command'] = selectPic2
    btn_run['command'] = run

    frame.pack()

    btn_image_slt1.place(x = window_width/2 - 115, y = window_height/2 - 30)
    btn_image_slt2.place(x = window_width/2 - 115, y = window_height/2 + 30)
    lbl_title.place(x = window_width/2 - 170, y = 40)

    root.mainloop()


main()
