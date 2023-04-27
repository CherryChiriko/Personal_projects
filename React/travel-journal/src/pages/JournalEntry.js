import React from 'react'
import Entry from "../components/Entry"
import {cardsData} from "../assets/data"
import { useParams } from 'react-router-dom'


export default function JournalEntry (){
    const params = useParams()
    const card = cardsData.find(card => card.id === Number(params.id))
    return (
      <>
      <Entry card={card}/>
      </>
    )
}