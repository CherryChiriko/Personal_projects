import './index.scss';
import Logo from '../../../assets/images/logo.png'
export default function Logo(){
    return (
        <div className="logo-container">
            <img className='solid-logo' src={Logo} alt="S" />
        </div>
    )
}