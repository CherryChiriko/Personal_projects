import React from 'react'
import ReactDOM from 'react-dom'

function Page (){
    return(
        <div className="container2">
      <div className="container1">
        <img src="https://lh3.googleusercontent.com/TesSrhinoe9DtqgTZ8Gh3eZvYH45JaGwaU8bBVXoZbLjxxhf-THfVAF1YS52a6zW6Kma3xDVKTzZch5d8Eh-n67SMp-bGEYHouaol-P3zC5-LbtSHvSFy4Jh37UYHmo0Wy8xcSW5Nkc=w2400?source=screenshot.guru" alt="me" />
        <h3 className="name">Sofia Di Gennaro</h3>
        <h4 className="job-title">Student</h4>
        <a className= "website" href="https://cherrychiriko.netlify.app" target="_blank">Personal Website</a>
        <div className="contacts d-flex">
          <div className="d-grid gap-2 col-4 mx-auto">
          <a className="btn bg-white email" href="mailto:sofia.digennarox@gmail.com" role="button">
          <i className="fas fa-envelope icon"></i>Email</a>
          <a className="btn btn-primary" href="https://www.linkedin.com/in/sofia-di-gennaro-3a8b49208/" role="button">
          <i className="fab fa-linkedin-in icon"></i>LinkedIn</a>
          </div>
        </div>
        <div className="about">
          <h4 className="about-title">About</h4>
          <p>I am a PhD student in Theoretical Physics, but I am interested in many things besides my current path.  am currently working part-time as a language teacher and team manager. I love learning languages and programming, which are my two main focusses at the moment. I am always eager to learn new things and improve myself. I</p>
          <h4 className="about-title">Interests</h4>
          <p>Language enthusiast and Asian lover. I like RPG games, cats, cooking & baking, anime & manga. </p>
        </div>
        <footer>
          <a className="btn bg-white" href="https://github.com/CherryChiriko" role="button">
          <i className="fab fa-github git-icon"></i></a>
        </footer>
      </div>
      </div>
    )
}

ReactDOM.render(<Page/>, document.getElementById('root'))