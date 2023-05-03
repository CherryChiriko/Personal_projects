import 'bootstrap/dist/css/bootstrap.min.css';
export default function DrumPad(props) {
  // function playAudio(){
  //   if (props.isPowerOn) {
  //     document.getElementById(`${props.letter}`).play();}
  //   else return;
  // }
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

