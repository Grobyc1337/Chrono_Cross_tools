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


new_anim_list = []
input_animation = []

# ----- Enter File to process (drag and drop) -----
input_file = sys.argv[1]

with open(input_file, 'r') as f:
    file_data = f.read()

# ----- Start writing a new list with the entered Animation values -----
for data in file_data:
    data_content = data
    new_anim_list.append(data)

input_animation = ''.join(new_anim_list)
print(input_animation)

#  When Writing is Done -> We Make a new List from input_animation values
#  and remove all Space and \n
no_space_input_animation = input_animation.replace("\n", "")
print("\n This is no_line_jump_header \n" + no_space_input_animation + "\n")

# Print #XX + input_animation 32 values +  ->      or  Translate Model or Rotate Model
k = 1
z = 0
bone_offset = 0
b = "6"
bone_offset = hex(bone_offset)
header_list = ['0' + bone_offset.replace("0x", "") + "  " + '#0' + str(k) + ' = ']
bone_offset = hex(int(bone_offset, 16) + int(b, 16))
#  Refine Header add "\n" every 32 value - Make a little function for that
k += 1
k_display = str(k)


for h_data in no_space_input_animation:
    z += 1
    bone_offset.replace("0X", "")
    header_list.append(h_data)
    if z == 18:  # 18 = Size of each Articulation Values for Sub_Frame(s)

        if k < 10:
            if k == 2:
                header_list.append("-> " + 'Translate Model' + "\n" + '0' + bone_offset.upper().replace("0X", "")
                                   + "  " + '#0' + k_display + ' = ')
            if k == 3:
                header_list.append("-> " + 'Rotate Model' + "\n" + '0' + bone_offset.upper().replace("0X", "")
                                   + "  " + '#0' + k_display + ' = ')
            if k > 3:
                header_list.append("-> " + "\n"+ bone_offset.upper().replace("0X", "") + "  " + '#0'
                                   + k_display + ' = ')
            z = 0
            k += 1

            bone_offset = hex(int(bone_offset, 16) + int(b, 16))
            print(bone_offset)
            k_display = str(k)
        else:
            header_list.append("-> " + "\n" + bone_offset.upper().replace("0X", "") + "  " + '#' + k_display + ' = ')
            z = 0
            k += 1
            bone_offset = hex(int(bone_offset, 16) + int(b, 16))
            k_display = str(k)

k_display = str(k)
header = ''.join(header_list)
print(str(header + " -> "))

banner_display = """******************************************************
   PC_NAME Anim Articulation for Secondary Frame(s)
****************************************************** \n"""

sub_frame = banner_display + header + " -> "

with open("output_file.txt", "w") as f:
    f.write(sub_frame)

print("\n End of Program")