function isCaracterInArray(caracter, array){
    for(i of array){
        if(i === caracter){
            return true;
        }
    }
    return false;
}

function disemvowel(str){
    var vowelsArr = ['a','e','i','o','u','A','E','I','O','U'];
    var aux = "";
 

    for(var i=0; i< str.length ; i++){
        if(!isCaracterInArray(str[i],vowelsArr))(aux += str[i]);
    }

    return aux;
}

/* Clever Way xDranik, ssineriz, laoris, colbydauph, Balkoth, osuushi (plus 5890 more warriors)
    function disemvowel(str) {
    return str.replace(/[aeiou]/gi, '');
    }
*/

var x = disemvowel("This website is for losers LOL!");
console.log(x);