// ======================================
// SIMPLE CALCULATOR OPEARATIONS
// ======================================
function addNum(n1, n2) {
    return n1 + n2;
}

function subtractNum(n1, n2) {
    return n1 - n2;
}

function multiplyNum(n1, n2) {
    return n1 * n2;
}

function divideNum(n1, n2) {
    return n2 !== 0 ? n1 / n2 : "Cannot divide by zero";
}
const operations = {"+":addNum,"-":subtractNum,"*":multiplyNum,"/": divideNum }


// Declaration  Variables in javascript
let current_user;
//  Definition of Variables in javascript
current_user = "Oluwaseun";
const age = 27;

// Declaration and Definition of Function in JavaScript
function calculator() {
    let num1 = parseFloat(prompt("What is your first number?"));
    console.log("Available operations:", Object.keys(operations).join(" "));
    let shouldContinue = true;
    while (shouldContinue) {
        let operatorSymbol = prompt("Pick an operation from the line above: ");
        let num2 = parseFloat(prompt("What is your next number?"));

        if (operations[operatorSymbol]) {
            let usersOperationFunction = operations[operatorSymbol];
            let answer = usersOperationFunction(num1, num2);
            console.log(`${num1} ${operatorSymbol} ${num2} = ${answer}`);
            let continueCalculation = prompt(`Type 'y' to continue calculating with ${answer}, or type 'n' to start a new calculation:`);
            
            if (continueCalculation.toLowerCase() === 'y') {
                num1 = answer;
            } else {
                shouldContinue = false;
                calculator();
            }
        } else {
            console.log("Invalid operator. Please try again.");
        }
    }
}

calculator();
