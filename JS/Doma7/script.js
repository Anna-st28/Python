let but = document.querySelector('input[type="button"]');
but.addEventListener("click", smsUser);

function smsUser(){
    let sms = document.querySelector("textarea").value;
    let name = document.querySelector('input[type="text"]').value;
    let regExpBBMail = /([\w.]+@[\w.]+\.[a-z]{2,3})/ig;
    sms = sms.replace(regExpBBMail, "<span style='color: red'>$1</span>");
    let form = document.querySelector("form");
    form.insertAdjacentHTML("beforeend", `<fieldset>
            <legend>${name}</legend>
            <div>${sms}</div>
        </fieldset>`)
    }