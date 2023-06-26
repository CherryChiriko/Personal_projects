import React from 'react'
import { projectsData } from '../../assets/projectsData'
import ProjectCard from '../../components/ProjectCard'

export default function ProjectInfo (){
    const projects = projectsData.map((project : any) => {
        return (
        <ProjectCard key={project.id} {...project}/>
      )})
    return(
        <div className='portfolio-div flex-column'>
            <div className='section-header'>
                <h1 className='main-title mx-5 my-0'>Portfolio</h1>
            </div>
            <div className='section-body'>
                <h4 className='text-bold'>React projects</h4>
                <div className='blue-line'></div>
                {projects}
            </div>
        </div>
    )
}