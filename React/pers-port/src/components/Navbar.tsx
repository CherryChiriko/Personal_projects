import './Navbar.css'
import { NavLink } from 'react-router-dom'
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import {faEarthEurope} from '@fortawesome/free-solid-svg-icons'

export default function Navbar (){
    function activeStyles(isActive : any) {
        return isActive?
        {
            color: "white",
            fontWeight: "bold"
        } : {}
    } 
    return(
        <nav className="flex-center">
            <NavLink className="link" to="/"
            style={isActive => activeStyles(isActive)}> Home </NavLink>
            <NavLink className="link" to="/"> Skills </NavLink>
            <NavLink className="link" to="/"> Portfolio </NavLink>
            <NavLink className="link" to="/"> Contacts </NavLink>
        </nav>
    )
}