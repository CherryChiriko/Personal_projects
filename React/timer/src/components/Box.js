import React from 'react';
import Timer from './Timer';
import TimeSetup from './TimeSetup';
import './Box.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlay } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Box() {
    return (
      <div class="box flex-center flex-column py-5 bg-white">
        <TimeSetup/>
        <Timer type="Session" minutes={25}/>
        <button id="start_stop"></button>
        <button id="reset"></button>
          <FontAwesomeIcon icon={faPlay} />
          <div class="buttons mt-3 flex-center">
            <button class="btn mx-2" type="button" name="stop"    id="stop"    >
                <i class="fas fa-stop"></i></button>
            <button class="btn mx-2" type="button" name="start"   id="start"   >
                <i class="fas fa-play pe-2"></i>Start</button>
            <button class="btn mx-2" type="button" name="restart" id="restart" >
                <i class="fas fa-arrow-rotate-right"></i></button>
          </div>
        </div>
    );
  }