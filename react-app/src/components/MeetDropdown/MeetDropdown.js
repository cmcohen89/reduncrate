import { useEffect, useState } from "react";
import { BsGithub, BsLinkedin } from "react-icons/bs"
import './MeetDropdown.css'

const MeetDropdown = () => {
  const [devs, setDevs] = useState([]);

  useEffect(() => {
    const devsArr = [
      {
        name: 'CHRIS COHEN',
        gitHub: 'https://github.com/cmcohen89',
        linkedIn: 'https://www.linkedin.com/in/christopher-cohen-94ab06236/'
      },
      {
        name: 'SARA DUNLOP',
        gitHub: 'https://github.com/Risclover',
        linkedIn: 'https://www.linkedin.com/in/sara-dunlop-66375a146/'
      },
      {
        name: 'MIKE MILLER',
        gitHub: 'https://github.com/mikemillercodes',
        linkedIn: 'https://www.linkedin.com/in/mike-miller-546a1832/'
      },
      {
        name: 'GRAY NANCE',
        gitHub: 'https://github.com/g-wn',
        linkedIn: 'https://www.linkedin.com/in/gray-nance/'
      }
    ];

    const shuffledDevs = devsArr.sort(() => 0.5 - Math.random());
    setDevs(shuffledDevs);
  }, [])


  return (
    <div className="meet-team-links-wrapper">
      <ul className="meet-team-links">
        {devs.map((dev, idx) => (
          <li key={idx} className="one-meet-team-link">
            <div>
              {dev.name}
            </div>
            <div className='meet-team-icons'>
              <a className='meet-team-icon' target='_blank' href={dev.gitHub} rel='noreferrer'><BsGithub size={20} /></a>
              <a className='meet-team-icon' target='_blank' href={dev.linkedIn} rel='noreferrer'><BsLinkedin size={20} /></a>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default MeetDropdown;
