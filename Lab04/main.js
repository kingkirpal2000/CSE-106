class Calculator {
    constructor() {
        this.firstNum = 0;
        this.secondNum = 0;
        this.operand = "";
        this.containsDec = false;
        this.decimalsF = 0;
        this.decimalsS = 0;

    }
}

var calc = new Calculator();

function displayController(num){
    if(calc.containsDec == true){
        decimalConverter(num);
    } else if(calc.operand == ""){
        calc.firstNum = calc.firstNum * 10;
        calc.firstNum = calc.firstNum + num;
        document.getElementById("result").value = (calc.firstNum);
    } else {
        calc.secondNum = calc.secondNum * 10;
        calc.secondNum = calc.secondNum + num;
        document.getElementById("result").value = (calc.secondNum);
    }
}

function selectDivision() {
    calc.operand = "/";
    calc.containsDec = false;
    document.getElementById("result").value = "/";
}

function selectMult() {
    calc.operand = "*";
    calc.containsDec = false;
    document.getElementById("result").value = "*";
}

function selectSum() {
    calc.operand = "+";
    calc.containsDec = false;
    document.getElementById("result").value = "+";
}

function selectSubtract() {
    calc.operand = "-";
    calc.containsDec = false;
    document.getElementById("result").value = "-";
}

function decimalConverter(num) {
        if(calc.operand == ""){
            calc.decimalsF = calc.decimalsF * 10;
            calc.decimalsF = calc.decimalsF + num;
            calc.containsDec = true;
            document.getElementById("result").value = `${calc.firstNum}.${calc.decimalsF}`;
        } else {
            calc.decimalsS = calc.decimalsS * 10;
            calc.decimalsS = calc.decimalsS + num;
            calc.containsDec = true;
            document.getElementById("result").value = `${calc.secondNum}.${calc.decimalsS}`;
        }


}

function equateCalc() {

    while(calc.decimalsF / 10 >= 0.1){
        calc.decimalsF = calc.decimalsF / 10;
    }
    calc.firstNum = calc.firstNum + calc.decimalsF;

    while(calc.decimalsS / 10 >= 0.1){

        calc.decimalsS = calc.decimalsS / 10;
    }
    calc.secondNum = calc.secondNum + calc.decimalsS;


    if(calc.operand == "/") {
        document.getElementById("result").value = calc.firstNum / calc.secondNum;
    } else if (calc.operand == "*") {
        document.getElementById("result").value = calc.firstNum * calc.secondNum;
    } else if (calc.operand == "+") {
        document.getElementById("result").value = calc.firstNum + calc.secondNum;
    } else if (calc.operand == "-") {
        document.getElementById("result").value = calc.firstNum - calc.secondNum;
    } else {
        document.getElementById("result").value = calc.firstNum;
    }

}

function clearScreen() {
    calc.firstNum = 0;
    calc.secondNum = 0;
    calc.operand = "";
    calc.containsDec = false;
    calc.decimalsF = 0;
    calc.decimalsS = 0;
    document.getElementById("result").value = "";
}





