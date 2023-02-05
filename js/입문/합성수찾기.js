function solution(n) {
  var answer = 0;

  // 합성수를 찾아내는 공식
  function isPrime(n) {
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) return true;
    }
  }

  for (let i = 1; i <= n; i++) {
    if (isPrime(i)) answer += 1;
  }

  return answer;
}
