import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faEnvelope } from '@fortawesome/free-solid-svg-icons'
import { faLinkedin } from '@fortawesome/free-brands-svg-icons';
import './Contacts.css';

export default function Contacts (){
    return(
      <div className="contacts">
      <div className="row justify-content-center">
        <div className="mx-5 col d-flex justify-content-between">
          <button className="btn bg-white text-dark">
            <a href="mailto:sofia.digennarox@gmail.com" className="mail">
              <FontAwesomeIcon icon={faEnvelope} className="mail icon"/>Email
            </a>
          </button>
          <button className="btn btn-primary"> 
            <a href="https://www.linkedin.com/in/sofia-di-gennaro-3a8b49208/"
            className="linkedin">
              <FontAwesomeIcon icon={faLinkedin} className="icon linkedin"/>LinkedIn
            </a>
          </button>
        </div>
      </div>
    </div>
    
        // <div className="contacts">
        //   <div className="d-grid gap-2 col-4 mx-auto justify-center">
        //     <button className="btn bg-white">
        //       <a href="mailto:sofia.digennarox@gmail.com">
        //       <FontAwesomeIcon icon={faEnvelope} className="icon"/>Email
        //       </a>
        //     </button>
        //     <button className="btn btn-primary"> 
        //       <a href="https://www.linkedin.com/in/sofia-di-gennaro-3a8b49208/">
        //       <FontAwesomeIcon icon={faLinkedin} className="icon linkedin"/>LinkedIn
        //       </a>
        //     </button>
        //   </div>
        // </div>
    )
}