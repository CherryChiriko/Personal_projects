import React from 'react'
import './App.css';
import Editor from './components/Editor'
import Preview from './components/Preview'
// import removeMarkdown from "markdown-to-text";

import initText from './assets/content.md';
import {marked} from 'marked';

export default function App() {
  const [text, setText] = React.useState('');
  const [parsedText, setParsedText] = React.useState('');
  function handleTextChange(val){    
    // console.log(marked.parse(val))
    setText(val); setParsedText(marked.parse(val))  
  }
  
  React.useEffect(()=>{
    fetch(initText)
    .then(res => res.text())
    .then(text => {
      setText(text); 
      setParsedText(marked.parse(text))
    })
  })

  return (
    <div className="App">
      <Editor 
      initText={text}
      updateText={val => handleTextChange(val)}/>
      <Preview text={parsedText}/>
    </div>
  );
}

