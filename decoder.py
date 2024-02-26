import cv2
from tkinter import *
from tkinter import filedialog, messagebox
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk

class QRCodeDecoder:
    def __init__(self, master):
        self.master = master
        self.master.title('QR Code Decoder')
        self.master.geometry('500x400')

        # Variable to store decoded data
        self.decoded_data = StringVar()

        # Canvas to display selected image
        self.canvas = Canvas(master, width=400, height=300)
        self.canvas.pack()

        # Button to select image file
        self.select_button = Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

        # Button to decode QR code
        self.decode_button = Button(master, text="Decode QR Code", command=self.decode_qr_code)
        self.decode_button.pack()

        # Label to display decoded data
        self.decoded_label = Label(master, textvariable=self.decoded_data)
        self.decoded_label.pack()

    def select_image(self):
        # Open file dialog to select image file
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Display selected image on canvas
            image = Image.open(file_path)
            image = image.resize((400, 300), Image.ANTIALIAS)
            self.image_tk = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image_tk)
            self.image_path = file_path

    def decode_qr_code(self):
        try:
            # Read selected image and decode QR code
            qr_code_image = cv2.imread(self.image_path)
            decoded_objects = decode(qr_code_image)

            # Extract decoded data and display
            if decoded_objects:
                decoded_data = "\n".join([obj.data.decode('utf-8') for obj in decoded_objects])
                self.decoded_data.set(decoded_data)
            else:
                self.decoded_data.set("No QR code found in the image.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = Tk()
    app = QRCodeDecoder(root)
    root.mainloop()

if __name__ == "__main__":
    main()
