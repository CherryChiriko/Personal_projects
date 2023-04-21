import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Editor(props) {
    function getMarkdownText() { console.log(props.text); return { __html: props.text };    }
    return (
      <>
      <div id="preview" className="table rounded">
        
        <p className="title">Preview</p>
        <div className="main-area rounded">
          <div dangerouslySetInnerHTML={getMarkdownText()} />
        </div>
      </div>
      </>
      
    );
  }