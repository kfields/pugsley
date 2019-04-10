from django.shortcuts import render
from django.http import JsonResponse

def calendar(request):
    return render(request, 'schedule/calendar.html')

def api_events(request):
    data = [
      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-03-16T13:00:00"
      },
      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-04-20T13:00:00"
      },

      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-05-18T13:00:00"
      },
      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-06-15T13:00:00"
      },
      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-07-20T13:00:00"
      },
      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-08-17T13:00:00"
      },
      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-09-21T13:00:00"
      },
        {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-10-19T13:00:00"
      },
        {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-11-16T13:00:00"
      },
      {
        "title": "EMPUG Monthly",
        "url": "https://www.meetup.com/empugdotorg/",
        "start": "2019-21-16T13:00:00"
      },
      {
        "title": "Christmas",
        "backgroundColor": "red",
        "start": "2019-12-25"
      },
      {
        "title": "Spring",
        "backgroundColor": "red",
        "start": "2019-03-20"
      },
      {
        "title": "Summer",
        "backgroundColor": "red",
        "start": "2019-06-21"
      },
      {
        "title": "Independence Day",
        "backgroundColor": "red",
        "start": "2019-07-04"
      }
    ]

    return JsonResponse(data, safe=False)
