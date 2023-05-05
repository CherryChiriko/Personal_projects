import { useRef } from 'react';
export default function DrumPad(props) {
  const audioRef = useRef(null);
  if (audioRef.current) {
    audioRef.current.volume = props.volume;}

  function handleClick(){
    props.handleButtonClick(props.letter);
  }
  return (
    <button className={`btn btn-dark drum-pad ${props.isActive ? 'active' : ''}`} onClick={handleClick}>
      <audio src={props.audio} className="clip" id={props.letter}
      ref={audioRef}/>
      <h2>{props.letter}</h2>
    </button>
  );
}

