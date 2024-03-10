import os
import sys
import binascii


def f_little_endian(monster_var):
    byte_a = monster_var[0:2]
    byte_b = monster_var[2:4]
    byte_c = monster_var[4:6]
    byte_d = monster_var[6:8]
    l_i_var = str(byte_d + byte_c + byte_b + byte_a)
    return l_i_var


header = []
the_list = []
info_list = []
p_list = []
display_info_list = []
clean_list = []
l_i_list = []
clean_l_i_list = []

all_bytes = 0
p_counter = 0
l_i_pointers = 0  # Pointer Amount
pointer_total_value = 0
pointer_amount = 0
pointer_boneBF = 0

i = 0  # Counter for Pointers
k = 1   # Pointer Counter
m = 0  # Little-indian counter

a = 24  # This is where the Pointer Starts Writing (Must skip first 24 values
b = a + 8
v_a = 0
v_b = 0
section_value_1 = 0
section_value_2 = 0

pointer = str
next_p_counter = str
pointer_values = str
take_value = str
pointer_display = str

info_list_str = str
p1_length_on = False
make_p_a = True
p_amount_counter = str

# ----- Enter File to process -----

input_file = sys.argv[1]

"""
with open(input_file, 'rb') as f:
    hex_data = f.read().hex()

file_data_length = len(hex_data)  # needed for last pointer
file_data_length_hex = int(len(hex_data) / 2)
file_data_length_display = str(int(file_data_length / 2))
print("Total Length Decimal value : " + file_data_length_display)
print("Total Length Hexa value    : " + hex(file_data_length_hex))  # Print the Length of the file!
"""

with open(input_file, 'r') as f:
    file_data = f.read()

# ----- Start writing a new list with the entered Header values -----




for all_bytes in file_data:
    byte_content = all_bytes
    the_list.append(all_bytes)

header = ''.join(the_list)
print(header)


#  When Writing is Done -> We Make a new List from all the entered values

no_space_header = header.replace(" ", "")
no_line_jump_header = no_space_header.replace("\n", "")
print("This is no_line_jump_header\n" + no_line_jump_header + "\n \n")

# Skip first 8 values = # pointer

x = (len(no_line_jump_header) / 8) - 4  # This is to know how many times it needs to display length
y = 0

#  Ok no_line_jump_header contains the header info ordered!

for each_byte in no_line_jump_header:
    if make_p_a:
        p_counter += 1
        p_amount_counter = str(each_byte)
        info_list.append(p_amount_counter)

        if p_counter == 24:  # 12 is 6x bytes = length of pointer + Bone Joint Bit Flag
            pointer_total_value = ''.join(info_list)
            pointer_amount = pointer_total_value

            pointer_boneBF = pointer_amount[8:24]
            pointer_display = pointer_total_value[:8] + ' = Amount of Frame/Pointer\n' + pointer_amount[8:]
            print(pointer_amount + "\n" + pointer_display + " = Bone Joint Bit Flag\n")
            make_p_a = False  # Finish pointer amount
    else:
        if i <= 8:  # length of pointer
            next_p_counter = str(each_byte)
            p_list.append(next_p_counter)
            i += 1

            if i == 8:  # length of pointer
                display_info_list.append("\n")
                k_amount = str(k)
                # Convert p_list to little-indian | Different from function I made  xd
                byte_01 = p_list[0] + p_list[1]
                byte_02 = p_list[2] + p_list[3]
                byte_03 = p_list[4] + p_list[5]
                byte_04 = p_list[6] + p_list[7]
                l_i_pointers = str(byte_04 + byte_03 + byte_02 + byte_01)

                l_i_list.append(l_i_pointers)
                pointer_values = ''.join(p_list)

                print(x)
                if y < x:
                    y += 1
                    v_a = no_line_jump_header[a:b]
                    a += 8  # Set a to go to next offset
                    b = a + 8  # Set b to go to next offset
                    v_b = no_line_jump_header[a:b]

                    print(v_a)
                    print(v_b)
                    l_i_values_a = f_little_endian(v_a)
                    l_i_values_b = f_little_endian(v_b)

                    section_value_1 = int(l_i_values_a, 16)
                    section_value_2 = int(l_i_values_b, 16)
                    current_section_length = str(hex(section_value_2 - section_value_1))  # Get
                    current_section_length = current_section_length.replace("0x", "")
                    current_section_length = " (" + current_section_length.upper() + ") -> "
                    print(current_section_length)
                    # Put all info gathered in take_value
                    if k < 10:
                        k_amount = "0" + k_amount
                        take_value = (
                                "#" + k_amount + "  " + pointer_values + " = " + l_i_pointers + current_section_length)
                    else:
                        take_value = (
                                "#" + k_amount + "  " + pointer_values + " = " + l_i_pointers + current_section_length)
                else:
                    current_section_length = str(hex(section_value_2 - section_value_1))
                    current_section_length = current_section_length.replace("0x", "")
                    current_section_length = " (" + current_section_length.upper() + ") -> "
                    if k < 10:
                        k_amount = "0" + k_amount
                        take_value = (
                                "#" + k_amount + "  " + pointer_values + " = " + l_i_pointers + current_section_length)
                    else:
                        take_value = (
                                "#" + k_amount + "  " + pointer_values + " = " + l_i_pointers + current_section_length)

                display_info_list.append(take_value)
                k += 1  # +1 for each Pointer made
                i = 0   # Reset Pointer Maker
                p_list.clear()   # Reset/Empty list
                pointer_values = ""  # Reset/Empty string


display_frame_4 = f_little_endian(pointer_amount[0:8]) + ' = Amount of Frame/Pointer\n'
display_frame_2 = display_frame_4[4:8] + ' = Amount of Frame/Pointer\n'
display_bonesBF = pointer_boneBF + ' = Bone Joint Bit Flag (Still not sure about these values)\n'

z = 0
header_list = []
#Refine Header add "\n" every 32 value - Make a little function for that
for h_data in header:
    z += 1
    header_list.append(h_data)
    if z == 48:
        header_list.append("\n")
        z = 0

header = ''.join(header_list)
print(str(header))

clean_list = ''.join(display_info_list)
outfile = str(header + "\n \n" + display_frame_2 + display_bonesBF + "\nFrames" + clean_list)

with open("output_file.txt", "w") as f:
    f.write(outfile)

print(clean_list)

print("\n End of Program")