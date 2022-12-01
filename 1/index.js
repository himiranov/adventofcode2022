const fs = require('fs')

fs.readFile('input.txt', (err, buf) => {
    const data = buf.toString();
    // part 1
    let maxCaloriesSum = 0;
    let currentCaloriesSum = 0;
    for (let calories of data.split('\n')) {
        if (calories === '') {
            if (currentCaloriesSum > maxCaloriesSum) {
                maxCaloriesSum = currentCaloriesSum;
            }
            currentCaloriesSum = 0;
            continue;
        }
        currentCaloriesSum += parseInt(calories, 10);
    }
    console.log(maxCaloriesSum);

    // part 2
    const allCaloriesSums = [];
    for (let calories of data.split('\n')) {
        if (calories === '') {
            allCaloriesSums.push(currentCaloriesSum);
            currentCaloriesSum = 0;
            continue;
        }
        currentCaloriesSum += parseInt(calories, 10);
    }
    let theBiggestCaloriesSum = 0; 
    allCaloriesSums.sort((a, b) => b - a).slice(0, 3).forEach((calories) => theBiggestCaloriesSum += calories);
    console.log(theBiggestCaloriesSum);
});
