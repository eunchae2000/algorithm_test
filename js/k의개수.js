function solution(i, j, k) {
    var answer = 0;
    for(var a=i; a<=j; a++){
        if(String(a).length > 1){
            for(var b in String(a)){
                if(String(a)[b].includes(String(k))){
                    answer += 1;
                }
            }
        }else{
            if(String(a).includes(String(k))){
                answer+=1
            }
        }
    }
    return answer;
}
