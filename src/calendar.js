import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';

import '@fullcalendar/core/main.css';
import '@fullcalendar/daygrid/main.css';
// import '@fullcalendar/timegrid/main.css';
// import '@fullcalendar/list/main.css';

document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');

  const calendar = new Calendar(calendarEl, {
    // events: '/schedule/api/occurrences?calendar_slug=pugsley',
    events: '/schedule/api/events',
    plugins: [ dayGridPlugin ],
    defaultView: 'dayGridMonth'
  });
  
  calendar.render();
});