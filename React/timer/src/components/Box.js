import React from 'react';
import Timer from './Timer';
import TimeSetup from './TimeSetup';
import './Box.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowRotateRight, faPause, faPlay } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Box() {
    const [time, setTime] = React.useState({ session: 0, break: 0  });
    const [type, setType] = React.useState("session");
    const [isTimerRunning, setIsTimerRunning] = React.useState(false);
    const [timerKey, setTimerKey] = React.useState(Date.now())

    const previousTimeRef = React.useRef(null);

    function handleTimeOut(){
        setType(prevType=> (prevType === "session" ? "break" : "session"))     
    }
    
    function reset(){
        setTimerKey(Date.now());
        setIsTimerRunning(false);
        setTime({ session: 25, break: 5  });
        setType("session");
    }
    React.useEffect( () => {
        if (!isTimerRunning && previousTimeRef.current !== time) {
            console.log(previousTimeRef.current, time)
            previousTimeRef.current = time;
            setTimerKey(Date.now());}
    }, [type, time])

    
    const startbtn = <FontAwesomeIcon icon={faPlay} className="me-3"/>
    const stopbtn = <FontAwesomeIcon icon={faPause} className="me-3"/>

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