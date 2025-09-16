document.querySelector("#load").addEventListener("click", loadTodos);

async function loadTodos() {
    let url = "https://jsonplaceholder.typicode.com/todos";
    let response = await fetch(url);
    let data = await response.json();
    let completedTodos = data.filter(function(item) {
        return item.completed === true;
    });

    let html = completedTodos.map(function(item) {
        return "<li>" + item.id + " " + item.title + "</li>";
    });

    document.querySelector("#list").insertAdjacentHTML("afterbegin", html.join(" "));
}