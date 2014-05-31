$(document).ready(function(){
   $('#form').on('submit',function(event){
       event.preventDefault();
        var ajax_object = {};
        ajax_object.data = object_from_form($(this));
        ajax_object.data.ajax = 'true';
        ajax_object.type = 'post';
        ajax_object.url = location.href;
        ajax_object.done_callback= function(response){
            if(response.hasOwnProperty('alert_message')){
                alert(response.alert_message);
            }
            location.pathname='/signin/';
        };
        do_ajax(ajax_object);
   });
});
