function solution(common) {
    if(common[1]-common[0] === common[2]-common[1]){
        // 배열의 마지막 요소와 덧셈
        return common.pop()+(common[1]-common[0])
    }else{
        // 배열의 마지막 요소와 곱셉
        return common.pop()*(common[1]/common[0])
    }
}