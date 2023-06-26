import React from "react"
import { Outlet } from "react-router-dom"

export default function PortfolioLayout() {
    return (
        <div className='flex-standard'>
            <div className='section-header'>
                <h1 className='main-title mx-5 my-0'>Portfolio</h1>
            </div>
            <Outlet />
        </div>
    )
}