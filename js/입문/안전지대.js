function solution(board) {
    var answer = 0;

    for(let i=0; i<board.length; i++){
        for(let j=0; j<board[i].length; j++){
            if(board[i][j] === 1) {
                // 폭탄을 기준으로 주위에 있는 8곳이 위험지역
                // board의 값이 1인 경우 상하좌우 대각선을 0인 경우 2로 바꿈
                // 상하 좌우를 2로 변경하되 이는 해당 칸이 0인 경우에만 해당
                // 맨 윗줄이 아닌 경우
                if(i !== 0 && board[i-1][j] !== 1) {
                    board[i-1][j] = 2    
                }
                // 맨 아랫줄이 아닌 경우
                if(i !== board.length-1 && board[i+1][j] !== 1) {
                    board[i+1][j] = 2
                }
                // 맨 왼쪽이 아닌 경우
                if(j !== 0 && board[i][j-1] !== 1) {
                    board[i][j-1] = 2
                }
                // 맨 오른쪽이 아닌 경우
                if(j !== board[i].length-1 && board[i][j+1] !== 1) {
                    board[i][j+1] = 2
                }
                // 맨 대각선 윗 왼쪽이 아닌 경우
                if(i !== 0 && j !== 0 && board[i-1][j-1] !== 1) {
                    board[i-1][j-1] = 2
                }
                // 맨 대각선 윗 오른쪽이 아닌 경우
                if(i !== 0 && j !== board[i].length-1 && board[i-1][j+1] !== 1) {
                    board[i-1][j+1] = 2
                }
                // 맨 대각선 아랫 왼쪽이 아닌 경우
                if(i !== board.length-1 && j !== 0 && board[i+1][j-1] !== 1) {
                    board[i+1][j-1] = 2
                }
                // 맨 대각선 아랫 오른쪽이 아닌 경우
                if(i !== board.length-1 && j !== board[i].length-1 && board[i+1][j+1] !== 1) {
                    board[i+1][j+1] = 2
                }
            }
        }
    }
    board.forEach(a => a.forEach(b =>b===0? answer++ : null));
    return answer;
}