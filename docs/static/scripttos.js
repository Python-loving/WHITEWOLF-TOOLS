let min = 0;
let max = 1;
let ok = document.getElementById("allo");
let btn = document.querySelector(".btn");
let popup = document.getElementById("popup");
let open = document.getElementById("open");
let close = document.getElementById("close");
let pooop = document.querySelector(".popup-content");
let txt = document.querySelector(".txt")
const mousmoov = document.querySelector(".mousmoov")

let random = Math.floor(Math.random() * (max - min + 1)) + min;

if (random == 1) {
    ok.innerHTML = "WHITE - WOLF TOOLS | TOS";
    // setInterval(() => {
    //     let randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
    //     ok.style.color = randomColor;
    // }, 1000);
} else {
    ok.innerHTML = "TOS - WHITE WOLF TOOLS";
    // setInterval(() => {
    //     let randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
    //     ok.style.color = randomColor;
    // }, 1000);
}

setInterval(() => {
    let randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
    txt.style.borderColor = randomColor;
}, 1000);

btn.addEventListener("click", function (e) {
    window.location.href = "index.html"
})


open.addEventListener("click", function () {
    popup.style.display = "flex";
    pooop.style.backgroundColor = "black";
});

window.onload = function () {
    document.getElementById("popup").style.display = "flex";
    pooop.style.backgroundColor = "black"
};

close.addEventListener("click", function () {
    popup.style.display = "none";
});