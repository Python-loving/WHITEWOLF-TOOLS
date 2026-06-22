let min = 0;
let max = 1;
let ok = document.getElementById("allo");
let btn = document.querySelector(".btn")

let random = Math.floor(Math.random() * (max - min + 1)) + min;

if (random == 1) {
    ok.innerHTML = "WHITE - WOLF TOOLS | TOS";
    setInterval(() => {
        let randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
        ok.style.color = randomColor;
    }, 1000);
} else {
    ok.innerHTML = "TOS - WHITE WOLF TOOLS";
    setInterval(() => {
        let randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
        ok.style.color = randomColor;
    }, 1000);
}

btn.addEventListener("click", function (e) {
    window.location.href = "index.html"
})
