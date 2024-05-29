from string import ascii_letters, punctuation, digits
from random import choices, randint

def encrypt(text):
    encode_text = ""

    c = ascii_letters + digits + punctuation
    
    # Generate random prefix
    front_length = randint(2, 100)
    random_fronts = choices(c, k=front_length)
    random_fronts = chr(front_length) + ''.join(random_fronts)
    encode_text += random_fronts
    
    # Generate random suffix
    back_length = randint(2, 100)
    random_backs = choices(c, k=back_length)
    random_backs = ''.join(random_backs) + chr(back_length)
    
    # Generate shift value
    shift = randint(1, 10)
    
    # Encode text with shift
    for i in text:
        encode_text += chr(ord(i) + shift)
    
    # Add suffix and shift value to the encoded text
    encode_text += random_backs + chr(shift)
    
    return encode_text

def decrypt(text):
    # Get the length of the prefix
    front_length = ord(text[0])
    text_without_front = text[front_length + 1:]
    
    # Get the length of the suffix
    back_length = ord(text_without_front[-2])
    text_without_suffix = text_without_front[:-back_length-2]
    
    # Get the shift value
    shift = ord(text_without_front[-1])
    
    # Decode the text by reversing the shift
    decoded_text = ""
    for i in text_without_suffix:
        decoded_text += chr(ord(i) - shift)
    
    return decoded_text