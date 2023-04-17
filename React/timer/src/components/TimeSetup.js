import React from 'react'
import './TimeSetup.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css';

export default function TimeSetup(props) {

    function decreaseBreakLength(){
        if (props.time.break){
            props.setTime(prevTime => 
                ({
                    ...prevTime,
                    break: prevTime.break-1
                 }))}  
    }
    function increaseBreakLength(){
        if (props.time.break < 60){
            props.setTime(prevTime => 
                ({
                    ...prevTime,
                    break: prevTime.break+1
                 }))}  
    }
    function decreaseSessionLength(){
        if (props.time.session){
            props.setTime(prevTime => 
                ({
                    ...prevTime,
                    session: prevTime.session-1
                 }))}  
    }
    function increaseSessionLength(){
        if (props.time.session < 60){
            props.setTime(prevTime => 
                ({
                    ...prevTime,
                    session: prevTime.session+1
                 }))} 
    }

    return (
        <div className='timer-div'>
            <div className="sb-div rounded">
                <label htmlFor="session" id="session-label" 
                className='my-2'>Session Length</label>
                <span className="sb-span" id="session">
                    <button id="session-decrement" className="btn timer-btn"
                    onClick={decreaseSessionLength}>
                        <FontAwesomeIcon icon={faMinus} />
                    </button>
                    <p id="session-length">{props.time.session}</p>
                    <button id="session-increment" className="btn timer-btn"
                    onClick={increaseSessionLength}>
                        <FontAwesomeIcon icon={faPlus} />
                    </button>
                </span>
            </div>
            
            <div className="sb-div rounded">
                <label htmlFor="break" id="break-label"
                className='my-2'>Break Length</label>
                <span className="sb-span" id="break">
                    <button id="break-decrement" className="btn timer-btn"
                    onClick={decreaseBreakLength}>
                        <FontAwesomeIcon icon={faMinus} />
                    </button>
                    <p id="break-length">{props.time.break}</p>
                    <button id="break-increment" className="btn timer-btn"
                    onClick={increaseBreakLength}>
                        <FontAwesomeIcon icon={faPlus} />
                    </button>
                </span>
            </div>
        </div>
    );
}