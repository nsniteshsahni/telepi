import pyowm
import time
import random
import datetime
import telepot
import wikipedia
import json

api = '6d93d0e4608c561b117bcc41a860d938'  # API Key for OpenWaetherMap 
owm = pyowm.OWM(api)
forecast = owm.daily_forecast("Delhi,in") # Weather forecast details
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)
observation = owm.weather_at_place('Delhi,in')  #Hardcoding the weather place to be delhi,Soon add functionality to autodetect location
w = observation.get_weather() 
def handle(msg):
    chat_id = msg['chat']['id']  # Stores chat id for referencing message
    command = msg['text'] # Filters text from the message sent

    print ('Got command: %s' % command)
   # Here Starts the command interpretation
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

# Here is the Telegram Bot API key

bot = telepot.Bot('228758380:AAELxfbRv-nlJXCV_L9hP6zEHwAFf1bm040')
bot.message_loop(handle) # Calling bot and keeping it active infinitely
print ('I am listening ...')

while 1:
    time.sleep(10)
