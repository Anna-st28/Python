document.querySelector("#load").addEventListener("click", loadTodos);

async function loadTodos() {
    let url = "https://jsonplaceholder.typicode.com/todos";
    let response = await fetch(url);
    let data = await response.json();
    let completedTodos = data.filter(function(item) {
        return item.completed === true;
    });

    let html = completedTodos.map(function(item) {
        return `Пользователь: ${item.userId} выполнил задачу № ${item.id} "${item.title}"`;
    });

    document.querySelector("#list").insertAdjacentHTML("afterbegin", html.map(text => `<li>${text}</li>`).join(" "));
}