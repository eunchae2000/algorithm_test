function solution(a, b) {
    while(b%2===0) b/= 2
    while(b%5===0) b/= 5
    if(b%a===0)b/= a
    return b === 1 ? 1: 2
}

// function solution(a, b) {
//     // a를 b로 나눈 수를 소수점 아래 10의 자리만큼 표기한 후 Number 타입으로 변환한다.
//     // 이때 변환한 값과 a를 b로 나눈 수가 같다면 유한소수이므로 1,
//     // 아니라면 무한소수이므로 2를 리턴한다.
//   return Number((a/b).toFixed(10)) == a/b ? 1 : 2
// }

console.log(solution(7, 20))
console.log(solution(11, 22))
console.log(solution(12, 21))