from TelegramBot import*
from Yolo import*


class Server:
    # open configfile
    config = open("config.txt", "r")
    config = json.load(config)
    botToken = config['botToken']

    # Setup Bot and Yolo
    bot = TelegramBot(botToken)
    yolo = Yolo(
        "cd darknet && ./darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights userPicture.jpg")

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

    for photos in photostack:
        # download picture
        bot.getPicture(photos['photo'][-1]['file_id'])
        # run yolo on picture
        numbers = yolo.start()
        for n in numbers:
            # print all resulting boxes and send to Telegram
            if not str(n)== "":
                print(str(n))
                bot.sendMessage(str(n), photos['from']['id'])

