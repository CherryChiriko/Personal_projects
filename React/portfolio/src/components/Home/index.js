import AnimatedLetters from '../AnimatedLetters';
import './index.scss';
import React from 'react'
export default function Home(){
    const [letterClass, setLetterClass] = React.useState('text-animate')
    const nameArray = ['l', 'o', 'b']
    const jobArray = ['web developer']

    React.useEffect(()=>{
        return setTimeout(()=>{
            setLetterClass('text-animate-hover')
        }, 4000)
    })
    return (
        <div className='container home-page'>
            <div className='text-zone'>
                <h1>
                <span className={letterClass}> H </span>
                <span className={`${letterClass} _12`}> i, </span>
                <br />
                <span className={`${letterClass} _12`}> I </span>
                <span className={`${letterClass} _12`}> a </span>
                <span className={`${letterClass} _12`}> m </span>
                <AnimatedLetters letterClass={letterClass} 
                strArray={nameArray} idx={15}/>
                <br/>
                <AnimatedLetters letterClass={letterClass} 
                strArray={jobArray} idx={22}/>
                </h1>
                <h2>Frontend Developer / JavaScript Expert</h2>
                <Link to='/contact' className='flat-button'>CONTACT ME</Link>
            </div>
            <Logo />
        </div>
    )
}