from django.shortcuts import render
from django.http import JsonResponse

def calendar(request):
    return render(request, 'schedule/calendar.html')

def api_events(request):
    data = [
      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        'rrule': {
          'freq': 'monthly',
          'byweekday': [ 'sa' ],
          'bysetpos': [3],
          'dtstart': '2019-04-20T13:00:00',
        },

        # for specifying the end time of each instance
        'duration': '02:00'
      },
      {
        "title": "Christmas",
        "backgroundColor": "#00FFFF",
        "start": "2019-12-25"
      },
      {
        "title": "Spring",
        "backgroundColor": "white",
        "start": "2019-03-20"
      },
      {
        "title": "Summer",
        "backgroundColor": "white",
        "start": "2019-06-21"
      },
      {
        "title": "Independence Day",
        "backgroundColor": "red",
        "start": "2019-07-04"
      }
    ]

    return JsonResponse(data, safe=False)
