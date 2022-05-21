txt = "PYTHON"
num = 20
A = txt.ljust(num, "_")
B = txt.center(num)
C = txt.rjust(num, "*")
D = txt.center(num, "*")
E = txt.center(num, "_")
print("|", A, "|")
# print("")  # print empty line
print("|", B, "|")
# print()  # print empty line
print("|", C, "|")
# print('')  # print empty line
print("|", D, "|", "\n")  # print empty line
print("|", E, "|")
# print empty line: print() or print('') or print("") or + ~,"\n")
# at the end of previous printed line.
