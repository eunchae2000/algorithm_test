function solution(n) {
    // 제곱근 판별하는 방식
    var sqrt = Math.sqrt(n);
    if(sqrt % 1 !== 0){
        return 2
    }else{
        return 1
    }
}