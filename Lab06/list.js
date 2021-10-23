function showStudents() {
    const xhttp= new XMLHttpRequest();
    const method = "GET";  // Could be GET, POST, PUT, DELETE, etc.
    const url= "http://127.0.0.1:5000/grades";
    const async = true;   // asynchronous (true) or synchronous (false) –don’t use synchronous
    xhttp.open(method, url, async);
    xhttp.onload= function() {
        const rep = JSON.parse(this.responseText);
        for(objs in rep){
            document.getElementById("answers").innerHTML += `<tr><td>${objs}</td><td>${rep[objs]}</td></tr>`
        }
    };

    xhttp.send();

}

showStudents();