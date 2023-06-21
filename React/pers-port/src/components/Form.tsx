import React from 'react'
import emailjs from '@emailjs/browser';

export default function Form (){
    const [formData, setFormData] = React.useState(
        {name: "", company: "", email: "", subject: "", message: ""}
    )

    function handleChange(event : any) {
        setFormData(prevFormData => {
            return {
                ...prevFormData,
                [event.target.name]: event.target.value
            }
        })
    }

    function handleSubmit(event : any){
        event.preventDefault();
        // emailjs.sendForm('0a2a409226', 'YOUR_TEMPLATE_ID', form.current, '12921e5f6211295e6bacfe6580e95e5e-us21')
        // .then((result) => {
        //  // show the user a success message
        // }, (error) => {
        //  // show the user an error
        // });
    }
    return(
        <form onSubmit={handleSubmit} className='form-group'>
            <div className='row my-3 form-column'>
                <div className='col'>
                    <div className='input-group mb-3'>
                    <input type="text" placeholder="Name"
                    onChange={handleChange}
                    name="name"
                    value={formData.name}
                    className='form-control bg-dark input-field'/>
                    <input type="text" placeholder="Company"
                    onChange={handleChange}
                    name="company"
                    value={formData.company}
                    className='form-control bg-dark input-field'/>
                </div>
                    <input type="text" placeholder="Email"
                    onChange={handleChange}
                    name="email"
                    value={formData.email}
                    className='form-control bg-dark input-field mb-3'/>

                    <input type="text" placeholder="Subject"
                    onChange={handleChange}
                    name="subject"
                    value={formData.subject}
                    className='form-control bg-dark input-field'/>
                </div> 
                <div className='col'>
                    <textarea 
                    placeholder="Message"
                    onChange={handleChange}
                    name="message"
                    value={formData.message}
                    className='form-control bg-dark input-field textarea-input'
                    />
                </div>
            </div>
            
            
            
            <button className='btn bg-dark blue-button d-block'>Submit</button>
        </form>
    )
}