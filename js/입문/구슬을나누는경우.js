function solution(balls, share) {
    return factorial(balls) / (factorial(balls-share) * factorial(share));
    // 팩토리얼 특징을 이용해서 전부 나누고 Math.round 함수를 이용해서 안전하게 반올림
    // Math.round(factorial(balls) / factorial(balls-share) / factorial(share))
}

function factorial(num){
    // BigInt => Number보다 안정적으로 더 큰 수를 저장할 수 있음
    let result = BigInt(1)
    for(let i=num; i>=2; i--){
        result *= BigInt(i)
    }
    return result
}