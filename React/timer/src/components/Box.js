import React from 'react';
import Timer from './Timer';
import TimeSetup from './TimeSetup';
import './Box.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlay, faStop } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Box() {
    const [type, setType] = React.useState("session");
    const [time, setTime] = React.useState(
        {
            session: 0,
            break: 5
        }
    );
    const [timeOut, setTimeOut] = React.useState(false);
    function handleTimerEnd(){
        setType(prevType => prevType === 'session' ? 'break' : 'session');
    }
    return (
      <div className="box flex-center flex-column py-5 bg-white">
        <TimeSetup time={time} setTime={setTime}/>
        <Timer type={type} minutes={time[type]} onTimerEnd={handleTimerEnd}/>
        <button id="start_stop">

        </button>
        <button id="reset"></button>
          <FontAwesomeIcon icon={faPlay} />
          <FontAwesomeIcon icon={faStop} />
          <div className="buttons mt-3 flex-center">
            <button className="btn mx-2" type="button" name="stop"    id="stop"    >
                <i className="fas fa-stop"></i></button>
            <button className="btn mx-2" type="button" name="start"   id="start"   >
                <i className="fas fa-play pe-2"></i>Start</button>
            <button className="btn mx-2" type="button" name="restart" id="restart" >
                <i className="fas fa-arrow-rotate-right"></i></button>
          </div>
        </div>
    );
  }