import React from 'react'

export default function Skill (props : any){
    return(
        <div className=''>
            <p className='text-bold mb-1'>{props.name}</p>
            <div className="progress mb-3">
                <div className="progress-bar" role="progressbar"
                style={{width: `${props.level*10}%`}} />
            </div>
        </div>
        
    )
}