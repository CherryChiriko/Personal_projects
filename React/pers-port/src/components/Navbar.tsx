import { NavLink } from 'react-router-dom'

export default function Navbar (){ 
    return(
        <nav className="flex-center">
            <NavLink to="/"
            className={({isActive}) => isActive ? "active-link" : "link"}> 
                Home </NavLink>
            <NavLink to="/skills"
            className={({isActive}) => isActive ? "active-link" : "link"}>
                Skills </NavLink>
            <NavLink to="/portfolio"
            className={({isActive}) => isActive ? "active-link" : "link"}> 
                Portfolio </NavLink>
            <NavLink to="/contacts"
            className={({isActive}) => isActive ? "active-link" : "link"}> 
                Contacts </NavLink>
        </nav>
    )
}