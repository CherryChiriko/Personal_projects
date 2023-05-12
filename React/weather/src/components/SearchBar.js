import React from 'react';
import citiesData from '../data/cities.json'

export default function SearchBar(props) {

    const handleChange = (event) => {
        const index = event.target.selectedIndex;
        const el = event.target.childNodes[index]
        const option =  el.getAttribute('id');

        props.handleChange({id: option, name: event.target.value})
    };
    const searchCity = citiesData.map(city => (
        <option key={`option-${city._id}`} value={city.name} id={city._id}>
          {city.name}
        </option>
    ));
    return (
        <div className="city-box my-3 rounded">
        <select className="form-select" onChange={handleChange}>
            <option selected disabled>Add a city...</option>
            {searchCity}
        </select>
        </div>
    );
}