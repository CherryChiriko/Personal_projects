import 'bootstrap/dist/css/bootstrap.min.css';
export default function DrumPad(props) {
  function playAudio(){
    document.getElementById(`${props.letter}`).play();
  }
  
  return (
    <button className="btn btn-light drum-pad" onClick={playAudio}>
      <audio src={props.audio} className="clip" id={props.letter}/>
      <h2>{props.letter}</h2>
    </button>
  );
}

