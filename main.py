from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
from ttkbootstrap import Style


WATERMARK = 'Francisco Suarez Maceiras'


# Function to add watermark to the selected image
def add_watermark():
    # Open the selected image
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the text for the watermark and font size
    watermark_text = WATERMARK
    font = ImageFont.truetype("arial.ttf", 36)

    # Position the watermark in the bottom-right corner
    watermark_position = (image.width - 300, image.height - 100)

    # Set watermark text color and opacity
    watermark_color = (255, 255, 255, 100)

    # Add the watermark to the image
    draw.text(watermark_position, watermark_text, fill=watermark_color, font=font)

    # Prompt the user to select a file save location
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")

    # Check if the user canceled the save dialog
    if save_path:
        # Save the watermarked image
        image.save(save_path)


# Create the main window
window = Tk()
window.title("Image Watermark App")
window.minsize(width=200, height=50)
window.configure(bg="lightgray")  # Set background color


# Style the Button
style = Style(theme="pulse")


# Create a button to add watermark
add_watermark_button = ttk.Button(window, text="Select Image", style="TButton", command=add_watermark)
add_watermark_button.pack(side="top", fill="both", expand=True, padx=10, pady=10, anchor="center")


# Start the Tkinter main loop
window.mainloop()
