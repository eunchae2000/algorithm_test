function solution(numbers, k) {
    let idx = 1;
    for(let i=0; i<k-1; i++){
        idx += 2;
        if(idx > numbers.length){
            idx -= numbers.length
        }
    }
    return idx
}