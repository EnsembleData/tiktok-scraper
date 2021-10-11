from tiktok_interface import Tiktok_I_IH


# Get a free token at www.influencerhunters.com
TOKEN = "XXXXXXXXXXXXX"

#Initialize sender class 
tt = Tiktok_I_IH(token_IH_API=TOKEN)

#Send the request to the IH server
print("sending the request..")
res, success = tt.get_user_posts(username = "charlidamelio", depth = 2)

if success:
    print("Success!")
    print("Retrieved the last",len(res),"posts")
else:
    print("Something went wrong, check the response for more information. \n(Did you insert a valid token?)")