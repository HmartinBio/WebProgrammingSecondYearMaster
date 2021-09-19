$(document).ready(function(){
    $(".signin").on("click", function(event){
        event.preventDefault();
        $("body").append("<div class = 'bodyofPage'></div>");
        $(".bodyofPage").css({'opacity': '0.5'});
        $(".header").css({'opacity': '0.5'});
        $(".footer").css({'opacity': '0.5'});
        $(".home-title").css({'opacity': '0.5'});
        $("body").append("<div class ='pageShapeLogin'></div>");
        $("body").append("<img src='/static/images/logo.png' class = 'logoleftLogin'>");
        $('.logoleftLogin').css({'position': 'absolute', 'height': '11%', 'width': '10%', 'left': '44.7%', 'top': '27%', 'z-index': '2'});
        
        $(".formul").load("MiniQuizz/login", function(){
            $(".formul label[for='id_username']").css({'position': 'absolute', 'left': '37.5%', 'top': '42.3%', 'z-index': '2'});
            $(".formul input[type='text']").css({'position': 'absolute', 'left': '42.5%', 'top': '42.1%', 'z-index': '2'});
            $(".formul label[for='id_password'").css({'position': 'absolute', 'left': '37.5%', 'top': '50.4%', 'z-index': '2'});
            $(".formul input[type='password']").css({'position': 'absolute', 'left': '42.5%', 'top': '50%', 'z-index': '2'});
            $(".formul button[type='submit']").css({'position': 'absolute', 'left': '37.5%', 'top': '61.5%', 'z-index': '2'});
            $(".first-picture").css({'opacity': '0.5'});
            $(".title-first-picture").css({'opacity': '0.5'});
            $(".third-picture").css({'opacity': '0.5'});
            $(".title-third-picture").css({'opacity': '0.5'});
        });
        
    });

    $(".register").on("click", function(event){
        event.preventDefault();
        $("body").append("<div class = 'bodyofPage'></div>");
        $(".bodyofPage").css({'opacity': '0.5'});
        $(".header").css({'opacity': '0.5'});
        $(".footer").css({'opacity': '0.5'});
        $(".home-title").css({'opacity': '0.5'});
        $("body").append("<div class ='pageShapeRegister'></div>");
        $("body").append("<img src='/static/images/logo.png' class = 'logoleftRegister'>");
        $('.logoleftRegister').css({'position': 'absolute', 'height': '11%', 'width': '10%', 'left': '46.4%', 'top': '22%', 'z-index': '1'});
        $(".first-picture").css({'opacity': '0.5'});
        $(".title-first-picture").css({'opacity': '0.5'});
        $(".third-picture").css({'opacity': '0.5'});
        $(".title-third-picture").css({'opacity': '0.5'});

        $(".formul").load("MiniQuizz/SignUp", function(){
            $(".formul label[for='id_name']").css({'position': 'absolute', 'left': '37%', 'top': '36.7%', 'z-index': '2'});
            $(".formul input[name='name']").css({'position': 'absolute', 'left': '43%', 'top': '36.2%', 'z-index': '2'});
            $(".formul label[for='id_surname']").css({'position': 'absolute', 'left': '37%', 'top': '41.5%', 'z-index': '2'});
            $(".formul input[name='surname']").css({'position': 'absolute', 'left': '43%', 'top': '41.1%', 'z-index': '2'});
            $(".formul label[for='id_username'").css({'position': 'absolute', 'left': '37%', 'top': '46.8%', 'z-index': '2'});
            $(".formul input[name='username']").css({'position': 'absolute', 'left': '43%', 'top': '46.5%', 'z-index': '2'});
            $(".formul label[for='id_mailAddress']").css({'position': 'absolute', 'left': '37%', 'top': '52.5%', 'z-index': '2'});
            $(".formul input[name='mailAddress']").css({'position': 'absolute', 'left': '43%', 'top': '52%', 'z-index': '2'});
            $(".formul label[for='id_password']").css({'position': 'absolute', 'left': '37%', 'top': '58%', 'z-index': '2'});
            $(".formul input[name='password'").css({'position': 'absolute', 'left': '43%', 'top': '57.5%', 'z-index': '2'});
            $(".formul button[type='submit']").css({'position': 'absolute', 'left': '37%', 'top': '67%', 'z-index': '2'});
            $(".formul input[name='password']").attr('type', 'password');
        });
   
    });

    
    $(".first-picture").on("click", function(event){
        event.preventDefault();
        $("body").append("<div class = 'bodyofPage'></div>");
        $(".bodyofPage").css({'opacity': '0.5'});
        $(".header").css({'opacity': '0.5'});
        $(".footer").css({'opacity': '0.5'});
        $(".home-title").css({'opacity': '0.5'});
        $("body").append("<div class ='pageShapeRegister'></div>");
        $("body").append("<img src='/static/images/logo.png' class = 'logoleftRegister'>");
        $('.logoleftRegister').css({'position': 'absolute', 'height': '11%', 'width': '10%', 'left': '46.4%', 'top': '22%', 'z-index': '1'});
        $(".first-picture").css({'opacity': '0.5'});
        $(".title-first-picture").css({'opacity': '0.5'});
        $(".third-picture").css({'opacity': '0.5'});
        $(".title-third-picture").css({'opacity': '0.5'});

        $(".formul").load("MiniQuizz/SignUp", function(){
            $(".formul label[for='id_name']").css({'position': 'absolute', 'left': '37%', 'top': '36.7%', 'z-index': '2'});
            $(".formul input[name='name']").css({'position': 'absolute', 'left': '43%', 'top': '36.2%', 'z-index': '2'});
            $(".formul label[for='id_surname']").css({'position': 'absolute', 'left': '37%', 'top': '41.5%', 'z-index': '2'});
            $(".formul input[name='surname']").css({'position': 'absolute', 'left': '43%', 'top': '41.1%', 'z-index': '2'});
            $(".formul label[for='id_username'").css({'position': 'absolute', 'left': '37%', 'top': '46.8%', 'z-index': '2'});
            $(".formul input[name='username']").css({'position': 'absolute', 'left': '43%', 'top': '46.5%', 'z-index': '2'});
            $(".formul label[for='id_mailAddress']").css({'position': 'absolute', 'left': '37%', 'top': '52.5%', 'z-index': '2'});
            $(".formul input[name='mailAddress']").css({'position': 'absolute', 'left': '43%', 'top': '52%', 'z-index': '2'});
            $(".formul label[for='id_password']").css({'position': 'absolute', 'left': '37%', 'top': '58%', 'z-index': '2'});
            $(".formul input[name='password'").css({'position': 'absolute', 'left': '43%', 'top': '57.5%', 'z-index': '2'});
            $(".formul button[type='submit']").css({'position': 'absolute', 'left': '37%', 'top': '67%', 'z-index': '2'});
            $(".formul input[name='password']").attr('type', 'password');
        });
   
    });

    $(".title-first-picture").on("click", function(event){
        event.preventDefault();
        $("body").append("<div class = 'bodyofPage'></div>");
        $(".bodyofPage").css({'opacity': '0.5'});
        $(".header").css({'opacity': '0.5'});
        $(".footer").css({'opacity': '0.5'});
        $(".home-title").css({'opacity': '0.5'});
        $("body").append("<div class ='pageShapeRegister'></div>");
        $("body").append("<img src='/static/images/logo.png' class = 'logoleftRegister'>");
        $('.logoleftRegister').css({'position': 'absolute', 'height': '11%', 'width': '10%', 'left': '46.4%', 'top': '22%', 'z-index': '1'});
        $(".first-picture").css({'opacity': '0.5'});
        $(".title-first-picture").css({'opacity': '0.5'});
        $(".third-picture").css({'opacity': '0.5'});
        $(".title-third-picture").css({'opacity': '0.5'});

        $(".formul").load("MiniQuizz/SignUp", function(){
            $(".formul label[for='id_name']").css({'position': 'absolute', 'left': '37%', 'top': '36.7%', 'z-index': '2'});
            $(".formul input[name='name']").css({'position': 'absolute', 'left': '43%', 'top': '36.2%', 'z-index': '2'});
            $(".formul label[for='id_surname']").css({'position': 'absolute', 'left': '37%', 'top': '41.5%', 'z-index': '2'});
            $(".formul input[name='surname']").css({'position': 'absolute', 'left': '43%', 'top': '41.1%', 'z-index': '2'});
            $(".formul label[for='id_username'").css({'position': 'absolute', 'left': '37%', 'top': '46.8%', 'z-index': '2'});
            $(".formul input[name='username']").css({'position': 'absolute', 'left': '43%', 'top': '46.5%', 'z-index': '2'});
            $(".formul label[for='id_mailAddress']").css({'position': 'absolute', 'left': '37%', 'top': '52.5%', 'z-index': '2'});
            $(".formul input[name='mailAddress']").css({'position': 'absolute', 'left': '43%', 'top': '52%', 'z-index': '2'});
            $(".formul label[for='id_password']").css({'position': 'absolute', 'left': '37%', 'top': '58%', 'z-index': '2'});
            $(".formul input[name='password'").css({'position': 'absolute', 'left': '43%', 'top': '57.5%', 'z-index': '2'});
            $(".formul button[type='submit']").css({'position': 'absolute', 'left': '37%', 'top': '67%', 'z-index': '2'});
            $(".formul input[name='password']").attr('type', 'password');
        });
   
    });



});

