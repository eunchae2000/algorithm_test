function solution(my_string) {
  let my_str = my_string.toLowerCase();
  return my_str.split("").sort().reverse().join("");
}
