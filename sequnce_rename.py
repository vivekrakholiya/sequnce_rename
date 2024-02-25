import os

import shutil

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

print('welcome to sequnce rename script')
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

# import folder path
source_folder_path = str(input('sequnce folder path :-  '))
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

# new name
new_file_name = str(input('Enter_sequnce_name :-  '))
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")



# new extension
print("example : ---  enter = 1(exr) , 2 (png) , 3(jpg)  -----:   ")
extansion = int(input('Please Enter(1-3) :-  '))
if extansion == 1:
    new_extension = ".exr"
elif extansion== 2:
    new_extension = ".png"
elif extansion== 3:
    new_extension = ".jpg"

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

# new start frame


new_start_frame = int(input('enter frist frame number exp(1001) :-  '))
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")


# asking acreat folder or not

create_folder = input('Do you want copy re-frame sequce in to separate folder (y or n) :- ')

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

if create_folder == 'y':
    copyFile = 1
else:
    copyFile = 0


# find items in folder path
sequnce_list = os.listdir(source_folder_path)




# create folder re_frame folder if not extis
if copyFile == 1:
    re_frame = source_folder_path + '\\' + 're_frame'
    if os.path.exists(re_frame):
        print('reframe folder alredy extist')
        totle_item = len(sequnce_list) -1
    else:
        os.mkdir(re_frame)
        print('re_frame folder created...')
        totle_item = len(sequnce_list)
else:
    totle_item = len(sequnce_list)
    pass


# copy items and rename it
if copyFile == 1:
    for index, file in enumerate(sequnce_list):

        # print(file)


        sorce_file_path = str(source_folder_path + '\\' + file)

        destination_file_path = str(re_frame)
        



        if os.path.exists(str(destination_file_path + '\\' + file)):
            print('File Alredy Extis in re_frame Folder')
            print('frist move or delet files')

            break

        else:

            if index == (totle_item):
                break
            else:
                

                shutil.copy(sorce_file_path,destination_file_path) 

                # rename File

                os.rename(str(destination_file_path + '\\' + file),str(destination_file_path + '\\' + new_file_name + "." + str(new_start_frame+index) +new_extension))




                prograss = index / (totle_item) * 100
                print(str(prograss) + '%...')
                print(str(destination_file_path + '\\' + "." + new_file_name + str(new_start_frame+index) +new_extension) +'copy and rename succfully')

else:
    for index, file in enumerate(sequnce_list):

        # print(file)


        sorce_file_path = str(source_folder_path + '\\' + file)

        destination_file_path = str(source_folder_path)
        

        if index == (totle_item):
            break
        else:
                

            # shutil.copy(sorce_file_path,destination_file_path) 

            # rename File

            os.rename(str(sorce_file_path),str(destination_file_path + '\\' + new_file_name + "." + str(new_start_frame+index) +new_extension))


            prograss = index / (totle_item) * 100
            print(str(prograss) + '%...')
            print(str(destination_file_path + '\\' + new_file_name + "." + str(new_start_frame+index) + new_extension) +'rename succfully')




# Last Texts

print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('script Developed By Vivek Rakholiya')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('Email:- vivekrakholiya53@gmail.com')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')



        



