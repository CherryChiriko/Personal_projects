import { Outlet } from 'react-router-dom';
import Sidebar from '../Sidebar';
import './index.scss';

export default function Layout(){
    return (
        <div className="App">
            <Sidebar />
            <div className='page'>
                <span className="tags top-tags">&lt;body&gt;</span>
                <Outlet />
                <span className="tags bottom-tags">&lt;body&gt;<br/></span>
                <span className="bottom-tags-html"></span>
            </div>
        </div>
    )
}