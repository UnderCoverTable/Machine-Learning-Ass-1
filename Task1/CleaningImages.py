import os
import csv
import random

entries = os.listdir('/home/sameed/Desktop/8th_semester_SP22/CSCS 460 ML/Machine-Learning-Ass-1/Task1/Unknown/')
i = 0


files = []
ages = []
for entry in entries:
    files.append(entry)
    age = ""
    
    for i in range(0,len(entry)):
        if(entry[i] == "_"):
            break
        else:
            age += entry[i]

    ages.append([age])

print(files)
print(ages)


# while(len(files) != 50):
#     break

#     del_file = random.choice(files)

#     os.unlink("/home/sameed/Downloads/Face Dataset/crop_part1/" + del_file)
#     files.remove(del_file)

    