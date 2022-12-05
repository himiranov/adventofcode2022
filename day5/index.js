const fs = require('fs')


const getProceduresFromData = (data) => {
    const re = /^move (\d+) from (\d+) to (\d+)$/
    const procedures = [];

    const rows = data.split('\n');
    const proceduresRows = rows.slice(rows.indexOf(''), rows.length);
    for (let row of proceduresRows) {
        const [_, count, fromStack, toStack] = row.match(re) || [];
        if (!(fromStack && count && toStack)) {
            continue;
        }
        procedures.push({
            fromStack: parseInt(fromStack, 10) - 1,
            count: parseInt(count, 10),
            toStack: parseInt(toStack, 10) - 1
        });
    }
    return procedures;
}

const getStacksFromData = (data) => {
    const stacks = [];
    const rows = data.split('\n');
    const stackRows = rows.slice(0, rows.indexOf('') - 1).reverse();
    for (let row of stackRows) {
        let stackIndex = 0;
        let crate = '';
        let i = 0;
        let j = 0;
        while (i <= row.length) {
            if (j === 3) {
                if (crate.trim()) {
                    if (!stacks[stackIndex]) {
                        stacks[stackIndex] = [];
                    }
                    stacks[stackIndex].push(crate[1]);
                }
                crate = '';
                stackIndex += 1;
                j = 0;
                i++;
                continue;
            }
            crate += row[i];
            i++;
            j++;
        }
    }
    return stacks;
}


const solveFirst = (data) => {
    const stacks = getStacksFromData(data);
    const procedures = getProceduresFromData(data);

    for (let { fromStack, count, toStack } of procedures) {
        for (let i = 0; i < count; i++) {
            stacks[toStack].push(stacks[fromStack].pop());
        }
    }
    let result = '';
    for (let stack of stacks) {
        result += stack[stack.length - 1];
    }
    console.log(result);
};


const solveSecond = (data) => {
    const stacks = getStacksFromData(data);
    const procedures = getProceduresFromData(data);

    for (let { fromStack, count, toStack } of procedures) {
        stacks[toStack].push(...stacks[fromStack].splice(stacks[fromStack].length - count, stacks[fromStack].length));
    }
    let result = '';
    for (let stack of stacks) {
        result += stack[stack.length - 1];
    }
    console.log(result);
};


const buf = fs.readFileSync('input.txt');
const data = buf.toString();
// ------------------
solveFirst(data);
// ------------------
solveSecond(data);



