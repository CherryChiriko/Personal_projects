  stop = document.getElementById("stop");
  const MINUTES = 0; const SECONDS = 3;

  function alarm(){
    alert("Helloooo");
  }
  function display_number (m, s){
    m = (m).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    s = (s).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    document.getElementById("time").innerHTML = m+": "+s;
  }
  function stop_timer (m = MINUTES, s = SECONDS){
    stop.disabled = true; clearInterval(display); clearTimeout(myTimeout);
    minutes = m; seconds = s; display_number (minutes, seconds);
    pause = false; start.innerHTML = "<i class='fas fa-play pe-2'></i>Start";
  }
  function timer(){
    display_number (minutes, seconds)

    if (seconds==0){minutes-=1; seconds=59;}  else{seconds-=1};
    if(minutes==0 && seconds==0){
        display_number (minutes, seconds);
        clearInterval(display);}
  }

  let pause = false;   stop.disabled = true; restart.disabled = true; start.disabled = false;
  let minutes = MINUTES;  let seconds = SECONDS;
  display_number (minutes, seconds);

  pause.onclick   = () => { clearInterval(display);}
  restart.onclick = () => { stop_timer();    restart.disabled = true;  start.disabled = false;}
  stop.onclick    = () => { stop_timer(0,0); restart.disabled = false; start.disabled = true;}

  start.onclick   = () => {
    if (!pause){
      stop.disabled = false; restart.disabled = false;
      myTimeout = setTimeout(alarm, 1000*(seconds+1)+60000*minutes);
      display = setInterval(timer, 1000); pause = true; start.innerHTML = "<i class='fas fa-pause pe-2'></i>Pause";}
    else {
      clearInterval(display); clearTimeout(myTimeout);
      pause = false; start.innerHTML = "<i class='fas fa-play pe-2'></i>Start";
    }
  }
