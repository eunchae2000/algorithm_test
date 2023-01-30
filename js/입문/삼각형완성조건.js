function solution(sides) {
    const max = Math.max(sides)
    const re_sides = sides.pop(max)

    if(re_sides[0]+re_sides[1] == max){ 
        return 2
    }
    else if (re_sides[0]+re_sides[1] < max){
        return 2
    }
    else{
        return 1
    }
}