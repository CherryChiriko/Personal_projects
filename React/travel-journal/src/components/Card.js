import React from 'react'

export default function Card (props){
    return(
    <div className="container row card--div">
      <div className="col-3 col-sm-4 col-lg-2 py-4">
        <img src={props.imageUrl} alt="place" />
      </div>
      <div className="col-lg-4 col-6 my-5">
        <span className="row"><p className="card-location col-6">
          <i className="fas fa-location-dot icon-location"></i>
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