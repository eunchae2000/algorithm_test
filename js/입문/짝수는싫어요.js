function solution(n) {
    var answer = [];
    for (var i=1; i<=n;i++){
        if (i%2!=0){
            answer.push(i)
        }
    }
    return answer;
}