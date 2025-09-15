let form = document.form1;

let message = {
    loading: "Загрузка",
    success: "Спасибо! Скоро мы с вами свяжемся",
    failure: "Что-то пошло не так.."
};

form.addEventListener("submit", event => {
    event.preventDefault();

    let msg = document.createElement("div");
    msg.textContent = message.loading;
    form.append(msg);

    let request = new XMLHttpRequest();
    request.open("POST", "server.php");

    let formData = new FormData(form);
    request.send(formData);

    request.addEventListener("load", function(){
        if(request.status === 200){
            console.log(request.response);
            msg.textContent = message.success;

            document.getElementById("myModal").style.display = "block";
        } else {
            msg.textContent = message.failure;
        }
        form.reset();
        setTimeout(() => msg.remove(), 3000);
    });
});

let modal = document.getElementById("myModal");
let span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
