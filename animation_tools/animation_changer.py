import os
import sys
import binascii

input_file = sys.argv[1]

with open(input_file, 'rb') as f:
    hexdata = f.read().hex()

# After getting hexdata -> we take every 2 value and put em together to create a new list

frame_size = input("What is the length of each Secondary Frames ? (in hex) : ")  # Input Frame Size
frame_size = int(frame_size, 16)  # Convert Frame Size input to Decimal values
print(hex(frame_size))            # Print Frame Size input to Hexadecimal values
frame_size = frame_size * 2       # This is because the program read 1 value at a time, not 1 byte


# Input new bones info to be used
new_bones_info = input("""Enter the values for the Bones display info
must be 6 bytes long  XX XX XX XX XX XX (in hex) : """)
new_bones_info.replace(" ", "")
print(new_bones_info)


start_offset_str = input("Which offset does the script starts at? (in hex) : ")
start_offset = int(start_offset_str, 16)  # Convert Frame Size input to Decimal values
print(hex(start_offset))


file = open('New_Frame_File.txt', 'w+')   # r+
file.truncate(0)

bone_counter = 0   # Unused for now but might be helpful to know how many Frames/Bones you edited/wanna edit
new_bone_counter = 0  # Unused for now but might be helpful if we add frame?
offset_counter = 0
skip_counter = 0

Part_1_start = True
Part_2_start = False
skip_byte = False

for each_bytes in hexdata:
    content = file.read()

    # Law 1 = Only Write bytes when skip_byte is False

    if not skip_byte:
        file.write(each_bytes)
        offset_counter += 1

    if skip_byte:
        skip_counter += 1
        if skip_counter == 12:  # Reach total skip of 12 Start writing again, 12 = Length of Bone Data
            skip_byte = False  # start writing again
            offset_counter = 0  # Reset offset_counter -> Now it will be compared to frame_size
            skip_counter = 0  # Reset skip_counter to be reused

    # Law 2 = Write until you encounter start_offset

    if Part_1_start:    # Only active while Part 1 is running (until we reach start_offset)
        if offset_counter == start_offset:  # When we start_offset must skip 12 bytes! & Write new_bones_info instead
            file.write(new_bones_info)
            skip_byte = True  # stop writing
            Part_1_start = False # We finished Part 1 -> now Part 2 Start
            Part_2_start = True

    if Part_2_start:
        if offset_counter == (frame_size - 12):  # Skip the 12 for Bones, its 66 - C
            file.write(new_bones_info)
            skip_byte = True  # stop writing
            offset_counter += 1

file.close()

# ------------------- OK PROGRAM WORK FROM HERE -------------------

# ------------ Chat GPT PROGRAM to convert to .hex file -----------

file2 = open('New_Frame_File.txt', 'r')
file2_contents = file2.read()

hex_data = file2_contents  # Replace this with your hexadecimal data

binary_data = bytes.fromhex(hex_data)

with open("output_file.bin", "wb") as f:
    f.write(binary_data)

print("\nHexadecimal data has been successfully converted to a binary file.\n")

# ----- Extra Info Display -----

total_length = len(hexdata)
total_length_hex = int(len(hexdata) / 2)
total_length_display = str(int(total_length / 2))
print("Total Length Decimal value : " + total_length_display)
print("Total Length Hexa value    : " + hex(total_length_hex))  # Print the Length of the file!
