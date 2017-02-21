
var date = new Date();
var currentDate = date.getDate()+"" + "/" + date.getMonth()+"" + "/" + date.getFullYear();
$('#get-current-date').html(currentDate);

$('.message.form').hide();

$('#first-add').click(function(){
    $('.empty.billboard').hide();
    $('.add-button-div').hide();
    $('.message.form').show();
});

$('#add').click(function(){
    $('.empty.billboard').hide();
    $('.add-button-div').hide();
    $('.message.form').show();
});

$('#send-form').click(function(){
    $('.message.form').hide();
    $('.add-button-div').show();
});

$('#close-form').click(function(){
    $('.message.form').hide();
    $('.add-button-div').show();
    $('.empty.billboard').show();
});
