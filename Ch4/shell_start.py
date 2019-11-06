#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    originalFile = "mytextfile.txt"
    if path.exists(originalFile):
        # get the path to the file in the current directory
        mypath = path.abspath(originalFile)
        pathComponent, filename = path.split(mypath)
        print(mypath)

        # let's make a backup copy by appending "bak" to the name
        newFilePath = mypath + ".bak"

        # copy over the permissions, modification times, and other info
        shutil.copy(mypath, newFilePath)
        shutil.copystat(mypath, newFilePath)

        # rename the original file
        os.rename(filename, "thisNewOtherName.txt")

        # now put things into a ZIP archive
        shutil.make_archive('myArchive', 'zip', pathComponent)

        # more fine-grained control over ZIP files
        with ZipFile('mySelectiveArchive.zip', 'w') as newzip:
            newzip.write(filename)
            newzip.write('README.md')


if __name__ == "__main__":
    main()
