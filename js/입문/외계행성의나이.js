function solution(age) {
  var agestr = String(age).split("");
  let result = "";
  for (let i = 0; i < agestr.length; i++) {
    // Number : 문자열 숫자를 int형으로 변환
    // +97을 한 이유는 소문자로 출력하기 위해서
    result += String.fromCharCode(Number(agestr[i]) + 97);
  }
  return result;
}
