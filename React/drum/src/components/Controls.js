import BootstrapSwitchButton from 'bootstrap-switch-button-react'
import React from "react"
export default function Controls(props){
    return (
        <div className="control-display">
            <div className="custom-control custom-switch">
                {/* <input type="checkbox" onClick={props.togglePower}
                className="custom-control-input" id="power" 
                /> */}
                {/* <label className="custom-control-label" htmlFor="power">
                    Power</label> */}
                <BootstrapSwitchButton
                    checked={props.power}
                    onlabel='On'
                    offlabel='Off'
                    onChange={props.togglePower}
                    size="sm"
                    onstyle="info"
                    offstyle="secondary"
                />
            </div>
            <div id="display" className="rounded my-3">
                {props.name}
            </div>
            <label htmlFor='volume-control'>Volume</label>
            <input
                id="volume-control"
                type="range"
                min={0}
                max={1}
                step={0.02}
                value={props.volume}
                onChange={event => {
                props.handleVolume(event.target.valueAsNumber)
                }}
            />
        </div>
    );
}