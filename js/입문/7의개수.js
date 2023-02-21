function solution(array) {
  var answer = array.join();
  var a = 0;
  for (let i = 0; i <= answer.length; i++) {
    if (answer[i] === 7) {
      a += 1;
    }
  }
  return a;
}
