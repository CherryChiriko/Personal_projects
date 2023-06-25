import React from 'react'

import ContactInfo from '../components/ConctactInfo'

import { contactsData } from '../assets/contactData'
import Form from '../components/Form'

export default function Contacts (){
    const contacts = contactsData.map(contact => {
        return (
        <ContactInfo key={contact.id} {...contact}/>
      )})
    return(
        <div className='flex-standard flex-column'>
            <div className='section-header'>
                <h1 className='main-title mx-5 my-0'>Contacts</h1>
            </div>
            <div className='section-body '>
                <div className="row div-contacts">
                    <div className='col-lg-4 col'>
                        {contacts}
                    </div>
                    <div className='col-lg-8 col'>
                        <h4 className='text-bold'>Contact me!</h4>
                        <div className='blue-line'></div>
                        <Form />
                    </div> 
                </div>
            </div>
        </div>
    )
}