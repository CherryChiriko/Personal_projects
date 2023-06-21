import React from 'react'

import ContactInfo from '../components/ConctactInfo'

import { contactsData } from '../assets/data'
import Form from '../components/Form'

export default function Contacts (){
    const contacts = contactsData.map(contact => {
        return (
        <ContactInfo key={contact.id} {...contact}/>
      )})
    return(
        <div className='main-div flex-column'>
            <div className='section-header'>
                <h1 className='main-title mx-5 my-0'>Contacts</h1>
            </div>
            <div className='section-body '>
                <div className="row div-contacts">
                    <div className='col-4'>
                        {contacts}
                    </div>
                    <div className='col-8'>
                        <Form />
                    </div> 
                </div>
            </div>
        </div>
    )
}