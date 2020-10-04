import datefinder
import winsound
import datetime

def setAlarm(text):
    date_Time = datefinder.find_dates(text)
    for match in date_Time:
        print(match)
    stringA = str(match)
    timeA = stringA[11:]
    print(timeA)
    hourA = timeA[:-6]
    print(hourA)
    minuteA = timeA[3:-3]
    print(minuteA)
    minuteA = int(minuteA)

    while True:
        if hourA == datetime.datetime.now().hour:
            if minuteA == datetime.datetime.now().minute:
                print("alarm is running...")
                winsound.playsound('D:\\VEDEOS\\Playlists\\Famous-Flute-Ringtone-2020', winsound.SND_LOOP)
            elif minuteA>datetime.datetime.now().minute:
                break
setAlarm("set alarm at 17:12")