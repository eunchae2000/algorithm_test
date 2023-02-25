function solution(n) {
    var answer = 0;
    for(i=0; i<n; i++){
        answer ++;
        // 3의 배수인 경우와 숫자에 3이 포함된 경우를 모두 고려
        while(answer%3 === 0 || answer.toString().includes('3')){
            answer ++;
        }
    }
    return answer;
}