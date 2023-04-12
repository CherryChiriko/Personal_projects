import React from 'react';
import './Calculator.css'
import data from '../data/data'
import Button from './Button';

export default function Calculator() {
const buttons = data.map( button => (
<Button keys={button.id} value={button.value} span={button.span}
        handleClick={() => {updateCalculation(button.value)}}/>
))
const [calculation, setCalculation] = React.useState('');

function compute(){
    // Use regex to match numbers separated by /, x, +, -
  const regex = /(-?\d+(?:\.\d+)?)[/x](-?\d+(?:\.\d+)?)([/x+-]?)/g;

  // Use a callback function to replace matched expressions with calculated result
//   const result = '5/2 + 3.5x4 - 1'.replace(regex, (match, num1, num2, operator) => {
//     // Convert matched numbers to floats for decimal support
//     num1 = parseFloat(num1);
//     num2 = parseFloat(num2);

//     // Perform division or multiplication based on operator
//     if (operator === '/') {
//       return (num1 / num2).toString();
//     } else if (operator === 'x') {
//       return (num1 * num2).toString();
//     }

//     // Return the original match if operator is not / or x
//     return match;
//   });
let expression = '5/2 + 3.5x4 - 1'
const regArr =  expression.match(regex)
console.log(regArr)
function multiplyDivide(match, n1, n2, op){
    n1 = Number(n1); n2 = Number(n2)
    const result = n1 + n2;
    return result.toString()
}
let result = expression.replace(regex, multiplyDivide)
return result
  // Evaluate the remaining + and - operations in the expression
//   return eval(result);
}
console.log(compute())
function addCharacter(calc, val){
    let calcArr = calc? calc.split(' ') : [];
    if (calcArr.length >= 15) {return 'DIGIT LIMIT MET'} 
    calcArr.push(val)
    return calcArr.join(' ')
}
function updateCalculation(val){
    val==="AC"? setCalculation('') :
    val==="="? compute() :
    setCalculation(prevCalculation => addCharacter(prevCalculation, val))
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
