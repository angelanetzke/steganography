# steganography

Steganography is any method of encoding a message in such a way that it is not apparent that a message is even hidden. This program hides an image inside an image. Usage requires two images. One image, called the carrier image, can be any image. The other, the message image, must be a black and white image and have the exact same dimensions as the carrier image. The new image that is created will be visually indistiguishable from the carrier image but will have the message in the message image encoded in it.

# Usage:
To encode a file:
	-encode INPUT_FILE MESSAGE_FILE OUTPUT_FILE	
To decode a file:
	-decode INPUT_FILE OUTPUT_FILE
	
	
# Examples:
Suppose we have a carrier image called carrier.png and a message image called message.png. To encode the hidden message in message.png into landscape.png, we will create a new image called landscape.png by typing
python steg.py -encode carrier.png message.png landscape.png
Once the message is encoded we can decode the hidden message and save it as decoded.png by typing
python steg.py -decode landscape.png decoded.png
