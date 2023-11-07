// Делаем, чтобы максимальное значение в поле ввода даты было сегодняшней датой
const today = new Date().toISOString().split('T')[0];
document.getElementById("birth_date").setAttribute("max", today);

// 