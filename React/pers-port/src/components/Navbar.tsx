import { NavLink } from 'react-router-dom'

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
            <NavLink className="link" to="/skills"> Skills </NavLink>
            <NavLink className="link" to="/portfolio"> Portfolio </NavLink>
            <NavLink className="link" to="/contacts"> Contacts </NavLink>
        </nav>
    )
}