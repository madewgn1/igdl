import requests as req
import json
from secrets import token_urlsafe
#url = "https:\/\/scontent.cdninstagram.com\/v\/t51.2885-15\/313468277_858115352224866_5688143858178090946_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=9YlKBnv3Ll8AX8PcO-o&edm=AJBgZrYBAAAA&ccb=7-5&oh=00_AfCKKzJPdD07v_3hqAhDiEv5R0hmZTj2fcdntcgAIuwrQA&oe=6363E6CF&_nc_sid=78c662"
url = "https://igdl.in/apis.php?url="
#|link = 

#x = req.get(x)
#print("")
#print(x)

def dl(link):
    get = req.get(url+link).text
    x = get.replace('\\',"")
    data = json.loads(x)
    type = data["graphql"]["shortcode_media"]["__typename"]
    if type == "GraphImage":
        h = data["graphql"]["shortcode_media"]["display_resources"][0]["src"]
#        return [i["src"] for i in h["display_resources"]]
        return h
    elif type == "GraphSidecar":
        h = data["graphql"]["shortcode_media"]["edge_sidecar_to_children"]["edges"]
        gambar = [i["node"]["display_url"] for i in h]
        return gambar

    else:
        return data["graphql"]["shortcode_media"]["video_url"]

def acak():
    return token_urlsafe(4)
def cek(link):
    get = req.get(url+link).text
    x = get.replace('\\',"")
    data = json.loads(x)
    type = data["graphql"]["shortcode_media"]["__typename"]
    return type
 
#print(dl("ttps://www.instagram.com/p/CkdUpr9v9P2/?igshid=YmMyMTA2M2Y="))

#print(dl("https://www.instagram.com/p/Cf08NZ-BGnH/?igshid=YmMyMTA2M2Y="))


#print(dl("https://www.instagram.com/tv/CkdGXSVAPk6/?igshid=YmMyMTA2M2Y="))

#print(acak())


