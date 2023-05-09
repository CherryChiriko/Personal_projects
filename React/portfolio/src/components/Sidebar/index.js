import './index.scss';
import Logo from '../../assets/images/logo.png'
import { Link, NavLink } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub, faLinkedin } from '@fortawesome/free-brands-svg-icons';
export default function Sidebar(){
    return (
        <div className='nav-bar'>
            <Link className='logo' to='/'>
                <img src={Logo} alt='logo'></img>
            </Link>
            <nav>
                <NavLink exact="true" activeClassName ="active" to="/">
                    <FontAwesomeIcon icon="faHome" color="#4d4d4e" />
                </NavLink>
                <NavLink exact="true" activeClassName="active" 
                className="about-link" to="/about">
                    <FontAwesomeIcon icon="faUser" color="#4d4d4e" />
                </NavLink>
                <NavLink exact="true" activeClassName="active" 
                className="contact-link" to="/contact">
                    <FontAwesomeIcon icon="faEnvelope" color="#4d4d4e" />
                </NavLink>
            </nav>
            <ul>
                <li>
                    <a taget="_blank" rel="noreferrer" href="">
                        <FontAwesomeIcon icon={faLinkedin} color="#4d4d4e"/>
                    </a>
                </li>
                <li>
                    <a taget="_blank" rel="noreferrer" href="">
                        <FontAwesomeIcon icon={faGithub} color="#4d4d4e"/>
                    </a>
                </li>
            </ul>
        </div>
    )
}