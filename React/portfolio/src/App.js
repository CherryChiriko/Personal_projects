import { Route, Routes } from 'react-router-dom';
import './App.scss';
import Layout from './components/Layout';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Layout/>} >
          <Route index element={<Home/>} >
        </Route>

      </Routes>
    </>
  );
}

export default App;
