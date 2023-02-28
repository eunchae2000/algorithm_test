function solution(num, total) {
    var answer = [];
    // 소수로 나올 경우 시작 수를 크게 잡아야 하기 때문에 ceil을 이용하여 반올림
    var n = Math.ceil((total/num)-Math.floor(num/2))
    for(let i=n; i<n+num; i++){
        answer.push(i)
    }
    return answer;
}