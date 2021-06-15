function Contact() {
    document.getElementById("card").style.display = "block";
}

function Contact() {
    document.getElementById("card").style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    let modal = document.getElementById('card');
    if (event.target == modal) {
        closeForm();
    }
}