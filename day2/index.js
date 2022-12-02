const fs = require('fs')

fs.readFile('input.txt', (err, buf) => {
    const data = buf.toString();

    const SCORE_MAP = {
        A: 1,
        B: 2,
        C: 3,
        X: 1,
        Y: 2,
        Z: 3
    };
    const LOSE_SCORE = 0;
    const DRAW_SCORE = 3;
    const WIN_SCORE = 6;
    // part 1
    let yourSumScore = 0;
    for (let strategy of data.split('\n')) {
        const [opponent, you] = strategy.split(' ');
        if (!opponent || !you) {
            break;
        }
        const opponentScore = SCORE_MAP[opponent];
        const yourScore = SCORE_MAP[you];
        const diff = yourScore - opponentScore; 
        if (diff === 0) {
            yourSumScore += yourScore + DRAW_SCORE;
        } else if (diff === 1 || diff === -2) {
            yourSumScore += yourScore + WIN_SCORE;
        } else {
            yourSumScore += yourScore + LOSE_SCORE;
        }
    }
    console.log(yourSumScore);
    // part 2
    const CHAR_TO_ACTION = {
        X: LOSE_SCORE,
        Y: DRAW_SCORE,
        Z: WIN_SCORE
    }
    let yourSumScorePart2 = 0;
    for (let strategy of data.split('\n')) {
        const [opponent, you] = strategy.split(' ');
        if (!opponent || !you) {
            break;
        }
        const opponentScore = SCORE_MAP[opponent];
        const yourAction = CHAR_TO_ACTION[you];
        let yourScore;
        if (yourAction === LOSE_SCORE) {
            yourScore = opponentScore === 1 ? 3 : opponentScore - 1;
        } else if (yourAction === DRAW_SCORE) {
            yourScore = opponentScore;
        } else {
            yourScore = opponentScore === 3 ? 1 : opponentScore + 1;
        }
        yourSumScorePart2 += yourScore + yourAction;
    }
    console.log(yourSumScorePart2);
});
