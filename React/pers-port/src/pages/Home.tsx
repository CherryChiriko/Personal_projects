import React from 'react'
import photo from '../assets/images/foto.png';

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
        <div className="home-div">
            <img src={photo} alt="Me" 
            className="home-photo rounded"></img>
            <div className="home-description">
                <p className='home-job'>Software Developer</p>
                <h1 className='home-title'>Sofia Di Gennaro</h1>
                <p>
                Highly motivated and dedicated professional with a strong background in theoretical physics, transitioning into programming with a focus on frontend development. Equipped with a solid foundation in scientific principles and analytical thinking, I am driven by a passion for problem-solving and creating innovative software solutions. Additionally, I possess a keen interest in foreign languages and thrive in international environments.
                </p>
                <div className="row">
                    <button className="btn bg-dark home-button">Curriculum</button>
                    <button className="btn bg-dark home-button">Contact</button>
                    
                </div>
            </div> 
        </div>
    )
}