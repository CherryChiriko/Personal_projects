import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

export default function Interests (props : any){
    return(
        <div className='flex-standard flex-column'>       
            <div className="mb-3">
                <FontAwesomeIcon icon={props.icon} className='interests-icon'/>
            </div>
            <p className='text-bold mb-1'>{props.name}</p>
        </div>
        
    )
}