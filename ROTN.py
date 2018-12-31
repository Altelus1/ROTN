import sys

def rotate(string_arg, no_rot):
	rot_output = ""
	for char in string_arg:
		rot_char = char
		if ord(char) >= 0x61 and ord(char) <= 0x7a:
			rot_char = chr((((ord(rot_char) - 0x61) + no_rot) % 26)+0x61)
		rot_output += rot_char
	return rot_output
	
	

def write_to_file(content, file_desc, current_rot_no):	
	file_desc.write("""
		At {} rotation
		===============================================================
		{}
	""".format(
		current_rot_no,
		rotate(content, current_rot_no)
	))
	
	
print("""
=============================================================
					 _____________        ___         _
	---------	    |_____  ______|      |   \       | |
	|  ____  \----------  | |            |    \      | |
	| |    |  \         \ | |            | |\  \     | |
	| |____|  /  -----   \| |   _____    | | \  \    | |
	|  ____  /  /     |  || |  |_____|   | |  \  \   | |
	|  |   \ \  |     |  || |            | |   \  \  | |
	|  |    \ \  \____|  || |            | |    \  \ | |
	|  |     \ \        / | |            | |     \  \| |
	|---      \_\______/  |_|            |_|      \____|

	By Altelus
=============================================================
""")

if len(sys.argv) < 5:
	print("""
		Correct Argument not supplied:
		Usage: python3 ROTN.py <input_file> <output_file> <rot_no> <enumerate_each_rot(y/n)>
		Example: 
			-python3 ROTN.py in.txt out.txt 26 y
			-python3 ROTN.py in.txt out.txt 3 n
	""")
	exit(0)

#arg[1] = input file
#arg[2] = output file
#arg[3] = no rotation
#arg[4] = enumerated? (y/n)

contents = ""

with open(sys.argv[1], "r") as rf:
	print("[+]Getting File Contents")
	contents = rf.read()

contents = contents.lower()	
	
with open(sys.argv[2], "w") as wf:
	if sys.argv[4] == "y":
		print("[+]Initiationg enumerated rotations...")
		for count in range(int(sys.argv[3])):
			write_to_file(contents, wf, count)
	print("[+]Initiating original rotation")
	write_to_file(contents, wf, int(sys.argv[3]))
			
	















	
