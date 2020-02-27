from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#Login to Google Drive and create drive object
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)
# Importing os and glob to find all png inside subfolder
import glob, os
#040603 is folder name
os.chdir("040603")
#below statement retrive all file which is of type jpg
for file in glob.glob("*.jpg"):
    print(file)
    with open(file,"r") as f:
        fn = os.path.basename(f.name)
        #print(f.read())
        file_drive = drive.CreateFile({'title': fn })  
        file_drive.SetContentFile(fn) 
        file_drive.Upload()
        print ("The file: " + fn + " has been uploaded")
   
print ("All files have been uploaded")
