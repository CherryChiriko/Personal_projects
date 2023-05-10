import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import CityBox from './components/CityBox';
import SearchBar from './components/SearchBar';

export default function App() {
  const [cities, setCities] = React.useState([]) 

  function addCity(city){
    setCities(prevCities => [...prevCities, city])
  }
  function deleteCity(cityId){
    setCities(prevCities => prevCities.filter(city => city.id !== cityId))
  }

  const city = cities.map(city => (
      <CityBox key={city.id} id={city.id} 
      name={city.name} weather={'weather'} 
      handleDelete={cityId => deleteCity(cityId)}/>
  ));

  return (
    <div>
      <div className="title">
        <h2>Weather Info</h2>
      </div>
      <div className='cities-div'> 
        <SearchBar handleChange={city => addCity(city)}/> 
        {city}
      </div>
    </div>
  );
}
