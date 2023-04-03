import './App.css';

import Header from './components/Header'
import Contacts from './components/Contacts'
import About from './components/About'
import Footer from './components/Footer'

export default function App (){
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
