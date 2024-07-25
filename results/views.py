from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import grades, listed_seats
from .utils import get_grades, parse_grades
import telebot
from json import loads
import time
import logging

bot = telebot.TeleBot("1156662740:AAEWzSmMZkdRiwlBX_fmLxdMeUuPQgE3ETM")
bot.delete_webhook(drop_pending_updates=True)
bot.set_webhook("https://joedev.alwaysdata.net/bot")

# Create your views here.
def index(request):
    return render(request, 'results/index.html')

def result(request, id):
    id = id.split(',')
    resultsView = []
    for seat in id:
        try :
            seat = int(seat)
            result = grades.objects.get(seat_no=seat).serialize()
            resultsView.append(result)
        except :
            print(f'Error with {seat}')
    return JsonResponse({'results' : resultsView})

@csrf_exempt
def bot_result(request):
    start_time = time.time()
    if request.headers.get('content-type') == 'application/json':
        try:
            logging.info("Request initialized")
            json_string = loads(request.body.decode('utf-8'))
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            logging.info("Request Done")
            logging.info(f"Request takes : {time.time() - start_time} seconds")
            return HttpResponse("ok")
        except Exception as e:
            print(e)
            return HttpResponse("Bad Request", status=400)
    else:
        return 'Unsupported Media Type', 415

def is_available_data():
    return len(grades.objects.all()) > 0

@bot.message_handler(func=lambda msg: is_available_data())
def get_data(message):
    start_time = time.time()
    logging.info("Processing Data")
    if "/" in message.text:
        bot.reply_to(message, "ارسل رقم الجلوس")
        return
    id = message.text.split(',')
    name =  f"{message.from_user.first_name} {message.from_user.last_name}"
    logging.info(f"Data process takes : {time.time() - start_time} seconds")
    for seat in id:
        try :
            start_time = time.time()
            results = get_grades(seat)
            print(f'Telegram User : {name}')
            for result in results :
                text = parse_grades(result)
                print(text)
                print('========')
                bot.reply_to(message, text)
            logging.info(f"Sending Process takes : {time.time() - start_time} seconds")
        except Exception as e :
            print(str(e))
            print(f'Error with {seat}')

@bot.message_handler(func=lambda msg: not is_available_data())
def register_data(message):
    logging.info("Registering Data")
    try:
        chat_id = message.chat.id
        text = message.text
        if "/" in text:
            bot.reply_to(message, "ارسل رقم الجلوس ليتم تسجيله")
            return
        listed_seats.objects.create(seat=text, chat_id=chat_id)
        bot.reply_to(message, "تم تسجيل طلبك بنجاح ستيم وصلك النتيجه فور اظهارها")
    except Exception as e:
        print(e)