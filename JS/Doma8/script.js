function User(name, age, job) {
    this.name = name;
    this.age = age;
    this.job = job;

    this.who = function() {
        return `Я ${this.name} мне ${this.age} лет. Я работаю ${this.job}ом.`;
    };
}

let User1 = new User('Дмитрий', 26, 'Дизайнер');
let User2 = new User('Станислав', 29, 'Программист');
let User3 = new User('Сергей', 35, 'Менеджер');
let output = document.getElementById('output');

output.innerHTML += `<p>${User1.who()}</p>`;
output.innerHTML += `<p>${User2.who()}</p>`;
output.innerHTML += `<p>${User3.who()}</p>`;
