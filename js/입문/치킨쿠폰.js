function solution(chicken) {
    var answer = 0;
    while(chicken>=10){
        // 주문할 수 있는 치킨의 개수
        answer += Math.floor(chicken/10)
        // 주문하면서 생긴 쿠폰의 개수와 주문할 때 사용한 쿠폰의 나머지 쿠폰
        chicken = chicken%10 + Math.floor(chicken/10);
    }
    return answer;
}