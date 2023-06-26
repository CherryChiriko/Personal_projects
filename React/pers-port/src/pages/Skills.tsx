import React from 'react'
import './Skills.css'
import Skill from '../components/Skill'
import { skillsData } from '../assets/skillsData'
import { interestsData } from '../assets/interestsData';
import Interests from '../components/Interests';

export default function Skills (){
    function makeSkill(type: string) : JSX.Element[] {
        return skillsData
        .filter(skill => skill.type === type)
        .map(skill => <Skill key={skill.id} {...skill} />);
    }
    const frontEndSkills = makeSkill('FE');
    const backEndSkills = makeSkill('BE');
    const languageSkills = makeSkill('L');

    const interests = interestsData.map( interest => (
        <Interests key={interest.id} {...interest} />
    ))

    return(
        <div className='flex-standard flex-column'>
            <div className='section-header'>
                <h1 className='main-title mx-5 my-0'>Skills</h1>
            </div>
            <div className='section-body'>
                <div className='row'>
                    <div className='col'>
                        <h4 className='text-bold'>Front-end skills</h4>
                        <div className='blue-line'></div>
                        {frontEndSkills}
                        <h4 className='text-bold'>Back-end skills</h4>
                        <div className='blue-line'></div>
                        {backEndSkills}
                    </div>
                    <div className='col ms-4'>
                        <h4 className='text-bold'>Language skills</h4>
                        <div className='blue-line'></div>
                        {languageSkills}
                        <h4 className='text-bold'>Interests</h4>
                        <div className='blue-line'></div>
                        <div className='d-flex flex-row interests-div'>
                            {interests}
                        </div>
                    </div>
                </div>
            
            </div>
        </div>
    )
}