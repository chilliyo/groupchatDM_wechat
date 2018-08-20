import itchat
itchat.auto_login()
itchat.send('hihi', toUserName='filehelper')

get_chatrooms = itchat.get_chatrooms()
print get_chatrooms