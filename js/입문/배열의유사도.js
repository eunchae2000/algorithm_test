// function solution(s1, s2) {
//     var answer = 0;
//     for(var i =0; i<s1.length; i++){
//         for (var j = 0; j<s2.length; i++){
//             if(s1[i] == s2[j]){
//                 answer += 1
//             }
//         }
//     }
//     return answer;
// }

function solution(s1, s2) {
    // 1. filter : s1에도 s 요소가 있다면 배열에 추가하고 길이를 결과로 반환
    // 2. includes : s2 배열이 가지고 있는 요소를 s로 지정
    return s1.filter(s => s2.includes(s)).length;
  }