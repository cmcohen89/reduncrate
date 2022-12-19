import { BsGithub, BsLinkedin } from "react-icons/bs";
import Footer from "../Footer/Footer";
import CategoriesNav from "../Navigation/CategoriesNav";
import Navigation from "../Navigation/Navigation";
import SupplyNavBar from "../SingleProduct/SupplyNavBar/SupplyNavBar";
import './MeetTeam.css'

const MeetTeam = () => {
  function shuffle(arr) {
    let curr = arr.length
    let randomNum;

    while (curr > 0) {
      randomNum = Math.floor(Math.random() * curr);
      curr--;
      [arr[curr], arr[randomNum]] = [arr[randomNum], arr[curr]];
    }

    return arr;
  }

  const devs = [
    {
      name: 'CHRISTOPHER COHEN',
      gitHub: 'https://github.com/cmcohen89',
      linkedIn: 'https://www.linkedin.com/in/christopher-cohen-94ab06236/',
      img: 'https://avatars.githubusercontent.com/u/103705214?v=4'
    },
    {
      name: 'SARA DUNLOP',
      gitHub: 'https://github.com/Risclover',
      linkedIn: 'https://www.linkedin.com/in/sara-dunlop-66375a146/',
      img: 'https://avatars.githubusercontent.com/u/85785443?v=4'
    },
    {
      name: 'MIKE MILLER',
      gitHub: 'https://github.com/mikemillercodes',
      linkedIn: 'https://www.linkedin.com/in/mike-miller-546a1832/',
      img: 'https://avatars.githubusercontent.com/u/107960217?v=4'
    },
    {
      name: 'GRAY NANCE',
      gitHub: 'https://github.com/g-wn',
      linkedIn: 'https://www.linkedin.com/in/gray-nance/',
      img: 'https://avatars.githubusercontent.com/u/98988710?v=4'
    }
  ]

  shuffle(devs)

  return (
    <>
      <Navigation />
      <CategoriesNav />
      <h1 className="meet-title">Meet the Team</h1>
      <div className="all-devs-container">
        <div className="all-devs">
          {devs.map((dev, idx) => (
            <div key={idx} className="one-dev">
              <img className='dev-pic' src={dev.img} alt='dev'></img>
              <h1 className="dev-name">{dev.name}</h1>
              <div className="meet-dev-links">
                <a className='meet-dev-link' target='_blank' href={dev.gitHub} rel='noreferrer'><BsGithub size={35} /></a>
                <a className='meet-dev-link' target='_blank' href={dev.linkedIn} rel='noreferrer'><BsLinkedin size={35} /></a>
              </div>
            </div>
          ))}
        </div>
      </div>
      <Footer />
    </>
  )
}

export default MeetTeam;
