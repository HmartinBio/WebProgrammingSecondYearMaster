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
   
    $("table[name='tableAnswers']").css({'position': 'absolute',
        'top': '17%'});
    
    $("#score").css({'position': 'absolute', 'left': '90%'});

    $("#descriptionQuestion1").css({'font-weight': 'bold'});
    $("#descriptionQuestion2").css({'font-weight': 'bold'});
    $("#descriptionQuestion3").css({'font-weight': 'bold'});
    $("#descriptionQuestion4").css({'font-weight': 'bold'});

});

