let purchaseAmount = prompt("Введите стоимость покупки:");
purchaseAmount = parseFloat(purchaseAmount);

if (isNaN(purchaseAmount)) {
  alert("Введено некорректное значение. Пожалуйста, введите число.");
} else {

  let discount = 0;

  if (purchaseAmount > 1000) {
    discount = 5;
  } else if (purchaseAmount > 500) {
    discount = 3;
  }

  let discountAmount = purchaseAmount * (discount / 100);
  let finalAmount = purchaseAmount - discountAmount;

  alert(
    "Стоимость покупки без скидки: " +
      purchaseAmount +
      " руб\n" +
      "Скидка: " +
      discount +
      "%\n" +
      "Итоговая стоимость: " +
      finalAmount +
      " руб"
  );
}