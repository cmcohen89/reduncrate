import React, { useState } from "react";
import { useSelector } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import SupplyHeader from "./SupplyHeader/SupplyHeader";
import "./SupplyNavBar.css";
import { Modal } from "../../../context/Modal";
import LoginForm from "../../auth/LoginForm";
import SignUpForm from "../../auth/SignUpForm";
import LogoutButton from "../../auth/LogoutButton";
import Cart from "../../Cart/Cart";
export default function SupplyNavBar() {
  const history = useHistory();
  const [showCartModal, setShowCartModal] = useState(false);
  const [showLoginModal, setShowLoginModal] = useState(false);
  const [showSignupModal, setShowSignupModal] = useState(false);
  const user = useSelector((state) => state.session.user);
  const cart = useSelector(state => state.cart);

  let cartItemCount;
  if (cart && cart.cartItems) cartItemCount = Object.keys(cart.cartItems).length

  return (
    <div className="supply-nav-bar">
      <div className={`cart-modal cart-container ${showCartModal ? "cart-show" : ""}`}>
        <Cart setShowCartModal={setShowCartModal} />
      </div>
      <div
        className={`cart-overlay ${showCartModal ? "cart-show" : ""}`}
        onClick={() => setShowCartModal(!showCartModal)}
      />
      <div className="topbar-wrapper">
        <div className="topbar">
          <div className="topbar-left">
            <NavLink to="/">
              {" "}
              <img
                src="/images/reduncrate-white2.png"
                className="reduncrate-logo-mini"
                alt="header-logo"
              ></img>
            </NavLink>
          </div>
          <div className="topbar-middle">
            <ul>
              <li>
                <a
                  rel="noreferrer"
                  target="_blank"
                  className="header-link"
                  href="https://www.linkedin.com/in/jwily/"
                >
                  JOHN LEE | PROJECT ADVISOR
                </a>
              </li>
              <li>
                <a
                  rel="noreferrer"
                  target="_blank"
                  className="header-link"
                  href="https://www.linkedin.com/in/brad-simpson-a6b1b7b2/"
                >
                  BRAD SIMPSON | MOD INSTRUCTOR
                </a>
              </li>
            </ul>
          </div>
          <div className="supply-nav-rightbtns">
            {!user ? (
              <div>
                <button
                  className="login-button"
                  onClick={() => setShowLoginModal(true)}
                >
                  LOG IN
                </button>
                &nbsp;&nbsp; | &nbsp;&nbsp;
                <button
                  className="login-button"
                  onClick={() => setShowSignupModal(true)}
                >
                  SIGN UP
                </button>
                <div className="supply-icons-alt">
                  &nbsp;&nbsp; | &nbsp;&nbsp;
                  <NavLink to="/search">
                    <i className="fa-solid fa-magnifying-glass"></i>
                  </NavLink>
                  {user ? (
                    <button
                      className="supply-header-crate-button"
                      onClick={() => setShowCartModal(true)}
                    >
                      <i className="fa-solid fa-box crate-icon"></i>
                    </button>
                  ) : (
                    <button
                      className="supply-header-crate-button"
                      onClick={() => setShowLoginModal(true)}
                    >
                      <i className="fa-solid fa-box crate-icon"></i>
                    </button>
                  )}
                  {showLoginModal && (
                    <Modal onClose={() => setShowLoginModal(false)}>
                      <LoginForm setShowCartModal={setShowLoginModal} />
                    </Modal>
                  )}
                  <span className="cart-badge"></span>
                </div>
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
              <div>
                <LogoutButton setShowLoginModal={setShowLoginModal} setShowSignupModal={setShowSignupModal} />
                &nbsp;&nbsp; | &nbsp;&nbsp;
                <button
                  className="profile-button"
                  onClick={() => history.push(`/profile`)}
                >
                  PROFILE
                </button>
                <div className="supply-icons-alt">
                  &nbsp;&nbsp; | &nbsp;&nbsp;
                  <NavLink to="/search">
                    <i className="fa-solid fa-magnifying-glass"></i>
                  </NavLink>
                  {user ? (
                    <button
                      className="supply-header-crate-button"
                      onClick={() => setShowCartModal(true)}
                    >
                      <i className="fa-solid fa-box crate-icon"></i>
                    </button>
                  ) : (
                    <button
                      className="supply-header-crate-button"
                      onClick={() => setShowLoginModal(true)}
                    >
                      <i className="fa-solid fa-box crate-icon"></i>
                    </button>
                  )}
                  {showLoginModal && (
                    <Modal onClose={() => setShowLoginModal(false)}>
                      <LoginForm setShowCartModal={setShowLoginModal} />
                    </Modal>
                  )}
                  {user ? (cartItemCount ? <span className="cart-item-count-single-alt">{cartItemCount}</span> : "") : ""}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
      <SupplyHeader />
    </div>
  );
}
