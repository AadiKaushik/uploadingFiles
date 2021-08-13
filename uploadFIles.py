import dropbox
import os 
from dropbox.files import WriteMode 



class TransferData:

    def __init__(self,access_token):
        self.access_token = access_token
        

    def uploadFiles(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        for root,dirs,files in os.walk(file_from):
           
            for filename in files:
                
                local_path = os.path.join(root,file_from)
               
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

            

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
                    print("file uploaded")



def main():
    access_token = "Gn1eiqY3M4gAAAAAAAAAARvZWW6L8U8WHRT9k60dNnhPaVdY9BYRnA3pBWFRJ46-"
    transferData = TransferData(access_token) 

    file_from = str(input("Enter the folder path to transfer : -  "))
    file_to = input("Enter the full path to upload to dropbox : - ")


    transferData.uploadFiles(file_from,file_to)
    print('Files Upload')


main()