const fs = require('fs')


const getRowsFromData = (data) => {
    const rows = data.split('\n');
    if (rows[rows.length - 1] === '') {
        return rows.slice(0, rows.length - 1);
    }
    return rows;
}


const checkIsInRange = (min, max, number) => {
    return (number >= min && number <= max);
}


const solveFirst = () => {
    const containsSum = rows.reduce((acc, row) => {
        const [range1, range2] = row.split(',');
        const [start1, end1 ] = range1.split('-').map((n) => parseInt(n, 10));
        const [start2, end2 ] = range2.split('-').map((n) => parseInt(n, 10));
        if (
            (checkIsInRange(start1, end1, start2) && checkIsInRange(start1, end1, end2)) ||
            (checkIsInRange(start2, end2, start1) && checkIsInRange(start2, end2, end1))
        ) {
            acc += 1;
        }
        return acc;
    }, 0);
    console.log(containsSum)
};


const solveSecond = () => {
    const containsSum = rows.reduce((acc, row) => {
        const [range1, range2] = row.split(',');
        const [start1, end1 ] = range1.split('-').map((n) => parseInt(n, 10));
        const [start2, end2 ] = range2.split('-').map((n) => parseInt(n, 10));
        if (
            checkIsInRange(start1, end1, start2) ||
            checkIsInRange(start1, end1, end2) ||
            checkIsInRange(start2, end2, start1) ||
            checkIsInRange(start2, end2, end1)
        ) {
            acc += 1;
        }
        return acc;
    }, 0);
    console.log(containsSum)
};


const buf = fs.readFileSync('input.txt');
const data = buf.toString();
const rows = getRowsFromData(data);
// ------------------
solveFirst();
// ------------------
solveSecond();
