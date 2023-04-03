const quote_list = [
  "I had a feeling I saw a girl in a sailor uniform with a machine gun walk by.",
  "When you learn something from Tsukasa, it feels like you\’ve really failed.",
  "Raise your hand if you thought of something naughty!",
  "Sounds like a lot of work, I think I\’ll pass. I\’d rather play and I\’ll ask for help when I get stuck.",
  "And the TV show ended by saying how young people are becoming increasingly illiterate, but doesn\’t browsing the Internet and blogging actually improve your literacy?",
  "How come you wear glasses? I mean, you\’re really pretty but you can only appeal to a tiny section of the fanbase.",
  "I wanted to see your homework from the other day. And I got to see your face while you were sleeping… so don\’t sweat it.","A great man once said that UFO catchers are like savings account.",
  "Tsukasa, don`t interfere in my punchline.",
  "I\’m actually concentrating really hard on not falling asleep but sensei … they still come … the demons of sleep … with no warning, no way to defend .. a full-out Attack!",
  "There\’s a difference between the flu and a cold? I thought the flu was like a super cold.",
  "As time goes by without anyone eating it, it starts getting dry and looking anything but appetizing, and no one\’s willing to make a move, but when the busboy takes it you go 'wait, we\’re not done with that yet.' kinda on reflex. But then you end up leaving without eating it."
]

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
