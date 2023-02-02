function solution(array) {
    var answer = [];
    var m = Math.max(...array)
    answer.push(m)
    var i = array.indexOf(m)
    answer.push(i)
    return answer;
}