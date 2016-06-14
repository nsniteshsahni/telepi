import pyowm
import time
import random
import datetime
import telepot
import wikipedia
import json

api = '6d93d0e4608c561b117bcc41a860d938'
owm = pyowm.OWM(api)
forecast = owm.daily_forecast("Delhi,in")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)
observation = owm.weather_at_place('Delhi,in')
w = observation.get_weather()
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/hi':
        bot.sendMessage(chat_id, "Hello")
    elif command == '/weather':
        bot.sendMessage(chat_id,"New Delhi,India\n" + w.get_detailed_status() + "\n\nTemperature Detials:\n" + str(w.get_temperature(unit='celsius'))+ "\n\nWind Speed Details:\n" + str(w.get_wind())+"\n\nCloud Coverage: \n" + str(w.get_clouds())+"%"+"\n\nHumidity: \n" + str(w.get_humidity())+"%"+"\n\nPressure Details :\n" + str(w.get_pressure())+"\n\nData fetched by openweathermap API.All copyrights reserved")
    elif '/wiki' in command :
        ny = wikipedia.summary(command[5:len(str(command))],sentences = 7)
        bot.sendMessage(chat_id,ny)
    elif command == '/help' :
        bot.sendMessage(chat_id,"List of supported commands is \n/hi - Greet Your Device\n/roll - Rolls a dice\n/weather - Tells detailed current weather report of Raspberry Pi's location\n/time - Tells current date and time\n/wiki <Topic Name> - Does a topic search on wikipedia and gives a summary of the topic.Try /wiki <Topic Name>\n\nSee your autofill for quick selection of command or tap '/' icon on right side of your chat textbox")
    else :
        bot.sendMessage(chat_id,"Type /help for list of supported commands till now,There are many more to come!!")
bot = telepot.Bot('228758380:AAELxfbRv-nlJXCV_L9hP6zEHwAFf1bm040')
bot.message_loop(handle)
print ('I am listening ...')

while 1:
    time.sleep(10)
