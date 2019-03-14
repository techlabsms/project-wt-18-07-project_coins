from TelegramBot import*
from Yolo import*


class Server:
    botToken = ""

    config = open("config.txt", 'r')
    config = json.load(config)
    botToken = config['botToken']

    bot = TelegramBot(botToken)
    yolo = Yolo()

    bot.sendMessage("testNachricht", "621555854")

    def server(self):
        messagestack = self.bot.getNewMessages()

        photostack = []
        if len(messagestack) > 0:
            for i in messagestack:
                if 'photo' in i:
                    photostack.append(i)

            print("Photos found:")
            for p in photostack:
                print(p)

            print("\n")

        for p in photostack:

            self.bot.getPicture(p['photo'][3]['file_id'])
