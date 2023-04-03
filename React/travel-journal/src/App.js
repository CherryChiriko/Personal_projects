import React from 'react'
import Navbar from "./components/Navbar"
import Card from "./components/Card"
import {cardsData} from "./data"

export default function App (){
    const card = cardsData.map(card => {
      return (
      <Card key={card.id} {...card}/>
    )})
    return (
      <>
      <Navbar/>
      {card}
      </>
    )
}

