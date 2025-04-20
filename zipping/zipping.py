import zipfile
import shutil

def fileOperation():
    fileOne = open("a.txt", "a+")
    fileOne.write("\nadding more content in file one")
    fileOne.close()

    fileTwo = open("b.txt", "a+")
    fileTwo.write("\nadding more content in file two")
    fileTwo.close()

def zip_a_folder():
    comp_file = zipfile.ZipFile("comp_file.zip","a")
    comp_file.write("a.txt", compress_type=zipfile.ZIP_DEFLATED)
    comp_file.write("b.txt", compress_type=zipfile.ZIP_DEFLATED)
    comp_file.close()

def unzip_a_folder():
    zip_obj = zipfile.ZipFile("comp_file.zip", "r")
    zip_obj.extractall("un_zip_folder")
    zip_obj.close()

def zip_a_folder_using_shell():
    input_folder = "./un_zip_folder"
    output_folder = "./zip_folder_with_shell"
    shutil.make_archive(output_folder, 'zip',input_folder)

def unzip_a_folder_using_shell():
    output_folder  = "./un_zip_folder"
    input_folder = "./zip_folder_with_shell.zip"
    shutil.unpack_archive(input_folder,output_folder, 'zip')

if __name__ == "__main__":
    #fileOperation()
    #zip_a_folder()
    #unzip_a_folder()
    #zip_a_folder_using_shell()
    unzip_a_folder_using_shell()