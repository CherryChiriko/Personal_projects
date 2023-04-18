
import './Timer.css'
import React from 'react';
export default function Timer(props) {
    const [minutes, setMinutes] = React.useState(props.minutes);
    const [seconds, setSeconds] = React.useState(5);

    function timeOut(){
        console.log("BEEP");
        props.timeOut();
    }
    React.useEffect(() => {
        console.log(props.isTimerRunning)
        if (props.isTimerRunning) {
            const id = setInterval(() => {
            setSeconds( prevSeconds => {
                if (!prevSeconds) {  
                    console.log(minutes) 
                    if (!minutes){ timeOut(); return 0}
                    setMinutes((prevMinutes) => prevMinutes - 1); 
                    return 59;
                } 
                return prevSeconds - 1
            })
        }, 1000);
        return ()=> clearInterval(id)}}
    )
  return (
    <>
        <h2 id="timer-label">{props.type}</h2>
        <h1 id="time-left">
            {minutes.toLocaleString('en-US',{
            minimumIntegerDigits: 2, useGrouping: false
            })} : {seconds.toLocaleString('en-US',{
            minimumIntegerDigits: 2, useGrouping: false })}
        </h1>
        <div className="pie ten flex-center"></div>        
    </>
  );
}