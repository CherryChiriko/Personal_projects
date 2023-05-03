export default function Controls(props){

    return (
        <div className="control-display">
            <div class="custom-control custom-switch">
                <input type="checkbox" onClick={props.togglePower}
                className="custom-control-input" id="power" 
                />
                <label className="custom-control-label" for="power">
                    Power</label>
            </div>
            <div id="display" className="rounded">
                {props.name}
            </div>
            <p>Control 2</p>
        </div>
    );
}