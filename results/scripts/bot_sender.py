from results.models import listed_seats
from results.utils import get_grades, parse_grades
import telebot

def send_registered():
    bot = telebot.TeleBot("1156662740:AAEWzSmMZkdRiwlBX_fmLxdMeUuPQgE3ETM")

    seats = listed_seats.objects.all()
    for seat in seats:
        chat_id = seat.chat_id
        seat_no = seat.seat.split(",")
        for no in seat_no:
            results = get_grades(no)
            text = f"نتائج الخاصه بالرقم المسجل : {no}"
            bot.send_message(chat_id, text)
            for result in results:
                text = parse_grades(result)
                bot.send_message(chat_id, text)