function solution(array, n) {
  // 편차가 같을 경우 먼저 계산한 요소를 return 하기 위해서 정렬
  var array = array.sort();
  var answer = 0;
  var abs = 0;
  var min = 100;
  for (let i = 0; i < array.length; i++) {
    abs = array[i] - n < 0 ? -(array[i] - n) : array[i] - n;
    if (abs < min) {
      min = abs;
      answer = array[i];
    }
  }
  return answer;
}
