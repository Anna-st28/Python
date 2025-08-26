let choose = document.querySelector('input[type="button"]');

choose.addEventListener('click', chooseMystery);

function chooseMystery(){
    const answers = {
        a: "Санки",
        b: "Снег",
        c: "Морковь",
        d: "Снежинка",
        e: "Волк"
    };

    const selectedOption = document.querySelector('input[name="radio2"]:checked');

    const answer = answers[selectedOption.value];
    alert(answer);
};