from TelegramBot import*
from Yolo import*


class Server:
    botToken = ""

    config = open("config.txt", 'r')
    config = json.load(config)
    botToken = config['botToken']




    bot = TelegramBot(botToken)
    yolo = Yolo()

    messageStack = bot.getNewMessages()

    photoStack = []
    if len(messageStack) > 0:
        for i in messageStack:
            if 'photo' in i:
                photoStack.append(i)

        print("Photos found:")
        for p in photoStack:
            print(p)

        print("\n")

    for p in photoStack:

        bot.getPicture(p['photo'][3]['file_id'])











