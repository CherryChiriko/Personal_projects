import React from 'react'
import photo from '../assets/images/foto.png';
// import { Link } from 'react-router-dom';

export default function Home (){
//     const fileURL = '';
//     fetch('https://cors-anywhere.herokuapp.com/' + fileURL, {
//     method: 'GET',
//     headers: {
//       'Content-Type': 'application/pdf',
//     },
//   })
//   .then((response) => response.blob())
//   .then((blob) => {
//     // Create blob link to download
//     const url = window.URL.createObjectURL(
//       new Blob([blob]),
//     );
//     const link = document.createElement('a');
//     link.href = url;
//     link.setAttribute(
//       'download',
//       `FileName.pdf`,
//     );

//     // Append to html link element page
//     document.body.appendChild(link);

//     // Start download
//     link.click();

//     // Clean up and remove the link
//     if (link.parentNode) link.parentNode.removeChild(link);
//     });

    return(
        <div className="flex-standard">
            <img src={photo} alt="Me" 
            className="home-photo rounded"></img>
            <div className="home-description">
                <p className='soft-text'>Software Developer</p>
                <h1 className='main-title'>Sofia Di Gennaro</h1>
                <p>
                Highly motivated and dedicated professional with a strong background in theoretical physics, transitioning into programming with a focus on frontend development. Equipped with a solid foundation in scientific principles and analytical thinking, I am driven by a passion for problem-solving and creating innovative software solutions. Additionally, I possess a keen interest in foreign languages and thrive in international environments.
                </p>
                <div className="row d-flex justify-content-center align-items-center">
                    <button className="btn bg-dark blue-button mx-4">Curriculum</button>
                    <button className="btn bg-dark blue-button mx-4"
                    onClick={() => window.location.href = '/contacts'}>Contact</button>
                </div>
            </div> 
        </div>
    )
}