import React from 'react';
import './Calculator.css'
import data from '../data/data'
import Button from './Button';

export default function Calculator() {
const buttons = data.map( button => (
<Button key={button.id} value={button.value} span={button.span} />
))
const [calculation, setCalculation] = React.useState('')
// handleClick={()=>{updateCalculation(button.value)}}
function updateCalculation(value){
    console.log(value)
}
return (
    <div className='rounded container tot-div'>
        <div className='screen container rounded'
        id="display">{calculation}</div>
        <div className='calc-div'>
            {buttons}
        </div>
    </div>
  );
}
