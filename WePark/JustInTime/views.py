from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.db.models import Count, Q
from .models import DeviceState, SegmentState, DeviceHistoric
from django.conf import settings


# Global variables
# A dictionary that keeps hourly data for each parking segment
mega_dict = {
    5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}, 13: {},
    14: {}, 15: {}, 16: {}, 17: {}, 18: {}, 19: {}, 20: {}, 21: {}, 22: {}
}
# A dictionary that maps hour numbers to hour names
names = {
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 21: "twentyone", 22: "twentytwo"
}
# A list of the parking segment IDs
parks = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
# A list of the total amount of active devices per parking segment
amounts = [DeviceState.objects.filter(parking_segment=park)
           .count() for park in parks]
# The total amount of active devices for all parking segments
amounts.append(DeviceState.objects.all().count())
# A list of the total amount of historic data per parking segment
amount_historic = [DeviceHistoric.objects.filter(parking_segment=park)
                   .count() for park in parks]
# A dictionary that holds the percentage of occupied parking spaces for each parking segment and hour
total = {}


# Index view
def index(request):
    """
    Renders the main view of the application and displays the percentage of occupied parking spaces.

    This function accepts an HTTP request and uses it to render the index.html template.
    The template displays the percentage of occupied parking spaces for each parking segment.
    To do this, the function retrieves the current state of each parking segment from the database and passes the
    percentages to the template for rendering. It also passes the Google Maps API key to the template, which is used to
    display a map and heatmaps of the parking segments.

    Args:
        request: an HTTP request object.

    Returns:
        An HTTP response containing the rendered index.html template, displaying the percentage of occupied parking
        spaces for each parking segment and a map of the parking segments.
    """
    for park in parks:
        globals()[f"percentage_{park}"] = (
            SegmentState.objects.get(pk=park).occupied)

    return render(request, 'JustInTime/index.html', {
        'percentage_A': percentage_A,
        'percentage_B': percentage_B,
        'percentage_C': percentage_C,
        'percentage_D': percentage_D,
        'percentage_E': percentage_E,
        'percentage_F': percentage_F,
        'percentage_G': percentage_G,
        'percentage_H': percentage_H,
        'percentage_I': percentage_I,
        "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY,
    })


# Project information view
def datosProyecto(request):
    """
    This view renders the datosProyecto.html template.
    It is a static view that shows information about the project.
    """
    return render(request, 'JustInTime/datosProyecto.html')


