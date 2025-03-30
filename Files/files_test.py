import os
import shutil
import send2trash

def test_files():
    # show current directory path
    print(os.getcwd())
    
    # list all files in the current directory
    print(os.listdir())

    # move a file from a location to another location
    #shutil.move("source", "destination")
    # send2trash.send2trash("file_path")

    for (folder, subfolders, files) in os.walk("/Users/ashislaha/work/Projects Explore/python/basics/"):
        print("\n\n")
        print(f"current folder ==> {folder}")
        print("subfolders ==>")
        for sub_fold in subfolders:
            print(f"subfolder => {sub_fold}")
        print("Files ==>")
        for file in files:
            print(f"file {file}")

if __name__ == "__main__":
    test_files()
