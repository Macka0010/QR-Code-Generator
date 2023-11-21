import qrcode
from PIL import Image

# QR Code generation
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://www.hoopers.org.uk')
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

# Load and resize the logo
logo_path = r'C:\Users\danny\Desktop\Default Icon.png'  # Replace with your logo file path
logo = Image.open(logo_path)
logo_size = 225  # Adjust the size as needed
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Handling transparency if the logo has transparency
if logo.mode == 'RGBA':
    # Create a mask using the alpha channel
    logo_mask = logo.split()[3]
    # Calculate the position for the logo
    pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
    # Paste using the mask to retain the transparency
    qr_img.paste(logo, pos, mask=logo_mask)
else:
    # Calculate the position for the logo and paste it onto the QR code
    pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
    qr_img.paste(logo, pos)


# Save the QR code with logo
qr_img.save(r'C:\Users\danny\Desktop\qr_with_logo.png')
