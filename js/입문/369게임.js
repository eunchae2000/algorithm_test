function solution(order) {
    var answer = 0;
    let order_str = String(order)
    for(let i=0; i<order_str.length; i++){
        if(Number(order_str[i]) == 3){
            answer += 1
        }else if(Number(order_str[i]) == 6){
            answer += 1
        }else if(Number(order_str[i]) == 9){
            answer += 1
        }
    }
    return answer;
}