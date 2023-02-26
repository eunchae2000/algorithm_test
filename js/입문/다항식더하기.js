function solution(polynomial) {
    // split을 이용해 공백+공백을 제거하여 배열을 생성
    const arr = polynomial.split(" + ")
    let xNum = 0;
    let num = 0;
    
    // 배열의 요소에 x가 존재하면 x를 제거하고 제거했을 경우 없어진다면 1로 반환  
    for(let i=0; i<arr.length; i++){
        if(arr[i].includes('x')){
            let strValue = arr[i].replace('x', '') || "1";
            // x가 있는 합
            xNum += parseInt(strValue, 10);
        }else{
            // 자연수의 합
            num += parseInt(arr[i])
        }
    }
    var answer = [];
    // 백틱을 사용해서 삼항연산자 구현
    if (xNum) answer.push(`${xNum === 1 ? "" : xNum}x`);
    if (num) answer.push(num);
     // 배열을 join() 메서드를 이용해 +를 넣어 문자열로 만들고 반환한다.
    return answer.join(" + ");
}