function solution(A, B) {
    let answer_A = [...A]
    for(let i=0; i<A.length; i++){
        let count = i;
        if(A === B){
            return count;
        }else{
            answer_A.unshift(answer_A.pop())
            if(answer_A.join('') === B)
            return i+1
        }
    }
    return -1
}

// 다른 사람 풀이 
// B 문자열을 두 번 반복해서 A가 있으면 A의 index를 출력
// let solution1 = (a,b) => (b+b).indexOf(a)