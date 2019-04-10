import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';

import '@fullcalendar/core/main.css';
import '@fullcalendar/daygrid/main.css';
// import '@fullcalendar/timegrid/main.css';
// import '@fullcalendar/list/main.css';

import $ from 'jquery';
const csrftoken = $("[name=csrfmiddlewaretoken]").val();
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
document.addEventListener('DOMContentLoaded', function() {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });
  
  const calendarEl = document.getElementById('calendar');

  const calendar = new Calendar(calendarEl, {
    events: '/schedule/api/occurrences?calendar_slug=pugsley',
    plugins: [ dayGridPlugin ],
    defaultView: 'dayGridMonth'
  });
  
  calendar.render();
});