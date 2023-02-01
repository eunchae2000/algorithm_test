function solution(my_string, n) {
  var answer = "";
  for (var i = 0; i < my_string.length; i++) {
    // repeat => 문자열을 n만큼 반복하는 함수
    answer += my_string[i].repeat(n);
  }
  return answer;
}
