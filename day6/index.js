const fs = require('fs')


const getRowsFromData = (data) => {
    const rows = data.split('\n');
    if (rows[rows.length - 1] === '') {
        return rows.slice(0, rows.length - 1);
    }
    return rows;
}


const getNextIndexAfterUniqueSubStrInRow = (row, uniqueSubStrLength) => {
    let subStr = '';
    let i = 0;
    for (let char of row) {
        i++;
        const index = subStr.indexOf(char)
        if (index !== -1) {
            subStr = subStr.slice(index + 1, subStr.length) + char
            continue;
        }
        subStr += char;
        if (subStr.length === uniqueSubStrLength) {
            break;
        }
    }
    return i;
}


const solveFirst = (rows) => {
    const row = rows[0];
    const index = getNextIndexAfterUniqueSubStrInRow(row, 4);
    console.log(index);
};


const solveSecond = (rows) => {
    const row = rows[0];
    const index = getNextIndexAfterUniqueSubStrInRow(row, 14);
    console.log(index);
};


const buf = fs.readFileSync('example.txt');
const data = buf.toString();
const rows = getRowsFromData(data);
// ------------------
solveFirst(rows);
// ------------------
solveSecond(rows);



