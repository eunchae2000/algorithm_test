function solution(my_str, n) {
  var answer = [];
  // 문자열 길이의 /n 만큼 실행
  for (let i = 0; i < my_str.length / n; i++) {
    let count = "";
    // n 길이 만큼 배열에 추가
    for (let j = i * n; j < i * n + n; j++) {
      if (my_str[j]) {
        count += my_str[j];
      } else {
        break;
      }
    }
    answer.push(count);
  }
  return answer;
}
