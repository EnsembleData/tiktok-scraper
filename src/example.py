from tiktok_interface import Tiktok_I_ED


# Get a free token at www.influencerhunters.com
TOKEN = "INSERT YOUR TOKEN HERE"

#Initialize sender class 
tt = Tiktok_I_ED(token_ED_API=TOKEN)

#Send the request to the ED server
print("sending the request..")
res, success = tt.get_hashtag_posts(name = "magic", cursor = 0)

if success:
    print("Success!")
    print("Retrieved the last",len(res["data"]),"posts")
else:
    print("Something went wrong, check the response for more information. \n(Did you insert a valid token?)")