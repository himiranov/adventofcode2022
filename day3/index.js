const fs = require('fs')


const getRowsFromData = (data) => {
    const rows = data.split('\n');
    if (rows[rows.length - 1] === '') {
        return rows.slice(0, rows.length - 1);
    }
    return rows;
}


const getScoreByChar = (char) => {
    const charCode = char.charCodeAt(0);
    if (charCode < 91) {
        // upper case
        return charCode - 38;
    }
    // lower case
    return charCode - 96;
}


const solveFirst = () => {
    let scoresSum = 0;
    for (let row of rows) {
        const firstRucksack = row.slice(0, row.length / 2);
        const secondRucksack = row.slice(row.length / 2, row.length);
        for (let char of firstRucksack) {
            if (secondRucksack.includes(char)) {
                scoresSum += getScoreByChar(char);
                break;
            }
        }
    }
    console.log(scoresSum);
};


const solveSecond = () => {
    let scoresSum = 0;
    for (let i = 0; i < rows.length; i += 3) {
        const firstRucksack = rows[i];
        const secondRucksack = rows[i + 1];
        const thirdRucksack = rows[i + 2];
        for (let char of firstRucksack) {
            if (secondRucksack.includes(char) && thirdRucksack.includes(char)) {
                scoresSum += getScoreByChar(char);
                break;
            }
        }
    }
    console.log(scoresSum);
};


const buf = fs.readFileSync('input.txt');
const data = buf.toString();
const rows = getRowsFromData(data);
// ------------------
solveFirst();
// ------------------
solveSecond();
