const fs = require('fs')

fs.readFile('../Words_list/Pokemon_volume_4.txt', (err, data) => {
    if (err) throw err;

    console.log(data.toString());
})

const quote = document.getElementById("text");
const author = document.getElementById("author");

generateQuote();

function generateQuote(){
  quote.innerHTML = quote_list[Math.floor(Math.random() * quote_list.length)] ;
  author.innerHTML = "Konata Izumi"
  setRandomColor();
}

function getRandomColor() {
  let letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function setRandomColor() {
  let newColor = getRandomColor()
  document.body.style.backgroundColor = newColor;
  document.body.style.color = newColor;
}
