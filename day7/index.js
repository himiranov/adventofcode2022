const fs = require('fs')


const getRowsFromData = (data) => {
    const rows = data.split('\n');
    if (rows[rows.length - 1] === '') {
        return rows.slice(0, rows.length - 1);
    }
    return rows;
}


class File {
    size = 0;
    name = '';
    
    constructor(size, name) {
        this.size = parseInt(size, 10);
        this.name = name;
    }
}


class Directory {
    size = 0;
    name = '';
    parentDirectory = null;
    subDirectories = {};
    files = [];
    
    constructor(name, parentDirectory = null) {
        this.name = name;
        this.parentDirectory = parentDirectory;
    }
}

const goToDirectoryRe = /^\$ cd (.*)$/
const subDirectoryRe = /^dir (.*)$/
const fileRe = /^(\d+) (.*)$/


const parseTree = (rows) => {
    let tree;
    let currentDirectory;
    let match;
    for (let row of rows) {
        if (row.startsWith('$ ls')) {
            continue
        }
        match = row.match(goToDirectoryRe);
        if (match) {
            const [_, dir] = match;
            if (dir === '/') {
                if (!tree) {
                    tree = new Directory(dir);
                    currentDirectory = tree;
                    continue;
                }
            } else if (dir === '..') {
                currentDirectory = currentDirectory.parentDirectory;
                continue;
            } else {
                currentDirectory = currentDirectory.subDirectories[dir];
                continue;
            }
        }
        match = row.match(subDirectoryRe);
        if (match) {
            const [_, dir] = match;
            currentDirectory.subDirectories[dir] = new Directory(dir, currentDirectory);
            continue;
        }
        match = row.match(fileRe);
        if (match) {
            const [_, fileSize, fileName] = match;
            currentDirectory.files.push(new File(fileSize, fileName));
        }
    }
    return tree;
}

const isEmpty = (obj) => !Object.keys(obj).length;


const calculateDirectorySize = (currentDirectory) => {
    let subDirectoriesSize = 0;
    if (!isEmpty(currentDirectory.subDirectories)) {
        Object.values(currentDirectory.subDirectories).forEach((directory) => {
            subDirectoriesSize += calculateDirectorySize(directory);
        })
    }
    currentDirectory.size += subDirectoriesSize;
    if (currentDirectory.files.length) {
        let size = currentDirectory.files.reduce((sum, file) => {
            sum += file.size;
            return sum;
        }, 0);
        currentDirectory.size += size;
    }
    return currentDirectory.size;
}


const solveFirst = (tree) => {
    let sum = 0;
    const calculateAtMost1000Size = (currentDirectory) => {
        if (!isEmpty(currentDirectory.subDirectories)) {
            Object.values(currentDirectory.subDirectories).forEach((directory) => {
                calculateAtMost1000Size(directory);
            })
        }
        if (currentDirectory.size <= 100000) {
            sum += currentDirectory.size;
        }
    }
    calculateAtMost1000Size(tree);
    console.log(sum)
};


const solveSecond = (tree) => {
    const spaceToClean = 30000000 - (70000000 - tree.size);
    let minSpaceToClean = tree.size;
    const calculateMinSpaceToClean = (currentDirectory) => {
        if (!isEmpty(currentDirectory.subDirectories)) {
            Object.values(currentDirectory.subDirectories).forEach((directory) => {
                calculateMinSpaceToClean(directory);
            })
        }
        if (currentDirectory.size >= spaceToClean && currentDirectory.size < minSpaceToClean) {
            minSpaceToClean = currentDirectory.size;
        }
    }
    calculateMinSpaceToClean(tree);
    console.log(minSpaceToClean);
};


const buf = fs.readFileSync('input.txt');
const data = buf.toString();
const rows = getRowsFromData(data);
const tree = parseTree(rows);
calculateDirectorySize(tree);
// ------------------
solveFirst(tree);
// ------------------
solveSecond(tree);
