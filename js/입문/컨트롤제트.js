function solution(s) {
    var answer = 0;
    let ss = []
    let s_string = s.split(" ")
    for(let i=0; i<s_string.length; i++){
        if(s_string[i] === 'Z'){
            ss.pop(s_string[-1])
        }
        else{
            ss.push(s_string[i])
        }
    }

    for(let j=0; j<ss.length; j++){
        answer += Number(ss[j])
    }
    return answer;
}