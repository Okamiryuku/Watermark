from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


# Function to add watermark to the selected image
def add_watermark():
    # Open the selected image
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the text for the watermark and font size
    watermark_text = "Your Watermark"
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
window.minsize(width=200, height=200)


# Create a button to add watermark
add_watermark_button = Button(window, text="Add Watermark", command=add_watermark)
add_watermark_button.pack()

# Start the Tkinter main loop
window.mainloop()
