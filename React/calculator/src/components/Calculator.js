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

function multiplyDivide(match, n1, op, n2) {
    n1 = Number(n1);    n2 = Number(n2);
    return (op === 'x' ? n1 * n2 : n1 / n2).toString();
}

function addSubtract(match, n1, op, n2){
    n1 = Number(n1); n2 = Number(n2); 
    return (op==='+'? n1 + n2: n1 - n2).toString();
}

function compute(){
    let result = calculation.split(' ').join('');
    let regex = /(-?\d+(?:\.\d+)?)([x/])(-?\d+(?:\.\d+)?)/g;
    
    result = result.replace(regex, multiplyDivide)
    regex = /(-?\d+(?:\.\d+)?)([+-])(-?\d+(?:\.\d+)?)/g;

    while (regex.test(result)) {
        result = result.replace(regex, addSubtract); console.log(result)
    }
    return result
}

function addCharacter(calc, val){
    let calcArr = calc? calc.split(' ') : [];
    if (calcArr.length >= 15) {return 'DIGIT LIMIT MET'} 
    calcArr.push(val)
    return calcArr.join(' ')
}

// function checkForm(val, num){
//     switch(val){
//         case 0: return false;
//         default: return true;
//     }
// }

function updateCalculation(val){
    
    switch(val){
        case 'AC': setCalculation(''); break;
        case '=': setCalculation(compute()); break;
        case 0: if (calculation ==='0') {break}
        // eslint-disable-next-line no-fallthrough
        case '.': 
        console.log(calculation[calculation.length-1], calculation)
        if (calculation[calculation.length-1]==='.') {break}
        // eslint-disable-next-line no-fallthrough
        default: 
        if (calculation === 'DIGIT LIMIT MET'){setCalculation(''); break;}
        setCalculation(prevCalculation => addCharacter(prevCalculation, val));
        break;
    }
    // val==="AC"? setCalculation('') :
    // val==="="? setCalculation(compute()) :
    // setCalculation(prevCalculation => addCharacter(prevCalculation, val))
}
return (
    <div className='rounded tot-div'>
        <div className='screen rounded'
        id="display">{calculation}</div>
        <div className='calc-div'>
            {buttons}
        </div>
    </div>
  );
}



// const regex = /(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)/;

// while (regex.test(expression)) {
//   expression = expression.replace(regex, (match, n1, op, n2) => {
//     n1 = Number(n1);    n2 = Number(n2);
//     let result = match;
//     switch (op) {
//       case '*':
//         result = n1 * n2; break;
//       case '/':
//         result = n1 / n2; break;
//       case '+':
//         result = n1 + n2; break;
//       case '-':
//         result = n1 - n2;  break;
//       default: break;
//     }
//     return result.toString();
//   });
// }