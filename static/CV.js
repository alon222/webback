console.log("alon klayman")
console.log("אלון קליימן")


function myFunction() {
const inpObj1 = document.getElementById("id1");
const inpObj2 = document.getElementById("id2");
console.log('inpObj1')
if (!inpObj1.checkValidity() && !inpObj2.checkValidity()) {
document.getElementById("demo").innerHTML = inpObj1.validationMessage + " "+ inpObj2.validationMessage;
} 
else {
document.getElementById("demo").innerHTML = "תודה רבה הפרטים נשלחו";
}
}

var i = 0;
var b=0;
var txt = 'hey my name is alon and im web developer';
var speed = 50;

function typeWriter() {

    if (i < txt.length) {
        document.getElementById("typing").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
      }
}