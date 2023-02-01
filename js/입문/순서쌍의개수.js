// function solution(n) {
//     var answer = 0;
//     for (var i = 0; i<=n; i++){
//         for (var j = 0; j<=n; j++){
//             if(i*j == n){
//                 answer += 1
//             }
//         }
//     }
//     return answer;
// }

function solution(n) {
    var answer = 0;
    for (var i = 1; i<=n; i++){
        if(n%i==0){
            answer+=1
        }
    }
    return answer;
}