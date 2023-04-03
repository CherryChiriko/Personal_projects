export default function Contacts (){
    return(
        <div className="contacts d-flex">
          <div className="d-grid gap-2 col-4 mx-auto">
          <a className="btn bg-white email" href="mailto:sofia.digennarox@gmail.com" role="button">
          <i className="fas fa-envelope icon"></i>Email</a>
          <a className="btn btn-primary" href="https://www.linkedin.com/in/sofia-di-gennaro-3a8b49208/" role="button">
          <i className="fab fa-linkedin-in icon"></i>LinkedIn</a>
          </div>
        </div>
    )
}