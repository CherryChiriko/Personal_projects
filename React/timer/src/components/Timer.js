
import './Timer.css'
import React from 'react';
export default function Timer(props) {
    const [minutes, setMinutes] = React.useState(props.minutes);
    const [seconds, setSeconds] = React.useState(5);

    const [isTimerRunning, setIsTimerRunning] = React.useState(true); 
    function timeOut(){
        setIsTimerRunning(false);
        console.log("BEEP")
    }
    React.useEffect(() => {
        console.log(isTimerRunning)
        if (isTimerRunning) {
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
        return ()=> clearInterval(id)}   }
    ,[isTimerRunning, minutes])
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