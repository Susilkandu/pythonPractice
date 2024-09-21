import os #importing os module
def list_directory_contents(folder_path): #define a function that take folder path and show the contents of the folder
    try:
        # Get the list of all files of folders
        contents = os.listdir(folder_path)
        print(f"Contents of the folder is :")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"'{folder_path}' folder does not exist \n")
        getInput()
    except PermissionError:
        print(f"Permission Denied to access The folder '{folder_path}' ")
        getInput()
    except NotADirectoryError:
        print(f"'{folder_path}' is not a Folder")
        getInput()
def getInput():    #defining getInput function that control input 
    print("Press 0 for exit")
    folder_path = input(" Plese Enter Correct folder path : \t")
    if(folder_path=='0'):
        print("program terminated")
        exit()
    list_directory_contents(folder_path)
getInput()