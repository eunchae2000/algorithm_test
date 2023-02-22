function solution(numbers) {
    let en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
    for(let i=0; i<en.length; i++){
        numbers = numbers.split(en[i]).join(i)
    }
    return Number(numbers)
}