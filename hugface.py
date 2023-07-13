import requests
import io
from PIL import Image
import ayutils

API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def genArt(prompt_txt):
	auto_prompt = f"realistic CGI,{prompt_txt}"
	print(f"using promt: {auto_prompt}")
	#image_bytes = query({
	#"inputs": "realistic CGI, giant asteroid colliding in prehistoric african forest, dinasaurs running from asteroid ",})
	ximage_bytes = query({
	"inputs": auto_prompt,})
	text = "https://t.me/atekreartbot"
	image_bytes = ayutils.add_watermark(ximage_bytes, text)
	return image_bytes
	#return io.BytesIO(image_bytes)

#print("image_bytes")
# You can access the image with PIL.Image for example

#image = Image.open(io.BytesIO(image_bytes))
#image.save('astro.jpg')