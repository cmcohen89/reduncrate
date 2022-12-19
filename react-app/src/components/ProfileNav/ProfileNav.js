import { NavLink } from 'react-router-dom';
import './ProfileNav.css'

const ProfileNav = () => {
  return (
    <div className='profile-nav-container'>
      <ul className='profile-nav-list'>
        <li className='profile-nav-sizer'><NavLink className='profile-nav-list-item' to='/order-history'>My Orders</NavLink></li>
        <li className='profile-nav-sizer'><NavLink className='profile-nav-list-item' to='/profile'>My Listings</NavLink></li>
        <li className='profile-nav-sizer'><NavLink className='profile-nav-list-item' to='/my-stash'>My Stash</NavLink></li>
      </ul>
    </div>
  )
}

export default ProfileNav;
