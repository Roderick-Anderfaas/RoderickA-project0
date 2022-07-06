#Project 0
#This will be a manual tracking application, the user will enter a directory location on their system and the program
#will list any files with the filetypes pdf, djvu, & epub and then add those files to a list that stores their name and location
#The user will aalso have the option to remove any files that are too small to be manuals, either removing entries based on the number of pages or filesize 
#Other features that could be implemented could be various sorting methods (By filesize, pages, author name), allowing the user to group books into sub-libraries,
#pulling up other books or manuals by the same author or related topics 
import os
librarydict = []
print("Hello!\nEnter the name of the directory you would like and this program will organize its pdf, djvu, & epup files")
filepath = input()
if filepath == "": filepath = os.getcwd
for file in os.walk(filepath):
    if (file[:-4]==".pdf") or (file[:-5]==".djvu" or ".epub"):
        librarydict.append(file)
for a in librarydict: print(a[0])
print("What name would you like the directory to have?")
filename = input()
os.mkdir(filepath,filename)