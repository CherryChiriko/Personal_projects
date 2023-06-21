import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Layout from './pages/Layout';
import Home from './pages/Home';
import Contacts from './pages/Contacts';
import Skills from './pages/Skills';
import Portfolio from './pages/Portfolio';


export default function App()  {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />} >
          <Route path="/" element={<Home />} />
          <Route path="/skills" element={<Skills />} />
          <Route path="/portfolio" element={<Portfolio />} />
          <Route path="/contacts" element={<Contacts />} />
        </Route>
      </Routes>
    </BrowserRouter>
    </>
  );
}
