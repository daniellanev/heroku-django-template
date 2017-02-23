
// if (request.user.is_authenticated()){

// var logged = JSON.parse(xmlhttp.responseText); // don't use eval
// if(logged.user_logged){   
    
//  if(!isset($_SESSION['loggedin'])){   

// {% if message_list %}
// {% for message in message_list %}


// <fieldset class="previous message">
// 	<legend class="legend">{{message.date.day}}/{{message.date.month}}/{{message.date.year}}</legend>
//     <div class="title">{{message.title}}</div>
//     <div class="text">{{message.text}}</div>
//     <div class="author">{{message.author}}</div>
// </fieldset>

// {% endfor %}

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
// }

// $('#create-message-form').on('submit', function(e){
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url: 'add_message',
//         data: {
//             title: $('#title').val(),
//             text: $('#text').val(),
//             author: $('#author').val(),
        
//         },
//         succes: function(){
//             alert('it worked');
//         }

//     });
// });


// function add_message() {
//     console.log("create post is working!") // sanity check
//     $.ajax({
//         url : "'add_message'/", // the endpoint
//         type : "POST", // http method
//         data: {
//             title: $('#title').val(),
//             text: $('#text').val(),
//             author: $('#author').val(),
//         },
//         succes: function(){
//             alert('it worked');
//         }
//     });
// };

// $('#create-message-form').on('submit', function(e){
//     e.preventDefault();
//     add_message();
// });

