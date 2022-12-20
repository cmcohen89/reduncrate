import React, { useState } from "react";
import { NavLink, useHistory } from "react-router-dom";
import { useSelector } from "react-redux";
import "./SupplyHeader.css";
import { Modal } from "../../../../context/Modal";
import Cart from "../../../Cart/Cart";
import LoginForm from "../../../auth/LoginForm";

export default function SupplyHeader() {
  const [showCartModal, setShowCartModal] = useState(false);
  const [showLoginModal, setShowLoginModal] = useState(false);

  const history = useHistory();
  const user = useSelector((state) => state.session.user);
  const cart = useSelector(state => state.cart)

  let cartItemCount;
  if (cart && cart.cartItems) cartItemCount = Object.keys(cart.cartItems).length

  return (
    <>
      <div className={`cart-modal cart-container ${showCartModal ? "cart-show" : ""}`}>
        <Cart setShowCartModal={setShowCartModal} />
      </div>
      <div
        className={`cart-overlay ${showCartModal ? "cart-show" : ""}`}
        onClick={() => setShowCartModal(!showCartModal)}
      />
      <div className="supply-header">
        <div className="supply-header-title">
          <h1 onClick={() => history.push('/')}>
            REDUNCRATE SUPPLY<sup>™</sup>
          </h1>
          <p>
            OBJECTS OF DESIRE & TOOLS OF THE TRADE, STOCKED & SHIPPED BY
            REDUNCRATE.
          </p>
          <div className="supply-icons">
            <NavLink to="/search" className='magnifying-glass-link'>
              <i className="fa-solid fa-magnifying-glass supply-magnifying-glass"></i>
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
                <LoginForm setShowLoginModal={setShowLoginModal} />
              </Modal>
            )}
            {user ? (cartItemCount ? <span className="cart-item-count-single">{cartItemCount}</span> : "") : ""}
          </div>
        </div>
        <div className="supply-header-categories">
          <div className="categorybar-top">
            {/* <ul>
                        <li>NEW ITEMS &nbsp;&nbsp;</li>/
                        <li>&nbsp;&nbsp; TOP PICKS &nbsp;&nbsp;</li>/
                        <li>&nbsp;&nbsp; BACK IN STOCK &nbsp;&nbsp;</li>/
                        <li>&nbsp;&nbsp; BRANDS &nbsp;&nbsp;</li>/
                        <li className="nav-surplus">&nbsp;&nbsp; SURPLUS</li>
                    </ul> */}
          </div>
          {/* <div className="categorybar-bottom">
                    <ul>
                        <li>APPAREL &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; HOME &nbsp;&nbsp;</li>/
                        <li>&nbsp;&nbsp; ART &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; BOOKS &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; BAGS &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; GROOMING &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; WATCHES &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; GEAR &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; TECH &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; TOYS &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; SPORT &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; VINTAGE &nbsp;&nbsp;/</li>
                        <li>&nbsp;&nbsp; VEHICLES</li>
                    </ul>
                </div> */}
        </div>
      </div>
    </>
  );
}
