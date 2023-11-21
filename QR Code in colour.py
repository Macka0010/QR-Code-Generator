import qrcode
from PIL import Image

# Generate the QR code with high error correction
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)
qr.add_data('https://www.hoopers.org.uk')
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Load the logo and define its size
logo_path = r'C:\Users\danny\Desktop\Default Icon.png'
logo = Image.open(logo_path)
logo_size = 300  # This size is a balance between visibility and not covering too much of the QR code
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Calculate the position for the logo
pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

# If the logo has transparency, prepare to use it as a mask
if logo.mode == 'RGBA':
    logo_mask = logo.split()[3]
    qr_img.paste(logo, pos, mask=logo_mask)
else:
    qr_img.paste(logo, pos)

# Save the QR code with the logo integrated
qr_img.save(r'C:\Users\danny\Desktop\qr_with_logo.png')
