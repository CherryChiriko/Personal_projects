export default function Controls(props){
    console.log(props.name)
    return (
        <div className="control-display">
            <div className="custom-control custom-switch">
                <input type="checkbox" onClick={props.togglePower}
                className="custom-control-input" id="power" 
                />
                <label className="custom-control-label" htmlFor="power">
                    Power</label>
            </div>
            <div id="display" className="rounded">
                {props.name}
            </div>
            <p>Control 2</p>
        </div>
    );
}