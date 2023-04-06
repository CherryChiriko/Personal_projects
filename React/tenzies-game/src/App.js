import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react'
import { nanoid } from 'nanoid';
import Die from './components/Die'
import Confetti from 'react-confetti'
import useWindowSize from 'react-use/lib/useWindowSize'

/**
 * Challenge:
 * 1. Add new state called `tenzies`, default to false. It
 *    represents whether the user has won the game yet or not.
 * 2. Add an effect that runs every time the `dice` state array 
 *    changes. For now, just console.log("Dice state changed").
 */
export default function App() {
  const { width, height } = useWindowSize()

  const [tenzies, setTenzies] = React.useState(false)  // Win the game or not

  function allNewDice(){
    let dice = [] 
    for(let i=0; i<10; i++ ){
      dice.push(
        {
          id: nanoid(),
          value: Math.ceil(Math.random()*6),
          isHeld: false
        })
    }
    return dice
  }

  const [diceArray, setDiceArray] = React.useState(allNewDice())
  let dice = diceArray.map(die => (
    <Die key={die.id} value={die.value} isHeld={die.isHeld}
    handleClick={() => toggleHold(die.id)}/>
  ))
  
  function rollDice(){    
    if (tenzies) {setDiceArray(allNewDice()); setTenzies(false)}
    else{
      setDiceArray(oldDice => oldDice.map(die => {
      return !die.isHeld ? 
          {...die, value: Math.ceil(Math.random()*6)} :
          die
    }))
  }}
  function toggleHold(id) {
    setDiceArray(oldDice => oldDice.map(die => {
      return die.id === id ? 
          {...die, isHeld: !die.isHeld} :
          die
    }))
  }
  React.useEffect(() => {
    const allHeld = diceArray.every( die => die.isHeld)
    const allSameNum = diceArray.every(die => die.value === diceArray[0].value)
    if (allHeld && allSameNum){
      setTenzies(true); 
      console.log("You won!")
    }
  }, [diceArray])
  return (
    <main>
      {tenzies && < Confetti
      width={width}
      height={height}
      />}
      <div className="rounded app-box">
      <h1 className="title">Tenzies</h1>
            <p className="instructions">Roll until all dice are the same. Click each die to freeze it at its current value between rolls.</p>
        <div className="div-grid">
          {dice}
        </div>
        <button className='btn btn-primary mt-5 px-4' onClick={rollDice}>{tenzies? "New Game" : "Roll"}</button>
      </div>
    </main>
  );
}

