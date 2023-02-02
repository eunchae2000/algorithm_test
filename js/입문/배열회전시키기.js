function solution(numbers, direction) {
    var answer = numbers
    if(direction == 'right'){
        var number = numbers.pop()
        numbers.unshift(number)
        return numbers
    }else{
        var number = numbers.shift()
        numbers.push(number)
        return numbers
    }
    return answer
}