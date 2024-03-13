import os
import sys
import binascii


# ----- Enter File to process (drag and drop) -----
input_file = sys.argv[1]

with open(input_file, 'r') as f:
    file_data = f.read()

# ----- Program Starts by asking Frame Size -----

frame_size = input("What is the length of each Secondary Frames ? (in hex) : ")  # Input Frame Size
frame_size = int(frame_size, 16)  # Convert Frame Size input to Decimal values
print(hex(frame_size))            # Print Frame Size input to Hexadecimal values
frame_size_length = frame_size * 2       # This is because the program read 1 value at a time, not 1 byte

# ----- then ask what offset does the program starts writing -----

start_offset_str = input("Which offset does the script starts at? (in hex) : ")
start_offset = int(start_offset_str, 16)  # Convert Frame Size input to Decimal values
print(hex(start_offset))
start_offset_x2 = start_offset * 2  # Needed to cause its x2 length in Hexeditor

subframes_values = []
input_animation = []
extracted_values_list = []

# ----- Start writing a new list with the entered Animation values -----
for data in file_data:
    data_content = data
    subframes_values.append(data)

#  When Writing is Done -> We Make a clean List from input_animation values
input_animation = ''.join(subframes_values)
print(input_animation)

#  and remove all Space and \n
input_animation = input_animation.replace(" ", "")
no_space_input_animation = input_animation.replace("\n", "")
print("\n This is no_line_jump_header \n" + no_space_input_animation + "\n")


z = 0  # Skip bytes amount  (skip subframe_size)
write_bones_counter = 0
offset_counter = 1

Part_1_start = True  # Only needed when start_offset = 0
#Part_2_start = False
skip_byte = True


if start_offset == 0:  # If offset start is 0
    skip_byte = False
    Part_1_start = False

for h_data in no_space_input_animation:

    if Part_1_start:    # Only active while Part 1 is running (until we reach start_offset)
        if offset_counter == start_offset_x2:
            skip_byte = False  # Back to Writing Bones values
            Part_1_start = False  # We finished Part 1 -> now Part 2 Start
        else:  # When we start_offset must skip 12 bytes! & Write new_bones_info instead
            offset_counter += 1
    else:
        # Law 1 = Only Write bytes when skip_byte is False
        if not skip_byte:
            extracted_values_list.append(h_data)
            #offset_counter += 1
            write_bones_counter += 1
            if write_bones_counter == 12:  # Only Write 12 Bytes in every subframes
                skip_byte = True
                write_bones_counter = 0  # Reset Bone counter
        else:  # Don't Write for frame_size long
            z += 1
            if z == (frame_size * 2) - 12:   # only needs to Jump (frame_size - Bone Size)
                skip_byte = False  # Back to Writing Bones values
                z = 0  # Reset Z

#print(extracted_values_list)

k = 0
l = 0
clean_evl_list = []

clean_list = ''.join(extracted_values_list)
for cl_data in clean_list:
    k += 1
    l += 1
    clean_evl_list.append(cl_data)
    if l == 2:
        clean_evl_list.append(" ")
        l = 0
    if k == 12:
        clean_evl_list.append("\n")
        k = 0
    if k == 12:
        clean_evl_list.append("\n")
        k = 0

sub_frame = "Bones (sub_frame)\n" + ''.join(clean_evl_list)
#sub_frame = str(clean_evl_list)
print(sub_frame)

print("Jacktoast")

with open("output_file.txt", "w") as f:
    f.write(sub_frame)

print("\n End of Program")
