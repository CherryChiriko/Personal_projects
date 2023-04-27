import React from 'react'
import Card from "../components/Card"
import {cardsData} from "../assets/data"

export default function Home (){
    const card = cardsData.map(card => {
      return (
      <Card key={card.id} {...card}/>
    )})
    return (
      <div className="flex-center flex-column">
      {card} 
      </div>
    )
}