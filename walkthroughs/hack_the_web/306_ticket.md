# URL
https://hack.arrrg.de/challenge/306
# Category
General
# Concept
Creating a QR code
# Method of solve
## Linux tools
* we can use the `qrencode` tool to create a PNG to give to the challenge web app
```
qrencode -o myqrcode.png "68463@Dodo-Airlines"
```
## Python code
```
import qrcode

# Data to be encoded in the QR code
data = "68463@Dodo-Airlines"

# Create a QR code object
# version: controls the size of the QR code (1 to 40)
# error_correction: controls the error correction level (L, M, Q, H)
# box_size: controls the size of each box (pixel) in the QR code
# border: controls the thickness of the white border around the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code data
# fill_color: color of the QR code squares
# back_color: background color
img = qr.make_image(fill_color="black", back_color="white")

# Save the image as a PNG file
img.save("my_qrcode.png")

print("QR code saved as my_qrcode.png")
```
* the answer is `Animal Crossing`
