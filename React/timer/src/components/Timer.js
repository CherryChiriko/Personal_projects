
import './Timer.css'
import React from 'react';
export default function Timer(props) {
    const [minutes, setMinutes] = React.useState(0);
    const [seconds, setSeconds] = React.useState(5);

    React.useEffect(() => {
        const id = setInterval(() => {
            setSeconds( prevSeconds => {
               if (!prevSeconds) {
                setMinutes((prevMinutes) => prevMinutes - 1); return 59;
               } 
               return prevSeconds - 1
            })
        }, 1000);
        return ()=> clearInterval(id)},[])
  return (
    <>
        <h2 id="timer-label">{props.type}</h2>
        <h1 id="time-left">
            {minutes.toLocaleString('en-US',{
            minimumIntegerDigits: 2, useGrouping: false
            })} : {seconds.toLocaleString('en-US',{
            minimumIntegerDigits: 2, useGrouping: false })}
        </h1>
        <div className='circle'></div>
        <pie className="ten flex-center"></pie>
        {/* <div class="border1">
        <div class="border2 flex-center">
          <h1 id="time"></h1>
        </div>
        </div> */}
        
    </>
  );
}