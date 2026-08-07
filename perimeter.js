function calculatePerimeter() {

    let length = Number(document.getElementById("length").value);
    let width = Number(document.getElementById("width").value);

    let perimeter = 2 * (length + width);

    document.getElementById("result").textContent =
        "Perimeter: " + perimeter;
}