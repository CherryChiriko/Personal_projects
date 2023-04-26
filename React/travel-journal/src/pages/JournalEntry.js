import React from 'react'
import Card from "../components/Card"
import {cardsData} from "../assets/data"

export default function JournalEntry (){
    const card = cardsData.map(card => {
      return (
      <Card key={card.id} {...card}/>
    )})
    return (
      <>
      {card} 
      </>
    )
}