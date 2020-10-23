var isSquare = function(n){
    for(var i=0; i<n+1;i++){
        aux = i*i;
        if( aux === n ){
        return true;
        } 
        else if(aux > n){
        return false;
        }
    }
    return false;
}


console.log(isSquare(25));