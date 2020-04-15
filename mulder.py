from os import listdir, chdir, makedirs
import platform

'''The output of this program is simple. You input the directory and file type
extension you want without the period, and you get a list back of the filenames
that have that extension in thay directory! If the list is huge, it creates
a directory in your main drive and creates a text file so it doesn't bog down
the interpreter.'''

def mulder():
  print("Welcome to the file finder!\nThe truth is in here!")
  print("Please input the directory and file type you seek.\n")
  directory = input("What directory would you like?: ")
  ext = input("What is the file extension you're looking for (do not add the '.' before the extension)?: ")
  filtered_files = [f for f in listdir(str(directory)) if f.endswith('.' + str(ext))]
  number_of_files = len(filtered_files)
  if filtered_files == []:
    return "Your file search returned no files."
  elif len(filtered_files) > 500:
    platform_type = platform.system()
    if platform_type == "Windows":
        chdir('c:\\')
        makedirs("file_search_result")
        chdir("c:\\file_search_result")
        print("You have a large number of files! The results have been put into a file in c:\\file_search_result")
        file = open("search_results.txt", "w")
        file.write(f"There are {number_of_files} files in {directory} that have the {ext} extentsion: \n \n" + str(filtered_files))
        file.close
  else:
    return f"There are {number_of_files} files in {directory} that have the {ext} extension: >>>   " + str(filtered_files)
