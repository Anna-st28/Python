let months = [ "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август",
  "Сентябрь", "Октябрь", "Ноябрь", "Декабрь" ];

function getRandomColor() {
  let letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

for (let i = 0; i < months.length; i++) {
  let monthName = months[i];
  let bgColor = getRandomColor();
  let divHTML = `<div style="text-align:center; background-color: ${bgColor}; padding: 12px; margin: 5px;">${monthName}</div>`;
  document.writeln(divHTML);
}