import { useRef } from 'react';
export default function DrumPad(props) {
  const audioRef = useRef(null);
  if (audioRef.current) {
    audioRef.current.volume = props.volume;}

  function handleClick(){
    props.handleButtonClick(props.letter);
  }
  console.log(document.getElementById("W"))
  // const audio = document.getElementById(`${props.letter}`);
  // audio.volume = 0.1;
  return (
    <button className="btn btn-dark drum-pad" onClick={handleClick}>
      <audio src={props.audio} className="clip" id={props.letter}
      ref={audioRef}/>
      <h2>{props.letter}</h2>
    </button>
  );
}

