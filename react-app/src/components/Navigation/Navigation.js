import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import "./Navigation.css";
import { Modal } from "../../context/Modal";
import LoginForm from "../auth/LoginForm";
import SignUpForm from "../auth/SignUpForm";
import { useDispatch, useSelector } from "react-redux";
import LogoutButton from "../auth/LogoutButton";
import { NavLink } from "react-router-dom";
import Cart from "../Cart/Cart";
import MeetDropdown from "../MeetDropdown/MeetDropdown";
import { getCart } from "../../store/cart";

function Navigation() {
  const dispatch = useDispatch();
  const [showLoginModal, setShowLoginModal] = useState(false);
  const [showSignupModal, setShowSignupModal] = useState(false);
  const [showCartModal, setShowCartModal] = useState(false);
  const [showMeet, setShowMeet] = useState(false);
  const user = useSelector((state) => state.session.user);
  const cart = useSelector((state) => state.cart);
  const history = useHistory();

  let cartItemCount;
  if (cart && cart.cartItems) cartItemCount = Object.keys(cart.cartItems).length

  useEffect(() => {
    if (user) dispatch(getCart());
  }, [dispatch, user]);

  return (
    <>
      <header className="splash-page-header">
        <div className={`cart-modal cart-container ${showCartModal ? "cart-show" : ""}`}>
          <Cart setShowCartModal={setShowCartModal} />
        </div>
        <div
          className={`cart-overlay ${showCartModal ? "cart-show" : ""}`}
          onClick={() => setShowCartModal(!showCartModal)}
        />
        <div className="splash-page-top-bar-container">
          <div className="header-top-bar">
            <div className="topbar-wrapper">
              <div className="topbar">
                <div className="header-top-bar-left">
                  <span
                    className="meet-button"
                    onClick={() => history.push('/meet-the-team')}
                    onMouseOver={() => setShowMeet(true)}
                    onMouseOut={() => setShowMeet(false)}
                  >
                    MEET THE TEAM
                    <span className={showMeet ? 'show-meet meet-button-hover' : "no-show-meet"}><MeetDropdown /></span>
                  </span>
                </div>
                <div className="header-top-bar-middle">
                  <ul>
                    <li>
                      <a
                        target="_blank"
                        className="header-link"
                        href="https://www.linkedin.com/in/jwily/"
                        rel='noreferrer'
                      >
                        JOHN LEE | PROJECT ADVISOR
                      </a>
                    </li>
                    <li>
                      <a
                        target="_blank"
                        className="header-link"
                        href="https://www.linkedin.com/in/brad-simpson-a6b1b7b2/"
                        rel="noreferrer"
                      >
                        BRAD SIMPSON | MOD INSTRUCTOR
                      </a>
                    </li>
                  </ul>
                </div>
                {!user ? (
                  <div className="header-top-bar-right">
                    <button
                      className="login-button"
                      onClick={() => setShowLoginModal(true)}
                    >
                      LOG IN
                    </button>&nbsp;&nbsp; | &nbsp;&nbsp;
                    <button
                      className="login-button"
                      onClick={() => setShowSignupModal(true)}
                    >
                      SIGN UP
                    </button>
                    {showLoginModal && (
                      <Modal onClose={() => setShowLoginModal(false)}>
                        <LoginForm setShowLoginModal={setShowLoginModal} />
                      </Modal>
                    )}
                    {showSignupModal && (
                      <Modal onClose={() => setShowSignupModal(false)}>
                        <SignUpForm />
                      </Modal>
                    )}
                  </div>
                ) : (
                  <div className="header-top-bar-right">
                    <LogoutButton setShowLoginModal={setShowLoginModal} setShowSignupModal={setShowSignupModal} />&nbsp;&nbsp; | &nbsp;&nbsp;
                    <button
                      className="profile-button"
                      onClick={() => history.push(`/profile`)}
                    >
                      PROFILE
                    </button>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
        <div className="header-bottom-bar">
          <div></div>
          <div className="header-logo">
            <NavLink to="/">
              <img
                src="/images/reduncrate-white2.png"
                className="reduncrate-logo"
                alt="header-logo"
              ></img>
            </NavLink>
          </div>
          <div className="splash-header-icons-wrapper">
            <div className="splash-header-icons">
              <NavLink to="/search" className="magnifying-glass-link">
                <i className="fa-solid fa-magnifying-glass"></i>
              </NavLink>
              <button
                className="nav-bar-crate-button"
                onClick={() => user ? setShowCartModal(true) : setShowLoginModal(true)}
              >
                <i className="fa-sharp fa-solid fa-box"></i>
              </button>
              {user ? (cartItemCount ? <span className="cart-item-count-splash">{cartItemCount}</span> : "") : ""}
            </div>
          </div>
        </div>
      </header>
    </>
  );
}

export default Navigation;
