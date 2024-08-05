function toggleMode() {
    const body = document.body;

    // Toggle the dark-mode class
    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        localStorage.setItem('dark-mode', 'disabled');
    } else {
        body.classList.add('dark-mode');
        localStorage.setItem('dark-mode', 'enabled');
    }
}

// Apply the saved mode preference on page load
document.addEventListener('DOMContentLoaded', function() {
    if (localStorage.getItem('dark-mode') === 'enabled') {
        document.body.classList.add('dark-mode');
    }
});
window.addEventListener('scroll',reveal);
function reveal(){
var reveals = document.querySelectorAll('.reveal')
for (var i=0; i<reveals.length; i++){
var windowheight = window.innerHeight;
var revealtop = reveals[i].getBoundingClientRect().top;
var revealpoint = 150;
if(revealtop<windowheight - revealpoint){
  reveals[i].classList.add('active');
}
else{
  reveals[i].classList.remove('active');
}
}
}
function phone_links(){
    var o = document.getElementById('open_bar');
    var x = document.getElementById("close_bar");
    var l = document.getElementById("phone_links");
    if (l.style.display === "none"){
        l.style.display = "block";
        o.style.display = "none";
        x.style.display = "block";
    }
    else{
        l.style.display = "none";
        o.style.display = "block";
        x.style.display = "none";
    }
}
window.setTimeout(function() {
    document.querySelectorAll('.alert').forEach(function(alert) {
        alert.style.display = 'none';
    });
}, 5000);
 
function hireme(){
    var h = document.getElementById('hire_me_text');
    var c = document.getElementById("laugh");
    if(h.style.display === "block" || h.style.display === ""){
        h.style.display="none"
        c.style.display
    }
    else{
        h.style.display = "none"
    }
}