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
function multiplyDivide(match, n1, n2){
    n1 = Number(n1); n2 = Number(n2); 
    console.log(n1, n2)
    let op = match.match(/[x/]/)[0];
    return (op==='x'? n1 * n2: n1/n2).toString();
}
function addSubtract(match, n1, op, n2){
    n1 = Number(n1); n2 = Number(n2); 
    return (op==='+'? n1 + n2: n1 - n2).toString();
}
let result = expression.replace(regex, multiplyDivide)
const regex2 = /^(-?\d+(?:\.\d+)?)\s*([+-])\s*(-?\d+(?:\.\d+)?)/;
console.log(result.match(regex2))
console.log('-----' + result.replace(regex2, addSubtract))
while (regex2.test(result)) {
    result = result.replace(regex2, addSubtract);
    console.log(result)
}
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
