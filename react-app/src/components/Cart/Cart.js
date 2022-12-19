import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink } from "react-router-dom";
import { getCart } from "../../store/cart";
import { removeCartItem } from "../../store/cart_items";
import SelectField from "../SelectField/SelectField";
import "./Cart.css";

const Cart = ({ setShowCartModal }) => {
  const dispatch = useDispatch();
  const cart = useSelector((state) => state.cart);

  useEffect(() => {
    dispatch(getCart());
  }, [dispatch]);

  const usDollar = Intl.NumberFormat("en-US");
  let totalPrice = 0;


  if (!cart || !cart.cartItems) return null;

  return (
    <div>
      <div className="cart-header">
        <h1 className="cart-title">YOUR CRATE</h1>
        <button
          className="cart-header-x"
          onClick={() => setShowCartModal(false)}
        >
          <i className="fa-sharp fa-solid fa-xmark"></i>
        </button>
      </div>
      <div className="cart-item-container">
        {Object.values(cart.cartItems).map((item) => (
          <div className="one-cart-item" key={item.id}>
            <NavLink to={`/products/${item.product.id}`}>
              <img
                className="cart-item-image"
                src={item.product.cartImgUrl ? item.product.cartImgUrl : item.product.productImages[item.product.previewImgId].url}
                alt="cart item"
              />
            </NavLink>
            <div className="cart-item-title-and-remove">
              {item.product.title}
              <button
                className="cart-remove-button"
                onClick={async (e) => {
                  e.preventDefault();
                  await dispatch(removeCartItem(item.id));
                  dispatch(getCart());
                }}
              >
                REMOVE
              </button>
            </div>
            <div className="cart-quantity-and-price">
              <div className="cart-price">
                ${usDollar.format(item.product.price * item.quantity)}
                {(totalPrice += item.product.price * item.quantity) && false}
              </div>
              <div className="cart-quantity-container">
                <SelectField currentItem={item} />
              </div>
            </div>
          </div>
        ))}
      </div>
      <div className="cart-checkout-div">
        <div className="cart-total-container">
          <span className="cart-total-text">TOTAL</span>
          <span className="cart-total-price">
            ${usDollar.format(totalPrice)}
          </span>
        </div>
        <div className="cart-checkout-button-container">
          {Object.values(cart.cartItems).length > 0 ?
            <NavLink to='/checkout'><button className="cart-checkout-button" onClick={() => setShowCartModal(false)}>CHECKOUT</button></NavLink>
            :
            <button className="cart-checkout-button-disabled">ADD AN ITEM TO ENABLE CHECKOUT</button>
          }
        </div>
        <div className="cart-checkout-text-container">
          <p className="cart-checkout-text">
            FREE SHIPPING OVER $200 IN THE U.S. INTERNATIONAL RATES AT CHECKOUT.
          </p>
        </div>
        <div className="cart-checkout-text-container">
          <p className="cart-checkout-text">
            WE'RE PROUD TO OFFER A DISCOUNT TO MILITARY, NURSES, AND FIRST
            RESPONDERS.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Cart;
