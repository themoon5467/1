def repair_jpeg(input_file, output_file, passcode):
    
    if isinstance(passcode, int):
        
        corruption_marker = passcode.to_bytes(4, byteorder='big')
    elif isinstance(passcode, str):
        
        corruption_marker = passcode.encode('utf-8')[:4]  
    else:
        raise ValueError("Wrong format!")

    with open(input_file, "rb") as f:
        data = bytearray(f.read())

    
    data = data.replace(corruption_marker, b'')

    with open(output_file, "wb") as f:
        f.write(data)

    print(f"Repaired JPEG saved as {output_file}.")


try:
    passcode_input = input("What is the passcode? ")  
    passcode = int(passcode_input) 
except ValueError:
    print("numbers only plssss. Exiting.")
    exit()

# Run the repair function
repair_jpeg("corrupted_photo.jpg", "repaired_photo.jpg", passcode)
