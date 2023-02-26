function solution(numer1, denom1, numer2, denom2) {
    var answer = 1;
    var denom = denom1*denom2
    var numer = numer1*denom2 + numer2*denom1
    for(let i=1; i<=denom; i++){
        if(denom%i == 0 && numer%i == 0){
            answer = i
        }
    }
    return [numer/answer, denom/answer];
}