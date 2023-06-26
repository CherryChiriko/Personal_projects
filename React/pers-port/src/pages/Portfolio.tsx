import React from 'react'
import ProjectCard from '../components/ProjectCard'
import { projectsData } from '../assets/projectsData'

export default function Portfolio (){
    const projects = projectsData.map(project => {
        return (
        <ProjectCard key={project.id} {...project}/>
      )})
    return(
        <div className='section-body'>
            <h4 className='text-bold'>React projects</h4>
            <div className='blue-line'></div>
            <div className='d-flex flex-row projects-div'>
                {projects}
            </div>
            <h4 className='text-bold mt-2'>Angular projects</h4>
            <div className='blue-line'></div>
            <h4 className='text-bold mt-2'>Python projects</h4>
            <div className='blue-line'></div>
        </div>
    )
}