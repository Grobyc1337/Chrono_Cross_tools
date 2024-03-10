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
#no_space_input_animation = input_animation.replace(" ", "")
#no_space_input_animation = no_space_input_animation.replace("\n", "")
no_space_input_animation = input_animation.replace("\n", "")
print("\n This is no_line_jump_header \n" + no_space_input_animation + "\n")

# Print #XX + input_animation 32 values +  ->      or  Translate Model or Rotate Model
k = 1
z = 0

header_list = ['#0' + str(k) + ' = ']
#  Refine Header add "\n" every 32 value - Make a little function for that
k += 1
k_display = str(k)

for h_data in no_space_input_animation:
    z += 1
    header_list.append(h_data)
    if z == 36:  # 36 = Size of each Articulation Values

        if k < 10:
            if k == 2:
                header_list.append("-> " + 'Translate Model' + "\n" + '#0' + k_display + ' = ')
            if k == 3:
                header_list.append("-> " + 'Rotate Model' + "\n" + '#0' + k_display + ' = ')
            if k > 3:
                header_list.append("-> " + "\n" + '#0' + k_display + ' = ')
            z = 0
            k += 1
            k_display = str(k)
        else:
            header_list.append("-> " + "\n" + '#' + k_display + ' = ')
            z = 0
            k += 1
            k_display = str(k)

k_display = str(k)
header = ''.join(header_list)
print(str(header + " -> "))

banner_display = """**********************************************
   PC_NAME Anim Articulation for Main Frame
********************************************** \n"""

frame_1 = banner_display + header + " -> "

with open("output_file.txt", "w") as f:
    f.write(frame_1)

print("\n End of Program")