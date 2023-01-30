function solution(n, k) {
    var answer = 0;
    if (n>=10){
        // 양꼬치를 먹고 받을 수 있는 서비스 음료수 개수
        var y = parseInt(n/10)
        var j = k-y
        answer = (n*12000) + (j*2000)
    }
    else{
        answer = (n*12000) + (k*2000)
    }
    return answer;
}