import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './pages/Layout';
import Home from './pages/Home';

export default function App() {
  return (
    <div>
        <BrowserRouter>
        <Routes>
            <Route element={<Layout />}>
              <Route element={<Home/>} path='/'/>
            </Route>
        </Routes>
        </BrowserRouter>
    </div>
  );
}

