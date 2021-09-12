import os
import apt

cache = apt.Cache()
if cache['aria2'].is_installed:
    print ("Aria2 is installed")
else:
    print ("Please Install aria2 package")


def downloader(itemlist):
    for item in itemlist:
        for i in item:
            print ("Downloading : " + str(i))
            directory = i.split("/")
            downloadpath =("./download/"+str(directory[2])+"/"+str(directory[3])+"/"+str(directory[4])+"/")
            if not os.path.exists(downloadpath):
                print ("DirectoryCreating Directory" + str(downloadpath))
                os.makedirs(downloadpath)
            cmd = "aria2c --continue=true -d "+ str(downloadpath)+ " " + i
            print (cmd)
            os.system(cmd)
    print ("Next Video")