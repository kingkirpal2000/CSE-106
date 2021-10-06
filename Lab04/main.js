class Calculator {
    constructor() {
        this.firstNum = 0;
        this.secondNum = 0;
        this.operand = "";
        this.ntc = false;
    }
}

var calc = new Calculator();


function displayController(num) {
    if(!(num == "." && document.getElementById("result").value.includes("."))){
        document.getElementById("result").value += num;
    }

}

function selectDivision() {
    document.getElementById("division").style.backgroundColor = "red";
    document.getElementById("subtract").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("add").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("multiply").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    calc.firstNum = eval(document.getElementById("result").value);
    if(calc.ntc == false){
        calc.operand = "/";
        document.getElementById("result").value = ""
    } else {
        equateCalc()
    }

}
function selectSubtract() {
    document.getElementById("subtract").style.backgroundColor = "red";
    document.getElementById("add").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("multiply").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("division").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    calc.firstNum = eval(document.getElementById("result").value);
    if(calc.ntc == false){
        calc.operand = "-";
        document.getElementById("result").value = ""
    } else {
        equateCalc()
    }
}
function selectSum() {
    document.getElementById("add").style.backgroundColor = "red";
    document.getElementById("multiply").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("division").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("subtract").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    calc.firstNum = eval(document.getElementById("result").value);
    if(calc.ntc == false){
        calc.operand = "+";
        document.getElementById("result").value = ""
    } else {
        equateCalc()
    }
}
function selectMult() {
    document.getElementById("multiply").style.backgroundColor = "red";
    document.getElementById("subtract").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("add").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("division").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    calc.firstNum = eval(document.getElementById("result").value);
    if(calc.ntc == false){
        calc.operand = "*";
        document.getElementById("result").value = ""
    } else {
        equateCalc()
    }
}
function clearScreen(){
    calc.firstNum = 0;
    calc.operand = "";
    calc.secondNum = 0;
    calc.ntc = false;
    document.getElementById("result").value = ""
    document.getElementById("subtract").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("add").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("multiply").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
    document.getElementById("division").style.backgroundColor = 'rgb(' + 40 + ',' + 181 + ',' + 224 + ')';
}

function equateCalc() {
    if(calc.ntc == false){
        calc.secondNum = eval(document.getElementById("result").value);
        calc.ntc = true;
    }

    if(calc.operand == "/"){
        document.getElementById("result").value = calc.firstNum / calc.secondNum;
        calc.firstNum = eval(document.getElementById("result").value)
    } else if(calc.operand == "-"){
        document.getElementById("result").value = calc.firstNum - calc.secondNum;
        calc.firstNum = eval(document.getElementById("result").value)
    } else if(calc.operand == "+"){
        console.log(calc.firstNum);
        console.log(calc.secondNum);
        document.getElementById("result").value = calc.firstNum + calc.secondNum;
        calc.firstNum = eval(document.getElementById("result").value)
    } else if(calc.operand == "*"){
        document.getElementById("result").value = calc.firstNum * calc.secondNum;
        calc.firstNum = eval(document.getElementById("result").value)
    }
}




