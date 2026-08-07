const today = new Date();

const days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
];

const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
];

document.getElementById("day").textContent =
    days[today.getDay()];

document.getElementById("date").textContent =
    today.getDate();

document.getElementById("monthYear").textContent =
    months[today.getMonth()] + " " + today.getFullYear();