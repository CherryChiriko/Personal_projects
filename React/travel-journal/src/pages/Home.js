import React from 'react'
import Card from "../components/Card"
// import {cardsData} from "../assets/data"

import '../server'

export default function Home (){
    const [cardData, setCardData] = React.useState(null);
    React.useEffect(() => {
      fetch("/api/cards")
        .then(response => response.json())
        .then(json =>  setCardData(json.cards))
    }, [])

    const card = cardData.map(card => {
      return (
      <Card key={card.id} {...card}/>
    )})
    return (
      <div className="flex-center flex-column">
      {card} 
      </div>
    )
}