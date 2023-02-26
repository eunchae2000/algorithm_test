function solution(array) {
    // 배열의 요소가 하나뿐이라면 그 값 그대로 return
    if(array.length === 1) return array[0];

    var obj = {};
    var answer = [];
    array.forEach(n => {
        // obj 객체를 이용해서 array의 배열 요소들이 obj에 존재하면 더하기 1, 없으면 1을 넣어줌
        obj[n] = ++obj[n] || 1;
    });

    // 객체는 key와 value가 묶어져 있기 때문에 for in 문
    for (let key in obj) {
        answer.push([key, obj[key]]);
    }

    // obj를 담은 answer 배열을 내림차순으로 정렬
    answer.sort((a, b) => b[1] - a[1]);

    // 최빈값이 동일한 요소가 있으면 return -1을 하고 없으면 최빈값 요소 반환, 객체 값으로 반환되기 때문에 정수로 바꾸어줘야함
    if(answer.length === 1) return Number(answer[0][0])
    else if (answer[0][1] === answer[1][1]) return -1;
    return Number(answer[0][0])
}
