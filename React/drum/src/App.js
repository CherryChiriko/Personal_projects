import './App.css';
import Controls from './components/Controls';
import Pad from './components/Pad';
import React from 'react';

function App() {
  const [key, setKey] = React.useState(null)
  function handleKeyPress(event){
    setKey(event.key)
  }
  function resetKey(){ setKey(null)}
  return (
    <div id="drum-machine" tabIndex={-1} onKeyDown={event => handleKeyPress(event)}>
      <div id="box">
        <Pad keyPressed={key} resetKey={resetKey}/>
        <Controls/>
      </div>
    </div>
  );
}

export default App;
