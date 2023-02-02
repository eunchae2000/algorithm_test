function solution(my_string, num1, num2) {
  var answer = [...my_string];

  // splice 특정 요소를 삭제하거나 바꿀때
  // (인덱스, 삭제 또는 변경 요소 개수, 바꿀 문자)
  answer.splice(num1, 1, my_string[num2]);
  answer.splice(num2, 1, my_string[num1]);
  return answer.join("");
}
