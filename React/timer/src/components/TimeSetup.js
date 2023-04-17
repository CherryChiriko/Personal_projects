import React from 'react'
import './TimeSetup.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css';

export default function TimeSetup() {
    const [breakLength, setBreakLength] = React.useState(5);
    const [sessionLength, setSessionLength] = React.useState(25);

    function decreaseBreakLength(){
        setBreakLength(prevBreakLength => prevBreakLength-1)
    }
    function increaseBreakLength(){
        setBreakLength(prevBreakLength => prevBreakLength+1)
    }
    function decreaseSessionLength(){
        setSessionLength(prevSessionLength => prevSessionLength-1)
    }
    function increaseSessionLength(){
        setSessionLength(prevSessionLength => prevSessionLength+1)
    }

    return (
        <div className='timer-div'>
            <p id="break-label">Break Length</p>
            <span className="sb-span">
                <button id="break-decrement" className="btn timer-btn"
                onClick={decreaseBreakLength}>
                    <FontAwesomeIcon icon={faMinus} />
                </button>
                <p id="break-length">{breakLength}</p>
                <button id="break-increment" className="btn timer-btn"
                onClick={increaseBreakLength}>
                    <FontAwesomeIcon icon={faPlus} />
                </button>
            </span>
            <p id="session-label">Session Length</p>
            <span className="sb-span">
                <button id="session-decrement" className="mx-1"
                onClick={decreaseSessionLength}>
                    <FontAwesomeIcon icon={faMinus} />
                </button>
                <p id="session-length">{sessionLength}</p>
                <button id="session-increment" className="mx-1"
                onClick={increaseSessionLength}>
                    <FontAwesomeIcon icon={faPlus} />
                </button>
            </span>
        </div>
    );
}