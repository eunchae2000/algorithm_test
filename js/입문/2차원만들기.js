function solution(num_list, n) {
  var answer = [];
  // slice 내장 함수는 index를 통해 배열을 자르고 자른 배열을 return
  // 첫번째 인자로 자르기 시작하는 index를 받고, 두 번째 인자로 어디 index 전까지 자를지 해당 index를 넣어줌\

  for (let i = 0; i < num_list.length / n; i++) {
    answer.push(num_list.slice(i * n, i * n + n));
  }
  return answer;
}
