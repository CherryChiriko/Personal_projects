import React from 'react'
import { Link } from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faEarthEurope} from '@fortawesome/free-solid-svg-icons'

export default function Navbar (){
    return(
        <nav className="flex-center">
            <Link className="link" to="/">
            <span> <FontAwesomeIcon icon={faEarthEurope} className='icon-earth'/>
            My Travel Journal</span>
            </Link>
        </nav>
    )
}