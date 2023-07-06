
import './Timer.css'
import React from 'react';
import mp3 from '../assets/store-beep.mp3';

export default function Timer(props) {
    const SECONDS = 0;
    const [minutes, setMinutes] = React.useState(props.minutes);
    const [seconds, setSeconds] = React.useState(SECONDS);

    
    const totalSeconds = props.minutes*60 + SECONDS;
    const [styles, setStyles] = React.useState(
        { backgroundImage: `none` }
    )

    function timeOut(){
        document.getElementById('beep').play();
        props.timeOut();
    }
    
    React.useEffect(() => {
        if (props.isTimerRunning) {
            const id = setInterval(() => {
            setSeconds( prevSeconds => {
                if (!prevSeconds) {  
                    if (!minutes){ timeOut(); return 0}
                    setMinutes((prevMinutes) => prevMinutes - 1); 
                    return 59;
                } 
                return prevSeconds - 1
            })
            if (!seconds && !minutes) {return}
            const elapsedSeconds = 1 + totalSeconds - (minutes*60 + seconds);
            let deg = 360 * elapsedSeconds / totalSeconds;
            setStyles({
                backgroundImage: `conic-gradient(white ${deg}deg, transparent 0)`
            })
        }, 1000);
        return ()=> clearInterval(id)}}
    )
  return (
    <>  
        <audio src={mp3} id="beep"/>
        <h2 id="timer-label">{props.type}</h2>
        <div className='outside-circle'>
            <div className="ten flex-center"
            style={styles}> 

                <div className="inside-circle flex-center">
                    <h1 id="time-left">
                    {minutes.toLocaleString('en-US',{
                    minimumIntegerDigits: 2, useGrouping: false
                    })} : {seconds.toLocaleString('en-US',{
                    minimumIntegerDigits: 2, useGrouping: false })}
                    </h1>
                </div>
            </div>
        </div>       
    </>
  );
}