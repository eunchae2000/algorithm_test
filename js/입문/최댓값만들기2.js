function solution(numbers) {
    let answer = numbers[0] * numbers[1];
    for (let i = 0; i < numbers.length - 1; i++) {
        const one = numbers[i];
        for (let j = i + 1; j < numbers.length; j++) {
            const two = numbers[j];
            if (answer < one * two) {
                answer = one * two;
            }
        }
    }
    return answer;
}