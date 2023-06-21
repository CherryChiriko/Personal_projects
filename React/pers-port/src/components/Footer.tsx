import './Navbar.css'
import { NavLink } from 'react-router-dom'
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import {faEarthEurope} from '@fortawesome/free-solid-svg-icons'

export default function Footer (){
    return(
        <div className="flex-center">
            <NavLink className="link" to="/skills"> Skills </NavLink>
            <NavLink className="link" to="/portfolio"> Portfolio </NavLink>
            <NavLink className="link" to="/contacts"> Contacts </NavLink>
        </div>
    )
}