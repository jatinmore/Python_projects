import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=4,
)
data=("Enter text or url here")
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("insta.png")
