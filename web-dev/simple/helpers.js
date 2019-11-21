url = 'https://api.adviceslip.com/advice';
$('#main_header').on('click', function(){
    $.getJSON(url, function(data){
        set_secret_message(data.slip["advice"]);
    });

});

function set_secret_message(message){
            $('.second-paragraph').html(message);
            $('.second-paragraph').css('color', "red");
}