function solution(money) {
    var answer = [];
    var a = parseInt(money/5500);
    var b = money % 5500;
    answer.push(a, b)
    return answer;
}