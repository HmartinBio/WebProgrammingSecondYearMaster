$(document).ready(function(){

    $("#username").css({'left': '88%', 
    'overflow': 'hidden',
    'text-overflow': 'ellipsis'});

    $(".quizz").css({'left': '22%'});

    $(".title-first-picture").css({'left': '5.5%'});
    
    $(".first-picture").mouseenter(function(){
        $(".title-first-picture").css({'text-decoration': 'underline'});
    });


    $(".first-picture").mouseleave(function(){
        $(".title-first-picture").css({'text-decoration': 'none'});

    });

    $(".second-picture").mouseenter(function(){
        $(".title-second-picture").css({'text-decoration': 'underline'});

    });

    $(".second-picture").mouseleave(function(){
        $(".title-second-picture").css({'text-decoration': 'none'});

    });

    $(".third-picture").mouseenter(function(){
        $(".title-third-picture").css({'text-decoration': 'underline'});

    });


    $(".third-picture").mouseleave(function(){
        $(".title-third-picture").css({'text-decoration': 'none'});

    });




});