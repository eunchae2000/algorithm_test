function solution(babbling){
    var answer = 0;
    let baby = ["aya", "ye", "woo", "ma"]
    for(let i in babbling){
        let result = babbling[i];
        for (let j in baby){
            if(babbling[i].includes(baby[j])){
                result = result.replace(baby[j], 'X')
            }
        }
        result = result.replace(/X/gi, '');
        if(result.length === 0){
            answer++;
        }
    }
    return answer
}

// const regex = /^(aya|ye|woo|ma)+$/;

//   babbling.forEach(word => {
//     if (regex.test(word)) answer++;  
//   })