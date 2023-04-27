import React from 'react'
import {Link} from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faLocationDot} from '@fortawesome/free-solid-svg-icons'
export default function Card (props){
    return(
      
    <div className="row card--div rounded">
      <div className="col p-4 img-div">
      <Link className="link" to={`/entries/${props.id}`}>
        <img className="small-img" src={props.imageUrl} alt={props.title} />
      </Link>
      </div>
      <div className="col my-5">
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
    )
}