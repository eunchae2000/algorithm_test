function solution(my_string) {
  const nums = my_string.match(/[0-9]+/g);
  // reduce > 배열의 모든 요소의 합 계산
  return nums ? nums.map((num) => Number(num)).reduce((a, c) => a + c, 0) : 0;
}
