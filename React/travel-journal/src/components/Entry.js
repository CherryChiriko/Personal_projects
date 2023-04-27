import React from 'react'

export default function Entry (props){
    function parseEntry(){
        return props.card.entry.split('\n').map(str => <p>{str}</p>)
    }

    return(
        <div className="d-flex flex-row py-4 total-div-entry ">
        <div className='col-md-3 mx-auto my-4'>
          <img className="large-img" src={props.card.imageUrl} alt={props.card.title}></img>
        </div>
        <div className='col-md-8 my-4'>
          <div className='row'>
            <div className='col'>
              <h2 className="entry-title">{props.card.title}</h2>
            </div>
          </div>
          <div className='row'>
            <div className='col'>
              <p className="entry-body">{parseEntry()}</p>
            </div>
          </div>
        </div>
      </div>
      

    )
}