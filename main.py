
try: import instaloader
except ImportError :
        import os
        os.system("pip install instaloader")
        

from instaloader import *

                

L = instaloader.Instaloader()

def DownloadVideo(targetUserName):
        profile = Profile.from_username(L.context , targetUserName)
        for post in profile.get_igtv_posts():
                L.download_post(post , target= profile.username)

def DownloadPost(targetUserName):
        profile = Profile.from_username(L.context , targetUserName)
        for post in profile.get_posts():
                L.download_post(post , target= profile.username)





while(True):
        
                targetUserName= input("Lütfen hedef kullanıcı adını giriniz :")
                DownloadType = input("Tüm içeriği indirmek için 1'e, \nSadece videoları indirmek için 2'ye basınız.\n")
                if (DownloadType == "1"): 
                        print("Tüm içerikleri indiriliyor lütfen bekleyin...")
                        DownloadPost(targetUserName)
                        print("İndirme başarıyla tamamlandı!")
                        continue
                elif (DownloadType == "2"):
                        print("Sadece videolar indirilmeye başlanıyor lütfen bekleyin..")
                        DownloadVideo(targetUserName)
                        print("İndirme başarıyla tamamlandı!")
                        continue
                
                
        
                        
                             
                     
   
   
   

