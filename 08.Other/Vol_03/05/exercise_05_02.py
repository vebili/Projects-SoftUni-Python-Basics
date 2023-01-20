# Запис във файл ред по ред
print("Writing a file line by line ")
txt = open("test.txt", "w", encoding='utf-8')

txt.write("Line 1\n")
txt.write("Line 2\n")

txt.close()

# Четене на създадения файл
print("Reading the created file ")
txt = open("test.txt", "r", encoding='utf-8')
for line in txt:
    print(line)

txt.close()
