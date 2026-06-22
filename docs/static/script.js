let sombre = 1;
let icon = document.getElementById("change");
let retour = document.querySelector(".return");
const sombre_id = document.getElementById("light");
const mode = document.querySelector(".mode");

if (sombre == 1) {
    console.log("Le site est en sombre");
} else {
    console.log("Le site est en light mode");
}

sombre_id.addEventListener("click", function () {

    if (sombre == 1) {
        mode.style.backgroundColor = "gray";
        mode.style.color = "black";
        sombre_id.style.backgroundColor = "white";
        sombre_id.style.color = "black";
        retour.style.color = "black"
        retour.style.backgroundColor = "white"
        icon.textContent = "light_mode";
        sombre = 0;
    } else {
        mode.style.backgroundColor = "black";
        mode.style.color = "white";
        sombre_id.style.backgroundColor = "black";
        sombre_id.style.color = "white";
        retour.style.color = "white"
        retour.style.backgroundColor = "black"
        icon.textContent = "brightness_2";
        sombre = 1;
    }
});

retour.addEventListener("click", function () {
    window.location.href = "index.html";
})