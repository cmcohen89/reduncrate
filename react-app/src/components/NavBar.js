
import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import { Modal } from '../context/Modal';
import LoginForm from './auth/LoginForm';

const NavBar = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <nav>
        <ul>
          <li>
            <NavLink to='/' exact={true} activeClassName='active'>
              Home
            </NavLink>
          </li>
          <li>
            <button onClick={() => setShowModal(true)}>
              Login
            </button>
            {showModal && <Modal onClose={() => setShowModal(false)}><LoginForm /></Modal>}
          </li>
          <li>
            <NavLink to='/sign-up' exact={true} activeClassName='active'>
              Sign Up
            </NavLink>
          </li>
          <li>
            <NavLink to='/users' exact={true} activeClassName='active'>
              Users
            </NavLink>
          </li>
          <li>
            <LogoutButton />
          </li>
        </ul>
      </nav>
    </>
  );
}

export default NavBar;
