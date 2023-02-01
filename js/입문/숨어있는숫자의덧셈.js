function solution(my_string) {
    var answer = 0;
    var str = String(my_string.replace(/[^0-9]/g,''));
    for (var i = 0; i<str.length; i++){
        answer += parseInt(str[i])
    }
    return answer;
}