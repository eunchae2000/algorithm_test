function solution(score) {
    let avg = score.map(v => (v[0]+v[1])/2);
    let avg_sort = avg.slice().sort((a,b) => b-a);
    return avg.map(v => avg_sort.indexOf(v) + 1)
}
