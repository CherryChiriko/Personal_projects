import DrumPad from './DrumPad';
import clipsData from '../data/clipsData.json';
import React from 'react';

  export default function Pad(props) {
    const clips = clipsData;

    const drumButtons = clips.map(clip =>
      (<DrumPad letter={clip.letter} key={clip.letter}
        audio={clip.audio} volume={props.volume}
        isActive={props.keyPressed === clip.letter}
      handleButtonClick={(event, letter) => handleButtonClick(event, letter)}/>))
    
    function handleButtonClick(letter) {
      props.handleButtonClick(letter);
    }

    return (
      <div className="pad-display">
          {drumButtons}
      </div>
    );
  }
  