import './App.css';
import Controls from './components/Controls';
import Pad from './components/Pad';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import clipsData from './data/clipsData.json';

export default function App() {
  const [isPowerOn, setIsPowerOn] = React.useState(false)
  function togglePower(){
    setIsPowerOn(prevIsPowerOn => !prevIsPowerOn)
  }

  const [key, setKey] = React.useState(null);

  function handleKeyPress(event){
    const keyPressed = event.key.toUpperCase()
    if (document.getElementById(`${keyPressed}`)){
      setKey(keyPressed) 
    }
  }
  function handleKeyLift(){    setKey(null)  }

  function setLetter(letter){
    console.log(letter)
    setKey(letter)
  }

  function playAudio(){
    if (isPowerOn) {
      document.getElementById(`${key}`).play();
    }
  }
  
  if (key && document.getElementById(`${key}`))
  { playAudio() }

  function getClipName(){
    const matchingClip = isPowerOn ? clipsData.find(clip => clip.letter === key) : null;
    return matchingClip ? matchingClip.name : ''
  }

  return (
    <div id="drum-machine" tabIndex={-1} 
    onKeyDown={event => handleKeyPress(event)}
    onKeyUp={handleKeyLift}
    >
      <div id="box" className='rounded'>
        <Pad isPowerOn={isPowerOn} keyPressed={key}
        handleButtonClick={setLetter}/>
        <Controls togglePower={togglePower} name={getClipName()}/>
      </div>
    </div>
  );
}

