// function solution(sides) {
//     const max = Math.max(sides)
//     const re_sides = sides.pop(max)
//     var answer = 0;

//     if(re_sides[0]+re_sides[1] <= max){ 
//         answer = 2;
//     }
//     else if (re_sides[0]+re_sides[1] > max){
//         answer = 1;
//     }
//     else{
//         answer = 2;
//     }

//     return answer
// }

function solution(sides) {
    const max = Math.max(...sides);
    // reduce 함수 => 하나의 반환값을 가지며 모든 조건을 전부 실행한 뒤 조건에 맞는 하나의 결과를 반환
    return max < sides.reduce((a, c) => a + c, 0) - max ? 1 : 2;
}