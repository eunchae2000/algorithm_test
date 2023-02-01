function solution(numbers) {
    // 내림차순 정렬, 원본 배열 수정
    let array = numbers.sort((a,b) => b-a)
    // 오름차순 정렬, 원본 배열 수정
    // let array = numbers.sort((a,b) => a-b)
    
    return array[0]*array[1];
}