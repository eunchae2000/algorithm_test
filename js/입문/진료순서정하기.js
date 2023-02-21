function solution(emergency) {
    var answer = emergency.slice().sort((a, b) => b-a); // 내림차순으로 정렬하고 새로운 변수 answer에 배열 저장
    return emergency.map(v => answer.indexOf(v)+1);
}