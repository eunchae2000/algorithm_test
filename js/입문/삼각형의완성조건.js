function solution(sides) {
    let an_1 = [];
    let max_sides = Math.max(...sides)
    let min_sides = Math.min(...sides)
    for(let i=max_sides-min_sides+1; i<=max_sides; i++){
        an_1.push(i)
    }
    for(let j=max_sides+1; j<max_sides+min_sides; j++){
        an_1.push(j)
    }

    return an_1.length;
}