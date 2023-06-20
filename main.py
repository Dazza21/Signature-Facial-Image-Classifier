import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from facedetector import detectFace


def main():
    def selectPics():
        global img1, img2
        btn_run.place_forget()

        img1_filename = filedialog.askopenfilename(parent = root, initialdir = "C:/Users/", title = "Select Face or Signature Image", filetypes = [("Image files", "*.png *.jpeg")])
        img2_filename = filedialog.askopenfilename(parent = root, initialdir = "C:/Users/", title = "Select Face or Signature Image", filetypes = [("Image files", "*.png *.jpeg")])

        try:
            img1 = Image.open(img1_filename)
            img2 = Image.open(img2_filename)

            lbl_result['text'] = "Result: Images uploaded successfully!"
            btn_run.place(x = window_width/2 - 25, y = window_height/2 + 160)
        except:
            lbl_result['text'] = "Result:\nError uploading images. Please try again!"

    def run():
        res1 = detectFace(img1)
        res2 = detectFace(img2)

        if res1:
            img1.save("./Output/FaceImage/face.png")
        else:
            img1.save("./Output/SignatureImage/sig.png")

        if not res2:
            img2.save("./Output/SignatureImage/sig.png")
        else:
            img2.save("./Output/FaceImage/face.png")

        tk.messagebox.showinfo(title = "Result", message = "Images successfully processed. Check Output Folder!")
        root.destroy()

    root = Tk()
    root.title("Signature Detector")
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

    lbl_title = tk.Label(root, text = "Signature Detector", font = ("Jokerman", 35), bg = "#D2E9E9", fg = "#00B7C2")
    lbl_result = tk.Label(root, font = ("Stencil", 16), bg = "#D2E9E9", fg = "#025464")

    btn_image_slt = tk.Button(frame, text = "Upload Credential Images", bg = "#060047", fg = "#E8A0BF",
                                 activebackground = "#E384FF", activeforeground = "#2F58CD", font = ("Verdana", 16), bd = 3, relief = SUNKEN)

    btn_run = tk.Button(frame, text = "RUN!", bg = "#2B3467", fg = "#E96479",
                                 activebackground = "#E384FF", activeforeground = "#2F58CD", font = ("Jokerman", 14), bd = 3)

    btn_image_slt['command'] = selectPics
    btn_run['command'] = run

    frame.pack()

    btn_image_slt.place(x = window_width/2 - 140, y = window_height/2 - 20, width = 300)
    lbl_title.place(x = window_width/2 - 220, y = 40)
    lbl_result.place(x = window_width/2 - 220, y = window_height/2 + 70)

    root.mainloop()


main()
