import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title('QR Code Generator')
        self.master.geometry('500x400')

        # Variables to store user inputs
        self.text = StringVar()
        self.error_correction = StringVar()
        self.qr_image = None

        # Label and Entry for text input
        Label(master, text="Enter text/URL:").pack()
        Entry(master, textvariable=self.text, width=40).pack()

        # Label and OptionMenu for error correction level selection
        Label(master, text="Select Error Correction Level:").pack()
        self.error_correction.set("H")  # Default error correction level
        OptionMenu(master, self.error_correction, "L", "M", "Q", "H").pack()

        # Button to generate QR code
        Button(master, text="Generate QR Code", command=self.generate_qr_code).pack()

        # Canvas to display generated QR code
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

    def generate_qr_code(self):
        # Creating a QRCode object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Adding data to QRCode object
        qr.add_data(self.text.get())
        qr.make(fit=True)

        # Specifying error correction level
        error_correction_levels = {"L": qrcode.constants.ERROR_CORRECT_L,
                                   "M": qrcode.constants.ERROR_CORRECT_M,
                                   "Q": qrcode.constants.ERROR_CORRECT_Q,
                                   "H": qrcode.constants.ERROR_CORRECT_H}
        qr.error_correction = error_correction_levels[self.error_correction.get()]

        # Generating QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Displaying QR code image on Canvas
        qr_image = qr_image.resize((300, 300), Image.ANTIALIAS)
        self.qr_image = ImageTk.PhotoImage(qr_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.qr_image)

        # Saving QR code image
        qr_image.save("generated_qr_code.png")
        messagebox.showinfo("QR Code Generator", "QR Code generated and saved successfully!")

def main():
    root = Tk()
    app = QRCodeGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
