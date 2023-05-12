import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faXmark, faRotateRight } from '@fortawesome/free-solid-svg-icons';

export default function CityBox(props) {
    function deleteCity(){
        props.handleDelete(props.id)
    }
    function reloadCity(){
        props.handleReload(props.id)
    }

    return (
        <div className="city-box my-1 rounded">
        <div className="left-aligned-items">
            <p className="mx-3 my-2 city-text">{props.name}</p>
        </div>
        <div className="centered-items">
            <img height="40px" src={props.icon} alt='icon'/>
            <p className="mx-3 my-2 weather-text">{props.weather}</p>
        </div>
        <div className="right-aligned-items">
            <button className="btn" onClick={reloadCity}>
            <FontAwesomeIcon icon={faRotateRight} />
            </button>
            <button className="btn" onClick={deleteCity}>
            <FontAwesomeIcon icon={faXmark} />
            </button>
        </div>
        </div>
    );
}