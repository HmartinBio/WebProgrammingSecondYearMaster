$(document).ready(function(){
    
    $("table[name='tableImages']").css({'position': 'absolute', 'top': '13%'});
    $("span[name='Description']").css({'font-weight': 'bold'});
    $("span[name='Microscopy']").css({'font-weight': 'bold'});
    $("span[name='Cell_type']").css({'font-weight': 'bold'});
    $("span[name='Component']").css({'font-weight': 'bold'});
    $("span[name='doi']").css({'font-weight': 'bold'});
    $("span[name='Organism']").css({'font-weight': 'bold'});
    $(".header").css({'position': 'absolute', 'left': '0%'});
    $(".home").css({'position': 'absolute', 'top': '400%'});
    $(".register").css({'position': 'absolute', 'top': '400%'});
    $(".signin").css({'position': 'absolute', 'top': '400%'});
    $(".quizz").css({'position': 'absolute', 'top': '400%', 
        'left': '22%'});
    $("#username").css({'position': 'absolute', 'top': '390%', 
        'overflow': 'hidden','text-overflow': 'ellipsis', 
        'left': '88%'});
    $("#score").css({'position': 'absolute', 'top': '700%'});
    $(".logout").css({'position': 'absolute', 'top': '400%'});
    $(".footer").css({'display': 'none'});
});