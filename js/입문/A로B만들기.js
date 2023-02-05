function solution(before, after) {
    let all = 0;

    // 각 문자열을 정렬
    before = [...before].sort()
    after = [...after].sort()
    for(let i=0; i<before.length; i++){
        if(before[i] == after[i]){
            all += 1;
        }
    }
    if(before.length == all){
        return 1
    }else{
        return 0
    }
}