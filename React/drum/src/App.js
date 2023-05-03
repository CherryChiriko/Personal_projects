import './App.css';
import Controls from './components/Controls';
import Pad from './components/Pad';
import React from 'react';

function App() {
  const [key, setKey] = React.useState(null);

  function handleKeyPress(event){
    setKey(event.key)  }
  function setLetter(letter){
    console.log(letter)
    setKey(letter)
  }
  function resetKey(){ setKey(null)}

  const [isPowerOn, setIsPowerOn] = React.useState(false)
  function togglePower(){
    setIsPowerOn(prevIsPowerOn => !prevIsPowerOn)
  }

  return (
    <div id="drum-machine" tabIndex={-1} onKeyDown={event => handleKeyPress(event)}>
      <div id="box">
        <Pad isPowerOn={isPowerOn} keyPressed={key} resetKey={resetKey}
        handleButtonClick={setLetter}/>
        <Controls togglePower={togglePower} name={key}/>
      </div>
    </div>
  );
}

export default App;
