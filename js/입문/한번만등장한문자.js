function solution(s) {
  var dict = {};
  s.split("").forEach((a) =>
    dict[a] !== undefined ? (dict[a] += 1) : (dict[a] = 1)
  );
  // entries: key, value 값을 하나로 합쳐 배열로 만들어준다.
  return Object.entries(dict)
    .map((a) => (a[1] === 1 ? a[0] : null))
    .filter((a) => a !== null)
    .sort()
    .join("");
}
