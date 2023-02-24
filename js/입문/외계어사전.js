function solution(spell, dic) {
    spell = spell.sort().join("");
    console.log(spell)
    return dic.map(a => a.split().sort().join("")).find(a => a === spell) === undefined ? 2 : 1
}

console.log(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
