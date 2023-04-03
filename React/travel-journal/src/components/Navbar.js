import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faEarthEurope} from '@fortawesome/free-solid-svg-icons'

export default function Navbar (){
    return(
        <nav className="flex-center">
        <span> <FontAwesomeIcon icon={faEarthEurope} className='icon-earth'/>
        My Travel Journal</span>
        </nav>
    )
}