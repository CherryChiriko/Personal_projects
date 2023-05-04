import DrumPad from './DrumPad';
import clipsData from '../data/clipsData.json';
import React from 'react';

  export default function Pad(props) {
    const clips = clipsData;

    const drumButtons = clips.map(clip =>
      (<DrumPad letter={clip.letter} audio={clip.audio} key={clip.letter}
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
  