import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { getCartHistory } from '../../store/cart';
import Footer from '../Footer/Footer';
import Navigation from '../Navigation/Navigation';
import ProfileNav from '../ProfileNav/ProfileNav';
import './OrderHistory.css';

const OrderHistory = () => {
  const dispatch = useDispatch();
  const purchasedCarts = useSelector(state => state.cart.orderHistory)
  const user = useSelector(state => state.session.user)

  useEffect(() => {
    dispatch(getCartHistory());
  }, [dispatch]);


  const usDollar = Intl.NumberFormat("en-US");

  if (!purchasedCarts) return null;

  return (
    <>
      <Navigation />
      <ProfileNav />
      <div className="checkout-page">
        <h1 className='checkout-title'>{user.first_name}'S ORDER HISTORY</h1>
        {purchasedCarts.length ?

          <div className='order-history-grid'>
            {purchasedCarts.map(cart => (
              <div key={cart.id} className="checkout-items-container">
                <div className="checkout-items">
                  {Object.values(cart.cartItems).map((item, idx) => (
                    <div key={idx} className="one-checkout-item">
                      <NavLink to={`/products/${item.product.id}`}>
                        <img
                          className='cart-item-image'
                          src={item.product.cartImgUrl ? item.product.cartImgUrl : item.product.productImages[item.product.previewImgId].url}
                          alt='cart item'
                        />
                      </NavLink>
                      <div className='checkout-item-title'>
                        {item.product.title}
                      </div>
                      <div className="checkout-item-quantity-and-price">
                        <div className='checkout-item-price'>
                          ${usDollar.format(item.product.price * item.quantity)}.00
                        </div>
                        <div className='checkout-item-quantity'>
                          QTY: <span className="checkout-quantity">{item.quantity}</span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
                <div className="checkout-total-container">
                  <span className="checkout-total">TOTAL</span>
                  <span className="checkout-price">USD ${usDollar.format(cart.total)}</span>
                </div>
              </div>
            ))}
          </div> : <h1 className='empty-message'>You haven't made any purchases!</h1>}
      </div>
      <Footer />
    </>
  )
}

export default OrderHistory;
