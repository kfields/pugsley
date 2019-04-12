import rrulePlugin from '@fullcalendar/rrule';

import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';

import '@fullcalendar/core/main.css';
import '@fullcalendar/daygrid/main.css';

document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');

  const calendar = new Calendar(calendarEl, {
    events: '/schedule/api/events',
    plugins: [ rrulePlugin, dayGridPlugin ],
    defaultView: 'dayGridMonth'
  });
  
  calendar.render();
});