# Statistics view
@cache_page(60 * 2)
def estadistic(request):
    """
    Renders the estadistic.html template and displays the percentage of occupied parking spaces.

    This function accepts an HTTP request and uses it to render the estadistic.html template.
    The template displays the percentage of occupied parking spaces for each parking segment and for each hour of the day.
    To do this, the function retrieves the device history from the database and calculates the percentage of occupied spaces
    for each parking segment and hour. It then passes this data to the template for rendering.
    The function also uses caching to improve performance.

    Args:
        request: an HTTP request object.

    Returns:
        An HTTP response containing the rendered estadistic.html template, displaying the percentage of occupied parking
        spaces for each parking segment and hour.
    """
    device_historics = DeviceHistoric.objects.filter(arrive_leave=True)
    for k, v in mega_dict.items():
        for i in range(len(parks)):
            mega_dict[k][parks[i]] = round(device_historics.filter(
                parking_segment=parks[i], hour_date__hour=k)
                .count() / amounts[i] * 100, 2)
            total[parks[i]] = round(device_historics.filter(
                parking_segment=parks[i])
                .count() / amount_historic[i] * 100, 2)

    for hour in mega_dict.keys():
        total[hour] = round(device_historics.filter(
            hour_date__hour=hour)
            .count() / amounts[-1] * 100, 2)

    for num, name in names.items():
        for park in parks:
            var = f"{name}_{park}"
            globals()[var] = mega_dict[num][park]

    total_A, total_B, total_C, total_D = total["A"], total["B"], total["C"], total["D"]
    total_E, total_F, total_G = total["E"], total["F"], total["G"]
    total_H, total_I = total["H"], total["I"]
    total_5, total_6, total_7, total_8 = total[5], total[6], total[7], total[8]
    total_9, total_10, total_11 = total[9], total[10], total[11]
    total_12, total_13, total_14 = total[12], total[13], total[14]
    total_15, total_16, total_17 = total[15], total[16], total[17]
    total_18, total_19, total_20 = total[18], total[19], total[20]
    total_21, total_22 = total[21], total[22]

    context = {
        'five_A': five_A, 'five_B': five_B, 'five_C': five_C,
        'five_D': five_D, 'five_E': five_E, 'five_F': five_F,
        'five_G': five_G, 'five_H': five_H, 'five_I': five_I,
        'six_A': six_A, 'six_B': six_B, 'six_C': six_C,
        'six_D': six_D, 'six_E': six_E, 'six_F': six_F,
        'six_G': six_G, 'six_H': six_H, 'six_I': six_I,
        'seven_A': seven_A, 'seven_B': seven_B, 'seven_C': seven_C,
        'seven_D': seven_D, 'seven_E': seven_E, 'seven_F': seven_F,
        'seven_G': seven_G, 'seven_H': seven_H, 'seven_I': seven_I,
        'eight_A': eight_A, 'eight_B': eight_B, 'eight_C': eight_C,
        'eight_D': eight_D, 'eight_E': eight_E, 'eight_F': eight_F,
        'eight_G': eight_G, 'eight_H': eight_H, 'eight_I': eight_I,
        'nine_A': nine_A, 'nine_B': nine_B, 'nine_C': nine_C,
        'nine_D': nine_D, 'nine_E': nine_E, 'nine_F': nine_F,
        'nine_G': nine_G, 'nine_H': nine_H, 'nine_I': nine_I,
        'ten_A': ten_A, 'ten_B': ten_B, 'ten_C': ten_C,
        'ten_D': ten_D, 'ten_E': ten_E, 'ten_F': ten_F,
        'ten_G': ten_G, 'ten_H': ten_H, 'ten_I': ten_I,
        'eleven_A': eleven_A, 'eleven_B': eleven_B, 'eleven_C': eleven_C,
        'eleven_D': eleven_D, 'eleven_E': eleven_E, 'eleven_F': eleven_F,
        'eleven_G': eleven_G, 'eleven_H': eleven_H, 'eleven_I': eleven_I,
        'twelve_A': twelve_A, 'twelve_B': twelve_B, 'twelve_C': twelve_C,
        'twelve_D': twelve_D, 'twelve_E': twelve_E, 'twelve_F': twelve_F,
        'twelve_G': twelve_G, 'twelve_H': twelve_H, 'twelve_I': twelve_I,
        'thirteen_A': thirteen_A, 'thirteen_B': thirteen_B,
        'thirteen_C': thirteen_C, 'thirteen_D': thirteen_D,
        'thirteen_E': thirteen_E, 'thirteen_F': thirteen_F,
        'thirteen_G': thirteen_G, 'thirteen_H': thirteen_H,
        'thirteen_I': thirteen_I, 'fourteen_A': fourteen_A,
        'fourteen_B': fourteen_B, 'fourteen_C': fourteen_C,
        'fourteen_D': fourteen_D, 'fourteen_E': fourteen_E,
        'fourteen_F': fourteen_F, 'fourteen_G': fourteen_G,
        'fourteen_H': fourteen_H, 'fourteen_I': fourteen_I,
        'fifteen_A': fifteen_A, 'fifteen_B': fifteen_B, 'fifteen_C': fifteen_C,
        'fifteen_D': fifteen_D, 'fifteen_E': fifteen_E, 'fifteen_F': fifteen_F,
        'fifteen_G': fifteen_G, 'fifteen_H': fifteen_H, 'fifteen_I': fifteen_I,
        'sixteen_A': sixteen_A, 'sixteen_B': sixteen_B, 'sixteen_C': sixteen_C,
        'sixteen_D': sixteen_D, 'sixteen_E': sixteen_E, 'sixteen_F': sixteen_F,
        'sixteen_G': sixteen_G, 'sixteen_H': sixteen_H, 'sixteen_I': sixteen_I,
        'seventeen_A': seventeen_A, 'seventeen_B': seventeen_B,
        'seventeen_C': seventeen_C, 'seventeen_D': seventeen_D,
        'seventeen_E': seventeen_E, 'seventeen_F': seventeen_F,
        'seventeen_G': seventeen_G, 'seventeen_H': seventeen_H,
        'seventeen_I': seventeen_I, 'eighteen_A': eighteen_A,
        'eighteen_B': eighteen_B, 'eighteen_C': eighteen_C,
        'eighteen_D': eighteen_D, 'eighteen_E': eighteen_E,
        'eighteen_F': eighteen_F, 'eighteen_G': eighteen_G,
        'eighteen_H': eighteen_H, 'eighteen_I': eighteen_I,
        'nineteen_A': nineteen_A, 'nineteen_B': nineteen_B,
        'nineteen_C': nineteen_C, 'nineteen_D': nineteen_D,
        'nineteen_E': nineteen_E, 'nineteen_F': nineteen_F,
        'nineteen_G': nineteen_G, 'nineteen_H': nineteen_H,
        'nineteen_I': nineteen_I, 'twenty_A': twenty_A, 'twenty_B': twenty_B,
        'twenty_C': twenty_C, 'twenty_D': twenty_D, 'twenty_E': twenty_E,
        'twenty_F': twenty_F, 'twenty_G': twenty_G, 'twenty_H': twenty_H,
        'twenty_I': twenty_I, 'twentyone_A': twentyone_A,
        'twentyone_B': twentyone_B, 'twentyone_C': twentyone_C,
        'twentyone_D': twentyone_D, 'twentyone_E': twentyone_E,
        'twentyone_F': twentyone_F, 'twentyone_G': twentyone_G,
        'twentyone_H': twentyone_H, 'twentyone_I': twentyone_I,
        'twentytwo_A': twentytwo_A, 'twentytwo_B': twentytwo_B,
        'twentytwo_C': twentytwo_C, 'twentytwo_D': twentytwo_D,
        'twentytwo_E': twentytwo_E, 'twentytwo_F': twentytwo_F,
        'twentytwo_G': twentytwo_G, 'twentytwo_H': twentytwo_H,
        'total_5': total_5, 'total_6': total_6, 'total_7': total_7,
        'total_8': total_8, 'total_9': total_9, 'total_10': total_10,
        'total_11': total_11, 'total_12': total_12, 'total_13': total_13,
        'total_14': total_14, 'total_15': total_15, 'total_16': total_16,
        'total_17': total_17, 'total_18': total_18, 'total_19': total_19,
        'total_20': total_20, 'total_21': total_21, 'total_22': total_22,
        'total_A': total_A, 'total_B': total_B, 'total_C': total_C,
        'total_D': total_D, 'total_E': total_E, 'total_F': total_F,
        'total_G': total_G, 'total_H': total_H, 'total_I': total_I,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'JustInTime/estadistic.html', context)


