import DrumPad from './DrumPad';
import clipsData from '../data/clipsData.json';
  
  export default function Pad(props) {
    const clips = clipsData;
    const keyPressed = props.keyPressed ? 
    props.keyPressed.toUpperCase() : null;

    const drumButtons = clips.map(clip =>
      (<DrumPad letter={clip.letter} audio={clip.audio} key={clip.letter}/>))
    
    function playAudio(){
      console.log("pressed")
      document.getElementById(`${keyPressed}`).play();
    }
    
    if (keyPressed && document.getElementById(`${keyPressed}`))
      { playAudio(); props.resetKey()}
    return (
      <div className="pad-display">
          {drumButtons}
      </div>
    );
  }
  