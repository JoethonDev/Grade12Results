from .models import grades


def parse_grades(result):
    grade = result.serialize()
    text = f"""
    Name : {grade["name"]}\nSeat_Number : {grade["seatNo"]}\nDegree : {grade["degree"]}\nState : {grade["state"]}
    """
    return text

def get_grades(seat):
    seat = str(seat)
    if seat.isdigit():
        results = grades.objects.filter(seat_no=seat)
    else :
        results = grades.objects.filter(name__icontains=seat)
        if len(results) >= 5:
            results = results[:5]
    return results