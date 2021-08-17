import shutil
import datetime 
import time

print("---- File Duplicator by Luis Pavel ----")
print("")
print("---- Settings ----")
print("")
# Variables
file_name = input("- File name (without extension): ")
file_extension = input("- File extension (without dot): ")

number_of_copies = int(input("- Number of copies: "))

tic = time.perf_counter()

# For Loop
for i in range(0, number_of_copies):
    i += 1
    shutil.copy(f'{file_name}.{file_extension}', f'{file_name}{i}.{file_extension}')

toc = time.perf_counter()

print("")
print(f"- {number_of_copies} copies of {file_name}.{file_extension} were created! Check Logs.txt for more info.")



# Logs

f = open("Logs.txt", "a")
f.write(f"- [{datetime.datetime.now()}] {number_of_copies} copies of {file_name}.{file_extension} were created.\n{number_of_copies} files created in {toc-tic} seconds.\n\n")
f.close()

time.sleep(10)