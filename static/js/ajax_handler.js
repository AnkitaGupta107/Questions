function do_ajax(ajax_object){
    var request = $.ajax({
        type:ajax_object.type,
        data:ajax_object.data,
        url:ajax_object.url
    });
    request.done(function(response,textStatus,jqXHR){
        if(ajax_object.hasOwnProperty('console_done_msg'))
            console.log(ajax_object.console_done_msg+response);

        if(response['status']==200){
            if(ajax_object.hasOwnProperty('done_callback')){
        ajax_object.done_callback(response);
            }
            else if(response.hasOwnProperty('alert_msg')){
                alert(response.alert_msg);
            }


        }
        else{
            if(ajax_object.hasOwnProperty('error_callback')){
                ajax_object.error_callback(response);
            }
            else{
                if(response.hasOwnProperty('error_msg')){
                    alert(response.error_msg);
                    if(response.hasOwnProperty('reset_key')){
                        location.reload();
                    }
                }
                else
                alert('Not server error but validation problem');
            }
        }

        });

        request.fail(function(jqXHR,textStatus,errorThrown){
            console.error(
                "The following error occured: "+
                    textStatus, errorThrown
            );
            if(ajax_object.hasOwnProperty('fail_callback'))
            ajax_object.error_callback(jqXHR,errorThrown);
        });

}

function object_from_form(jform){
    var paramObj = {};
$.each(jform.serializeArray(), function(_, kv) {
  if (paramObj.hasOwnProperty(kv.name)) {
    paramObj[kv.name] = $.makeArray(paramObj[kv.name]);
    paramObj[kv.name].push(kv.value);
  }
  else {
    paramObj[kv.name] = kv.value;
  }
});
    return paramObj;
}
