function solution(my_string) {
    const arr = my_string.split("")
    // Set => 중복제거
    // 자바스크립트에서 중복을 제거하기 위해서는 Set 메소드를 사용해야 함
    // Array.from => 배열을 초기화
    const result_arr = Array.from(new Set(arr))
    return result_arr.join('');
}