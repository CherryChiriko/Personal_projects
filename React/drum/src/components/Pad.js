import DrumPad from './DrumPad';
import clipsData from '../data/clipsData.json';
import React from 'react';

  export default function Pad(props) {
    const clips = clipsData;
    const [keyPressed, setKeyPressed] = React.useState(
      props.keyPressed ? 
    props.keyPressed.toUpperCase() : null);

    const drumButtons = clips.map(clip =>
      (<DrumPad letter={clip.letter} audio={clip.audio} key={clip.letter}
      isPowerOn={props.isPowerOn} 
      handleButtonClick={(event, letter) => handleButtonClick(event, letter)}/>))
    
    function playAudio(){
      if (props.isPowerOn) {
        document.getElementById(`${keyPressed}`).play();
        console.log(keyPressed)
        props.resetKey();
        console.log("after reset", keyPressed)
      }
      else return;
    }
    // function handleButtonClick(event, letter){
    //   console.log(event.target, letter)
    //   setKeyPressed(letter);
    //   props.handleButtonClick(letter);
    // }

    function handleButtonClick(letter) {
      console.log(`Button ${letter} clicked`);
      setKeyPressed(letter);
      props.handleButtonClick(letter);
    }

    if (keyPressed && document.getElementById(`${keyPressed}`))
      { playAudio() }
    return (
      <div className="pad-display">
          {drumButtons}
      </div>
    );
  }
  