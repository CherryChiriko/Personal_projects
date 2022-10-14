import React from 'react'
import ReactDOM from 'react-dom'
import Header from './Header'
import Contacts from './Contacts'
import About from './About'
import Footer from './MainContent'

function Page (){
    return(
      <div className="container2">
      <div className="container1">
        <Header />
        <Contacts />
        <About />
        <Footer />
      </div>
      </div>
    )
}

ReactDOM.render(<Page/>, document.getElementById('root'))