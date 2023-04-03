import React from 'react'
import Navbar from "./components/Navbar"
import Card from "./components/Card"
import cardsData from "./data"

export default function App (){
    console.log(cardsData);
    const card = cardsData.map(item => {
        return <Card item={item} />
    })
    return (
            <div>
            <Navbar/>
             {card}
            </div>
    )
}
