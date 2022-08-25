from sys import argv
import os

if not argv[1]:
    print("[x] Please provide a file to compile.")
else:

    file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), argv[1])

    if not os.path.isfile(file):
        print("\n[x] File not found. Exiting. (All C files need to be in Downloads)\n")
        exit()
    elif os.path.isfile(file):
        print("\n[+] File found.")
        if not file.endswith(".c"):
            print("\n[x] File is not a C file. Exiting.\n")
            exit()
        else:
            print("\n[+] File is a C file. Compiling.\n")
            with open("../temp.py", "w") as tw:
                tw.write(open(file).read())
            with open("../temp.py", "r+") as tr:
                lines = tr.readlines()

                for i, line in enumerate(lines):
                    if line.find("// Compile - Start") != -1:
                        with open("../temp.py", "w") as tw:
                            tw.write("".join(lines[i+1:]))
            
                # Add Functions #
                with open("../temp.py", "w") as funcs:
                    funcs.write("""def backward(x, type, tn):
    if type == "rotations":
        print("\\n[+] Rotations:")

backward(1, rotations, 50)""" + open("../temp.py").read())