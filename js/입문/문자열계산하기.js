// eval => 자바스크립트에서 String을 숫자로 계산하여 출력해주는 함수
function solution(my_string) {
  let str = my_string.split(" ");
  var answer = Number(str[0]);
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "-") {
      answer -= Number(str[i + 1]);
    } else if (str[i] === "+") {
      answer += Number(str[i + 1]);
    } else {
      continue;
    }
  }
  return answer;
}
