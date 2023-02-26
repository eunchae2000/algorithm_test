function solution(quiz) {
    var answer = [];
    var quiz_arr = [];
    var result = 0;
    for(let i=0; i<quiz.length; i++){
        quiz_arr = quiz[i].split(" ");
        
        if(quiz_arr[1] === '-'){
            result = Number(quiz_arr[0])-Number(quiz_arr[2])
            if(result === Number(quiz_arr[4])){
                answer.push('O')
            }else{
                answer.push('X')
            }
        }else{
            result = Number(quiz_arr[0])+Number(quiz_arr[2])
            if(result === Number(quiz_arr[4])){
                answer.push('O')
            }else{
                answer.push('X')
            }
        }
    }
    return answer;
}

console.log(solution(["3 - 4 = -3", "5 + 6 = 11"]))