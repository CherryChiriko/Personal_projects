import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Layout from './pages/layouts/Layout';
import Home from './pages/Home';
import Contacts from './pages/Contacts';
import Skills from './pages/Skills';
import Portfolio from './pages/Portfolio';
import ProjectInfo from './pages/subpages/ProjectInfo';
import ProjectList from './pages/subpages/ProjectList';
import PortfolioLayout from './pages/layouts/PortfolioLayout';


export default function App()  {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />} >
          <Route index element={<Home />} />
          <Route path="skills" element={<Skills />} />

          <Route path="portfolio" element={<PortfolioLayout />} >
            <Route index element={<Portfolio />}/>
            <Route path=":id" element={<ProjectInfo />} />
            <Route path="list" element={<ProjectList />} />
          </Route>
          
          <Route path="contacts" element={<Contacts />} />
        </Route>
      </Routes>
    </BrowserRouter>
    </>
  );
}
