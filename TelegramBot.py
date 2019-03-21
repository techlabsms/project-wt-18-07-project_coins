import json
import ssl
import urllib.request

class TelegramBot:

    messageId = 0
    #Todo: Remove SSL Bypass
    context = ssl._create_unverified_context()
    botToken = ""

    # setup Bot
    def __init__(self, bottoken):
        self.botToken = bottoken

        print("TelegramBot initialized \n")

    # download new messages and return messagestack
    def getNewMessages(self):
        print("getNewMessages...\n")
        messageStack = []

        f = urllib.request.urlopen("https://api.telegram.org/bot"+self.botToken+"/getUpdates", context=self.context)

        data = json.load(f)

        for i in data['result']:
            if i['message']['message_id'] > self.messageId:
                self.messageId= i['message']['message_id']
                messageStack.append(i['message'])

        # print new messages
        print("new Messages:")
        for n in messageStack:
            print(n)
        print()

        return messageStack

    # download picture by fileId to darknet folder
    def getPicture(self,fileId):
        # Get path
        print("fileId:")
        print(fileId+"\n")
        print("Getting Path...\n")

        f = urllib.request.urlopen("https://api.telegram.org/bot" + self.botToken + "/getFile?file_id=" + fileId,
                                   context=self.context)
        data = json.load(f)
        filepath = data['result']['file_path']
        url = "https://api.telegram.org/file/bot" + self.botToken + "/" + filepath
        print(url +"\n")

        # download file
        print("Downloading file...\n")
        file = urllib.request.urlopen(url, context=self.context)

        # save to disk
        title = "userPicture"
        new_path ="darknet/"+ title + ".jpg"
        new_days = open(new_path, 'wb')

        new_days.write(file.read())
        new_days.close()

        print("file downloaded!\n")

    # send text to chatid
    def sendMessage(self ,text, chatid):

        print("sending message...\n")
        urllib.request.urlopen("https://api.telegram.org/bot" + self.botToken + "/sendmessage?chat_id="+str(chatid)+"&text="+str(text),context=self.context)
        print("message sent!")


