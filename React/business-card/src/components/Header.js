import photo from './foto.png';

export default function Header (){
    return(
        <div>
            <img src={photo} alt="my_picture" />
            <h3 className="name">Sofia Di Gennaro</h3>
            <h4 className="job-title">Software Developer</h4>
            <a className= "website" href="https://cherrychiriko.netlify.app" target="_blank">Personal Website</a>
        </div>
    )
}