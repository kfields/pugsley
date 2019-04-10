import 'bootstrap';

import './scss/app.scss';
import { library, dom } from "@fortawesome/fontawesome-svg-core";
/*
import { faSearch, faUserCircle} from "@fortawesome/free-solid-svg-icons";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
library.add(faSearch, faUserCircle, faGithub);

*/
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'

// Add all icons to the library so you can use it in your page
library.add(fas, far, fab)

dom.watch();

/**
 * setup JQuery's AJAX methods to setup CSRF token in the request before sending it off.
 * http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
 */
import $ from 'jquery'
function getCookie(name)
{
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});