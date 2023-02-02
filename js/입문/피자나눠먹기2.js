function solution(n) {
    while(true){
        let pizza = 1;
        if(pizza*6 % n == 0){
            break
        }else{
            pizza += 2
        }
    }
    return pizza*6;
}