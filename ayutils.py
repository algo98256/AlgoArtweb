from PIL import Image, ImageDraw, ImageFont
import io

def add_watermark(image_bytes, text):
    # Open the image from bytes
    image = image = Image.open(io.BytesIO(image_bytes))

    # Create a new image with the same size and mode as the original image
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))

    # Set the watermark text and font
    text_font = ImageFont.truetype('arial.ttf', 40)  # Change the font and size as per your preference

    # Calculate the center position for the watermark text
    text_width, text_height = text_font.getsize(text)
    center_x = (image.width - text_width) // 2
    center_y = (image.height - text_height) // 2

    # Draw the watermark text on the new image
    draw = ImageDraw.Draw(watermark)
    draw.text((center_x, center_y), text, font=text_font, fill=(255, 255, 255, 128))  # Change the fill color as per your preference

    # Combine the original image and the watermark image
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)

    # Save the watermarked image to a bytes buffer
    output_buffer = io.BytesIO()
    watermarked_image.save(output_buffer, format='PNG')
    output_buffer.seek(0)

    return output_buffer.getvalue()

def readfx(file_path):
    try:
        # Open the image file
        image = Image.open(file_path)
        return image.tobytes()  # Return the image data as bytes
    except IOError:
        print(f"Unable to open image file: {file_path}")

# Example usage
#file_path = open("astro.jpg",'rb')  # Replace with your image file path
#image_data = file_path.read()#readfx(file_path)
#text = "@atekrebot"
#add_watermark(image_data, text)

