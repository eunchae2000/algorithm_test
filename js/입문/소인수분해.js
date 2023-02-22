function solution(n) {
  var answer = [];
  let i = 2;
  while (n !== 1) {
    if (n % i == 0) {
      answer.push(i);
      n /= i;
    } else {
      i += 1;
    }
  }
  // 중복을 제거하고 오름차순으로 정렬
  return Array.from(new Set(answer.sort((a, b) => a - b)));
}
