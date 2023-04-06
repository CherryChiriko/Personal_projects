import './Die.css';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Die(props) {
    const styles = {
        backgroundColor: props.isHeld ? "#59E391" : "white"
    }
  return (
      <div className="die rounded text-center" onClick={props.handleClick}
      style={styles}>
        <h2>{props.value}</h2>
      </div>
  );
}
