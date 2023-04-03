import React from 'react'

export default function Card (props){
    return(
    <div className="container row card--div">
      <div className="col-3 col-sm-4 col-lg-2 py-4">
        <img src={props.item.imageUrl} alt="place" />
      </div>
      <div className="col-lg-4 col-6 my-5">
        <span className="row"><p className="card-location col-6"><i className="fas fa-location-dot icon-location"></i>{props.item.location.toUpperCase()}</p>
          <a href="${props.googleMapsUrl}" target="_blank" className="col-6">View on Google Maps</a></span>
        <h2 className="fw-bold">{props.item.title}</h2>
        <p className="fw-bold">{props.item.startDate} - {props.item.endDate}</p>
        <p>{props.item.description}</p>
      </div>
    </div>
    )
}