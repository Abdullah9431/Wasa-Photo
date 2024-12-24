import os
listed_operation_id = [
    "doLogin",
    "setMyUserName",
    "uploadPhoto",
    "followUser",
    "unfollowUser",
    "banUser",
    "unbanUser",
    "getUserProfile",
    "getMyStream",
    "likePhoto",
    "unlikePhoto",
    "commentPhoto",
    "uncommentPhoto",
    "deletePhoto"
]

os.chdir('/home/abdullah9431/WorkSpace/projects/wasa_project')
with open("user.yaml") as f:
    data = f.read()
    print("Implementation missing:")
    for i in listed_operation_id:
        if i not in data:
            print(i)