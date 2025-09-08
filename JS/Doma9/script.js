class Header{
    constructor(img, h1){
        this.src = img;
        this.h1 = h1;
    }

    render(id){
        this.out= `
            <img src="${this.src}" alt="">
            <h1>${this.h1}</h1>
        `;

        document.querySelector(`#${id}`).innerHTML = this.out;
    }
}


let img1 = "https://img.icons8.com/?size=50&id=9489&format=png";

let header1 = new Header(img1, "Работа 24 часа в сутки, 7 дней в неделю, 365 дней в году");
header1.render("header1");

let img2 = "https://img.icons8.com/?size=80&id=116727&format=png";

let header2 = new Header(img2, "Нет географических границ");
header2.render("header2");

let img3 = "https://img.icons8.com/?size=50&id=EOgeMtw8XphP&format=png";

let header3 = new Header(img3, "Ассортимент");
header3.render("header3");

let img4 = "https://img.icons8.com/?size=48&id=ybTMXclwjSGB&format=png";

let header4 = new Header(img4, "Безопасность");
header4.render("header4");

let img5 = "https://img.icons8.com/?size=80&id=ZzRKS7CVNpXa&format=png";

let header5 = new Header(img5, "Сокращение расходов на аренду и персонал");
header5.render("header5");

let img6 = "https://img.icons8.com/?size=80&id=108638&format=png";

let header6 = new Header(img6, "Партнерские отношения");
header6.render("header6");

let img7 = "https://img.icons8.com/?size=80&id=gKMM6YI2joik&format=png";

let header7 = new Header(img7, "Покупатель всегда на связи");
header7.render("header7");

let img8 = "https://img.icons8.com/?size=80&id=ydDK3uAiZSi4&format=png";

let header8 = new Header(img8, "Комфортный выбор");
header8.render("header8");

let img9 = "https://img.icons8.com/?size=50&id=34425&format=png";

let header9 = new Header(img9, "Удобство оплаты");
header9.render("header9");