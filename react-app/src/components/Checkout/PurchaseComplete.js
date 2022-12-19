import { useHistory } from "react-router-dom";
import CategoriesNav from "../Navigation/CategoriesNav";
import Navigation from "../Navigation/Navigation";
import './PurchaseComplete.css'

const PurchaseComplete = () => {
  const history = useHistory();
  return (
    <>
      <Navigation />
      <CategoriesNav />
      <div className="checkout-page">
        <h1 className='purchase-title'>PURCHASE COMPLETE!</h1>
        <div className="cart-checkout-button-container">
          <button className="cart-checkout-button" onClick={() => {
            history.push('/');
          }}>RETURN HOME</button>
        </div>
        <div className="cart-checkout-button-container">
          <button className="cart-checkout-button" onClick={() => {
            history.push('/profile');
          }}>GO TO PROFILE</button>
        </div>
        <div className="cart-checkout-button-container">
          <button className="cart-checkout-button" onClick={() => {
            history.push('/order-history');
          }}>GO TO ORDER HISTORY</button>
        </div>
      </div>
    </>
  )
}

export default PurchaseComplete;
