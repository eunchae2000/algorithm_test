function solution(box, n) {
    var a = parseInt(box[0]/n)
    var b = parseInt(box[1]/n)
    var c = parseInt(box[2]/n)
    return a*b*c;
}