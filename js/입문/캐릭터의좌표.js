// 비트연산자를 사용하는 방법도 있음
function solution(keyinput, board) {
    const limitX = (board[0] - 1) / 2
    const limitY = (board[1] - 1) / 2
  
    const key = {
      up: [0, 1],
      down: [0, -1],
      left: [-1, 0],
      right: [1, 0],
    }
  
    let x = 0
    let y = 0
  
    keyinput.forEach((command) => {
      const [dx, dy] = key[command]
      const nx = x + dx
      const ny = y + dy
      if (Math.abs(nx) <= limitX && Math.abs(ny) <= limitY) {
        x = nx
        y = ny
      }
    })
  
    return [x, y]
  }