# Save a new record in the database
def record(request, id_device, slot_state):
    """
    Saves a new record in the database received from the device.

    This function checks if the state of the slot has changed and if so, saves it to the database.
    If the state hasn't changed, it returns an HTTP response indicating that the state was the same.

    Args:
        request: The request object.
        id_device: The ID of the device sending the data.
        slot_state: The state of the slot (1 for True, 0 for False).

    Returns:
        An HTTP response indicating whether the record was saved or not.
    """
    if slot_state == 1:
        slot_state = True
    else:
        slot_state = False
    if DeviceState.objects.get(pk=id_device).slot_state != slot_state:
        parking_segment = DeviceState.objects.get(
            id_device=id_device).parking_segment
        device, crea = DeviceState.objects.get_or_create(id_device=id_device)
        device.slot_state = slot_state
        device.parking_segment = parking_segment
        device.save()
        DeviceHistoric.objects.create(id_device=id_device,
                                      arrive_leave=slot_state, hour_date=timezone.now(),
                                      parking_segment=parking_segment)
        total = DeviceState.objects.filter(
            parking_segment=parking_segment).count()
        active = DeviceState.objects.filter(
            parking_segment=parking_segment, slot_state=True).count()
        segment, created = SegmentState.objects.get_or_create(
            parking_segment=parking_segment)
        segment.occupied = round((active/total)*100, 2)
        segment.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("Same state")
