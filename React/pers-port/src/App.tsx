import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Layout from './pages/Layout';
import Home from './pages/Home';


export default function App()  {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />} >
          <Route path="/" element={<Home />} />
        </Route>
      </Routes>
    </BrowserRouter>
    </>
  );
}
