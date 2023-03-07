import os
import csv
import random

path = "C:\\Users\\Sameed\\Desktop\\Machine-Learning-Ass-1\\Task1\\Arham - Test split\\Cropped\\"
entries = os.listdir(path)
i = 0


files = []
ages = []
for entry in entries:
    files.append([path.replace("\\",chr(92)) + entry])
    age = ""
    
    for i in range(0,len(entry)):
        if(entry[i] == "_"):
            break
        else:
            age += entry[i]

    ages.append([age])

print(files)
print(ages)


# data to be written row-wise in csv file
data = files

# opening the csv file in 'w+' mode
file = open('TrainTTT.csv', 'w+', newline ='')

# writing the data into the file
with file:
	write = csv.writer(file)
	write.writerows(data)
	# write.writerows(ages)
        
        




# while(len(files) != 50):
#     break

#     del_file = random.choice(files)

#     os.unlink("/home/sameed/Downloads/Face Dataset/crop_part1/" + del_file)
#     files.remove(del_file)

    