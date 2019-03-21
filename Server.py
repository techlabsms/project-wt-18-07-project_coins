from TelegramBot import*
from Yolo import*
import time


class Server:


    # open configfile
    config = open("config.txt", "r")
    config = json.load(config)
    botToken = config['botToken']

    lastUpdate = 0

    yoloCommand = "cd darknet && ./darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights userPicture.jpg"
    yoloCommand = "cd darknet && ./darknet detector test ./coins.data ./coins-yolov3.cfg ./coins-yolov3_6000.weights userPicture.jpg"
    # Setup Bot and Yolo
    bot = TelegramBot(botToken)
    yolo = Yolo(yoloCommand)

    # TODO delete while True
    while True:

        if time.time() - lastUpdate > 1:

            # timer
            lastUpdate = time.time()

            # get new messages
            messagestack = bot.getNewMessages()

            # get new photos
            photostack = []
            if len(messagestack) > 0:
                for i in messagestack:
                    if 'photo' in i:
                        photostack.append(i)

                # print all found pictures
                print("Photos found:")
                for p in photostack:
                    print(p)
                print("\n")

            else:
                print("none")
                print()

            for photos in photostack:
                # download picture
                bot.getPicture(photos['photo'][-1]['file_id'])
                # send confirmation
                bot.sendMessage("Thank you for sending me your picture!" , photos['from']['id'])
                bot.sendMessage("I'm looking at it right now...", photos['from']['id'])
                # run yolo on picture
                numbers = yolo.start()
                bot.sendMessage("These are the Coins I found:", photos['from']['id'])
                # print all resulting boxes add them up and send to Telegram
                coinSum = 0
                for n in numbers:

                    if not str(n)== "" and "%" not in n:
                        print(str(n))
                        bot.sendMessage(str(n)+" Cent", photos['from']['id'])
                        coinSum = coinSum+int(n)

                bot.sendMessage("Your Sum is: " +str(coinSum) +" Cent", photos['from']['id'])




