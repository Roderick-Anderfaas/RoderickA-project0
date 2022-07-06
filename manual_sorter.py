import os, shutil, PyPDF2
from pathlib import Path
lib_list = []
directory = str(input("Enter the directory you would like to sort:\n"))
def path_finder():
#This function takes in the directory that will be scanned for manual files
    for filename in os.listdir(directory):
        if filename.endswith('.pdf') or filename.endswith(".epub") or filename.endswith(".djvu"):
            lib_list.append(str(filename))
    

def new_folder():
    new_folder = input("Enter what you would like to name the directory that will contain every manual file:\n")
    path = os.path.join(directory,new_folder)
    os.mkdir(path)
    for filename in os.listdir(directory):
        if filename.endswith('.pdf') or filename.endswith(".epub") or filename.endswith(".djvu"):
            shutil.move((directory + '/' +filename), (path))

def clean():
#this will remove unwanted phrases from the end of a filename  
    removal = str(input("Type any words or phrases that will be removed from the end of the filename "))
    for filename in os.listdir(directory):
        if filename.endswith(removal +'.pdf') or filename.endswith(removal +'.epub') or filename.endswith(removal +'.djvu'):  
            os.rename(directory + '/' + filename, directory + '/' + filename.replace(removal, ''))


path_finder()
clean()
new_folder()
