let showButton = document.getElementById('showButton');
let hideButton = document.getElementById('hideButton');
let birdImage = document.getElementById('birdImage');

showButton.addEventListener('click', () => {
    birdImage.style.display = 'block';
});

hideButton.addEventListener('click', () => {
    birdImage.style.display = 'none';
});
