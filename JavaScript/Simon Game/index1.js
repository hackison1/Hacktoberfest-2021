$("div.yellow").click(addclass);
$("div.red").click(addclass);
$("div.blue").click(addclass);
$("div.green").click(addclass);

let i = 1;

function addclass(e) {
  e.target.classList.add("pressed");
  setTimeout(() => {
    e.target.classList.remove("pressed");
  }, 50);
  audio = document.querySelector(`audio.${e.target.classList[1]}`);
  audio.currentTime = 0;
  audio.play();
  gamecheck(parseInt(e.target.dataset.key));
}

let btn = {};
function start(e) {
  if (e.key == "a" || e.key == "A" || e == "start") {
    btn[i] = Math.floor(Math.random() * 4 + 1);
    console.log(btn[i]);
    box = $(`div[data-key="${btn[i].toString()}"]`);
    box.addClass("pressed");
    setTimeout(() => {
      box.removeClass("pressed");
    }, 50);
    audio = document.querySelector(`audio[data-key="${btn[i].toString()}"]`);
    audio.currentTime = 0;
    audio.play();
  }
}
let k = 1;
function gamecheck(keyno) {
  console.log(keyno);
  if ( btn[k]== keyno) {
    if (k == i) {
      $("h1").text(`Level ${i}`);
      i++;
      setTimeout(() => {
        start("start");
      }, 1000);
      k = 1;
    }
    else
    k++;
  } else {
    $("body").addClass("game-over");
    setTimeout(() => {
      $("body").removeClass("game-over");
    }, 50);
    i = 1;
    k=1;
    audio = document.querySelector(`audio.wrong`);
    audio.currentTime = 0;
    audio.play();
    $("h1").text(`Game Over,Press A to Restart`);
  }
}

if (i == 1) $(window).keydown(start);
