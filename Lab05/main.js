function searchStudent() {
    let val = document.getElementById("name").value;
    let nArr = val.split(" ");

    var urlName = "";
    for(let i = 0; i < nArr.length; i++){
        urlName += nArr[i];
        if(i != nArr.length-1){
            urlName += "%20";
        }
    }

    const xhttp= new XMLHttpRequest();
    const method = "GET";  // Could be GET, POST, PUT, DELETE, etc.
    const url= "https://amhep.pythonanywhere.com/grades/" + urlName;
    const async = true;   // asynchronous (true) or synchronous (false) –don’t use synchronous
    xhttp.open(method, url, async);
    xhttp.onload= function() {
        if(xhttp.status != 404){
            const rep = JSON.parse(this.responseText);
            document.getElementById("reply1").innerHTML= "GRADE: " + rep[val];

        } else {
            document.getElementById("reply1").innerHTML = "Student Not Found"
        }

    };

    xhttp.send();
}

function createStudent() {
    let nameVal = document.getElementById("nameNewStudent").value;
    let gradeVal = document.getElementById("gradeNewStudent").value;
    const payload = {
        name : nameVal,
        grade: eval(gradeVal)
    }
    const url = "https://amhep.pythonanywhere.com/grades"
    var xhttp= new XMLHttpRequest();
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload= function() {
        const rep = JSON.parse(this.responseText);
        document.getElementById("reply2").innerHTML=  "CREATED " + nameVal + " " + rep[nameVal];
    };
    xhttp.send(JSON.stringify(payload));
}