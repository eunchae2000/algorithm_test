function solution(my_string) {
    var real = my_string.replace(/[^0-9]/g, "")
    var result = []
    for (var i = 0; i<real.length; i++){
        result.push(parseInt(real[i]))
    }
    return result.sort();
}