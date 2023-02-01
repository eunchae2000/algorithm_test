function solution(array) {
    var arr = array.sort((a, b) => a-b)
    var mid = parseInt(arr.length/2)
    return arr[mid];
}