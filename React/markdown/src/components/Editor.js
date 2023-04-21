import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Editor(props) {
  const [value, setValue] = React.useState('');
  const handleChange = (event) => {
      const val = event.target.value;
      setValue(val);
      props.updateText(val)
  };
  return (
    <div className='table rounded'>
        <p className="title">Editor</p>
        <textarea className="form-control"
        id="editor" name="textarea" value={value} 
        defaultValue={props.initText}
        onChange={handleChange}>
        </textarea>
    </div>
  );
}