function solution(dots) {
  var answer = 0;

  function result(a, b, c, d) {
    let resultA, resultB;
    resultA = (b[1] - a[1]) / (b[0] - a[0]);
    resultB = (d[1] - c[1]) / (d[0] - c[0]);

    // 평행인 경우 answer 카운트
    if (resultA === resultB) answer++;
  }

  // 평행이 될 수 있는 모든 경우를 고려
  result(dots[0], dots[1], dots[2], dots[3]);
  result(dots[0], dots[2], dots[1], dots[3]);
  result(dots[0], dots[3], dots[1], dots[2]);

  return answer > 0 ? 1 : 0;
}
