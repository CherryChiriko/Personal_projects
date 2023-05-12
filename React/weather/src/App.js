import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import CityBox from './components/CityBox';
import SearchBar from './components/SearchBar';

import { OW_BASEURL, OW_APIKEY } from './data/config';

export default function App() {
  const [cities, setCities] = React.useState([]);
  const [selectedId, setSelectedId] = React.useState(null);
  const [refreshKey, setRefreshKey] = React.useState(0);

  const url = selectedId?
  `${OW_BASEURL}/weather?id=${selectedId}&appid=${OW_APIKEY}` : null;

  
  React.useEffect(()=>{
    if (url){
      fetch(url)
      .then(response => response.json())
      .then(json =>  { 
        console.log(json.weather[0].description); console.log(selectedId);
        const weather = json.weather[0].description;
        if (!findCityInArray(selectedId)){
          const newCity = {
            id: json.id,
            name: json.name,
            weather: weather
          };
          setCities(prevCities=>(
            [...prevCities, newCity]))
        }
        else {
          setCities(prevCities =>
            prevCities.map(city =>
              city.id === selectedId ? 
              { ...city, weather: weather } : city
            )
          );
        }
      })
    }   
  },[selectedId, refreshKey])

  function findCityInArray(id){
    return cities.find(city => city.id === Number(id))
  }  
 
  function reloadCity(cityId){
    if (cityId !== selectedId){
      setSelectedId(cityId)
    }
    else {
    setRefreshKey(prevRefreshKey => prevRefreshKey +1)}
  }
  function deleteCity(cityId){
    setCities(prevCities => prevCities.filter(city => city.id !== cityId))
  }

  const city = cities.map(city => (
      <CityBox key={city.id} id={city.id} 
      name={city.name} 
      weather={city.weather} 
      handleDelete={cityId => deleteCity(cityId)}
      handleReload={cityId => reloadCity(cityId)}/>
  ));

  return (
    <div>
      <div className="title">
        <h2>Weather Info</h2>
      </div>
      <div className='cities-div'> 
        <SearchBar 
        selectId={id => setSelectedId(id)}/> 
        {city}
      </div>
    </div>
  );
}


 // const id = 524901;
  
  // const url= 'https://jsonplaceholder.typicode.com/todos/1'

