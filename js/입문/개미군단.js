function solution(hp) {
    var five = parseInt(Math.floor(hp/5));
    var three = parseInt(Math.floor(hp-five*5)/3);
    var one = hp-five*5-three*3;
    return five + three + one;
}