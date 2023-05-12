import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import CityBox from './components/CityBox';
import SearchBar from './components/SearchBar';
import { OW_BASEURL, OW_APIKEY } from './data/config';

export default function App() {
  const [cities, setCities] = React.useState([]) 
  const [selectedId, setSelectedId] = React.useState(null);

  function findCityInArray(id){
    return cities.find(city => city.id === id)
  }

  const fetchWeatherData = (id) => {
    if (!findCityInArray(id)){
      const url=`${OW_BASEURL}/weather?id=${id}&appid=${OW_APIKEY}`;
      fetch(url)
        .then(response => response.json())
        .then(json =>  {
          // console.log(json.weather[0].description)
          setCities(prevCities=>(
            [...prevCities, 
              {id:json.id, name: json.name, weather: json.weather[0].description}]))
      })}
    }
  
  // const id = 524901;
  
  // const url= 'https://jsonplaceholder.typicode.com/todos/1'

  React.useEffect(()=>{
    fetchWeatherData(selectedId)}, [selectedId])

  function addCity(city){
    setSelectedId(city.id)
    // setCities(prevCities => [...prevCities, city])
  }
  function deleteCity(cityId){
    setCities(prevCities => prevCities.filter(city => city.id !== cityId))
  }

  const city = cities.map(city => (
      <CityBox key={city.id} id={city.id} 
      name={city.name} weather={city.weather} 
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
