import React from 'react';
import Timer from './Timer';
import TimeSetup from './TimeSetup';
import './Box.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowRotateRight, faPause, faPlay } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Box() {
    const [type, setType] = React.useState("session");
    const [time, setTime] = React.useState({ session: 0, break: 5  });
    const [isTimerRunning, setIsTimerRunning] = React.useState(false);

   function handleTimeOut(){
    setTimerKey(Date.now());
    setIsTimerRunning(false);
    setTime(prevTime => ({
        ...prevTime,
        [type]: prevTime[type]
    }));
   }
    const startbtn = <FontAwesomeIcon icon={faPlay} className="me-3"/>
    const stopbtn = <FontAwesomeIcon icon={faPause} className="me-3"/>
    function reset(){
        setTimerKey(Date.now());
        setIsTimerRunning(false);
        setTime({ session: 0, break: 5  });
        setType("session");
    }
    const [timerKey, setTimerKey] = React.useState(Date.now())
    return (
    <div className="box flex-center flex-column py-5 bg-white">
        <TimeSetup time={time} setTime={setTime}/>

        <Timer key={timerKey}
        type={type} minutes={time[type]} 
        isTimerRunning = {isTimerRunning}
        timeOut={handleTimeOut}/>

        <span>
            <button id="start_stop" className="mx-3"
            onClick={() => 
            (setIsTimerRunning(prevIsTimerRunning => !prevIsTimerRunning))}>
                {!isTimerRunning ? startbtn : stopbtn }
                {!isTimerRunning ? "Start" : "Pause"}
            </button>
            <button id="reset" className="btn LR-btn"
            onClick={reset}>
                <FontAwesomeIcon icon={faArrowRotateRight} />
            </button>
        </span>
    </div>
    );
  }