function solution(num, k) {
    var answer = 0;
    let num_str = String(num)
    for(let i =0; i<num_str.length; i++){
        if(num_str[i] == String(k)){
            answer = i+1
            break
        }else{
            answer = -1
        }
    }
    return answer;
}