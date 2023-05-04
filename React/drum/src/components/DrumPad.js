export default function DrumPad(props) {
  function handleClick(){
    props.handleButtonClick(props.letter);
  }
  return (
    <button className="btn btn-dark drum-pad" onClick={handleClick}>
      <audio src={props.audio} className="clip" id={props.letter}/>
      <h2>{props.letter}</h2>
    </button>
  );
}

