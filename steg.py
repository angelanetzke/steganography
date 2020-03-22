import sys
from PIL import Image

ENCODE = 0
DECODE = 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
usage_string = "To encode a file:\n" 
usage_string += "\t-encode INPUT_FILE MESSAGE_FILE OUTPUT_FILE\n"
usage_string += "To decode a file:\n" 
usage_string += "\t-decode INPUT_FILE OUTPUT_FILE"

#Change least significant bit in the RGB value
def set_final_bit(rgb, bit):
   if rgb[2] % 2 == bit:
      return rgb
   else:
      if bit == 1:
         return (rgb[0], rgb[1], rgb[2] + 1)
      else:
         return (rgb[0], rgb[1], rgb[2] - 1)

#Creates new image using a carrier image and message image. The new
#image is derived from the RGB values from the carrier image, with the
#least significant bit of the blue value set to 1 if the corresponding
#pixel in the #message image is black or 0 if the pixel in the message
#image is white.
def encode_message(carrier, message, output):
   width, height = carrier.size
   carrier_rgb_values = list(carrier.getdata())
   message_rgb_values = list(message.getdata())
   new_rgb_values = []
   for row in range(height):
      for column in range(width):
         message_pixel = message_rgb_values[row * width + column]
         carrier_pixel = carrier_rgb_values[row * width + column]
         if message_pixel[:3] == BLACK:
            new_rgb_values.append(set_final_bit(carrier_pixel, 1))
         else:
            new_rgb_values.append(set_final_bit(carrier_pixel, 0))
   output_image = Image.new(carrier.mode, carrier.size)
   output_image.putdata(new_rgb_values)
   output_image.save(output)
   carrier.show()
   output_image.show()   

#Creates a new image using the RGB values of an image with a message
#encoded in it using the encode_message function. If the least
#significant bit of the image is 1, the pixel in the new image will be
#black. If 0, then white.
def decode_message(hidden_message, output):
   width, height = hidden_message.size
   message_rgb_values = list(hidden_message.getdata())
   new_rgb_values = []
   for row in range(height):
      for column in range(width):
         message_pixel = message_rgb_values[row * width + column]
         if message_pixel[2] % 2 == 1:
            new_rgb_values.append(BLACK)
         else:
            new_rgb_values.append(WHITE)
   output_image = Image.new(hidden_message.mode, hidden_message.size)
   output_image.putdata(new_rgb_values)
   output_image.show()
   output_image.save(output)

mode = -1
if len(sys.argv) == 5 and sys.argv[1] == "-encode":
   mode = ENCODE
elif len(sys.argv) == 4 and sys.argv[1] == "-decode":
   mode = DECODE

if mode==ENCODE:
   images_OK = True
   try:
      carrier_image = Image.open(sys.argv[2], "r")
   except:
      print("Could not open %s" % sys.argv[2])
      images_OK = False
   try:
      message_image = Image.open(sys.argv[3], "r")
   except:
      print("Could not open %s" % sys.argv[3])
      images_OK = False
   if carrier_image.size != message_image.size:
      images_OK = False
      print("Input image and message image must be the same size")
   if images_OK:
      output_image_name = sys.argv[4]
      encode_message(carrier_image, message_image, output_image_name)
   else:
      print(usage_string)
elif mode == DECODE:
   images_OK = True
   try:
      input_image = Image.open(sys.argv[2], "r")
   except:
      print("Could not open %s" % sys.argv[2])
      images_OK = False
   if images_OK:
      output_image_name = sys.argv[3]
      decode_message(input_image, output_image_name)
   else:
      print(usage_string)
else:
   print(usage_string)
   
