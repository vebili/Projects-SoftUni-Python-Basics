# Отваряме текстов файл за четене:
mf=open("Н:\\Book\\Python\\poetry.txt")
# Четене съдържанието на файла:
txt=mf.read()
print("Съдържание на файла:")
# Показване съдържанието на файла:
print(txt)
# Затваряме файла:
mf.close()
print("Файлът е затворен...")
