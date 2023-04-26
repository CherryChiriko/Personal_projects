import React from 'react'
import {Link} from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faLocationDot} from '@fortawesome/free-solid-svg-icons'
export default function Card (props){
    return(
      <Link className="link" to="">
    <div className="container row card--div">
      <div className="col-3 py-4">
      
        <img src={props.imageUrl} alt={props.title} />

      </div>
      <div className="col-lg-4 col-6 my-5">
        <span className="row"><p className="card-location col-6">
          <FontAwesomeIcon icon={faLocationDot} 
          className='icon-location'/>
        {props.location.toUpperCase()}</p>
          <a href="{props.googleMapsUrl}" target="_blank" 
          className="col-6 google-a">View on Google Maps</a></span>
        <h2 className="fw-bold">{props.title}</h2>
        <p className="fw-bold">{props.startDate} - {props.endDate}</p>
        <p>{props.description}</p>
      </div>
    </div>
    </Link>
    )
}