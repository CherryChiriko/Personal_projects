import React from 'react'
import Home from "./pages/Home"
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './pages/Layout'
import JournalEntry from './pages/JournalEntry'

export default function App (){

    return (
      <>
      <BrowserRouter>      
      <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Home />}/>
        <Route path="/:entry-title" element={<JournalEntry />}/>
      </Route>
      </Routes>      
      </BrowserRouter> 
      </>
    )
}

