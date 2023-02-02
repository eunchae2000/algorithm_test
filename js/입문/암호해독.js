function solution(cipher, code) {
    var answer = '';
    var a = cipher.length / code
    for (var i = 1; i<=a; i++){
        answer += cipher[i*code-1]
    }
    return answer;
}