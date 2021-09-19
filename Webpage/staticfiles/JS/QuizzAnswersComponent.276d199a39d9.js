$(document).ready(function(){
    var trueVariable = document.getElementsByName('TrueQuestion');
    var falseVariable= document.getElementsByName('FalseQuestion');

    if (trueVariable.length != 0){

        for (var i=0; i<trueVariable.length; i++){
            $(trueVariable[i]).css({'background': 'lightgreen'});
            var childsText=$(trueVariable[i]).children().eq(3);
            childsText.css({'color': 'green'});
        }
    }

    if (falseVariable.length != 0){
        for (var j=0; j<falseVariable.length; j++){
            $(falseVariable[j]).css({'background': '#ffcccb'});
            var childsText=$(falseVariable[j]).children().eq(3);
            childsText.css({'color': 'red'});
       }

    }

  

   $("input[type='radio']").click(function(){
       return false;
   });

   $(".firstQuestion").css({'position': 'absolute','top': '17%'});
   $(".secondQuestion").css({'position':'absolute', 'top': '104%'});
   $(".thirdQuestion").css({'position':'absolute', 'top': '190%'});
   $(".fourthQuestion").css({'position': 'absolute', 'top': '276%'});
   $("#buttonReturn").css({'position':'absolute', 'top': '368%'});

   

});

