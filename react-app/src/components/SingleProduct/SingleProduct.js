import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams, NavLink } from "react-router-dom";
import { getSingleProduct } from "../../store/one_product";
import { addToFavorites, getFavorites } from "../../store/favorites";
import "./SingleProduct.css";
import Carousel from "./ImageCarousel/Carousel";
import SupplyNavBar from "./SupplyNavBar/SupplyNavBar";
import { postCartItem, editCartItem } from "../../store/cart_items";
import { Modal } from "../../context/Modal";
import Cart from "../Cart/Cart";
import { getCart } from "../../store/cart";
import SuggestedProduct from "./SuggestedProducts/SuggestedProduct";
import LoginForm from "../auth/LoginForm";
import Footer from "../Footer/Footer";
import { getProducts } from "../../store/all_products";

const SingleProduct = () => {
  const dispatch = useDispatch();
  const { id } = useParams();
  const singleProduct = useSelector((state) => state.product[id]);
  const [showCartModal, setShowCartModal] = useState(false);
  const [suggested, setSuggested] = useState([]);
  const [showLoginModal, setShowLoginModal] = useState(false);
  const user = useSelector((state) => state.session.user);
  const favorites = useSelector((state) => state.favorites);

  const cart = useSelector((state) => state.cart);
  let thisCartItem;
  for (let item in cart.cartItems) {
    if (+cart.cartItems[item].productId === +id)
      thisCartItem = cart.cartItems[item];
  }

  const usDollar = Intl.NumberFormat("en-US");

  useEffect(() => {
    dispatch(getSingleProduct(id));
    (async function fetchProducts() {
      const allProducts = await dispatch(getProducts());
      const shuffled = allProducts.Products.slice(0, 87).sort(() => 0.5 - Math.random());
      const selected = shuffled.slice(0, 8);
      setSuggested(selected);
    })();

    if (user) dispatch(getCart());
    if (user) dispatch(getFavorites(user.id));
  }, [dispatch, id, user]);

  let imgList = [];

  if (singleProduct) {
    for (let id in singleProduct.productImages) {
      if (
        singleProduct.productImages[id].productId === singleProduct.id &&
        !singleProduct.productImages[id].url.includes("shopify")
      ) {
        imgList.push(singleProduct.productImages[id].url);
      }
    }
  }

  if (!singleProduct || !favorites) return null;

  return (
    <div className="single-product-page">
      <SupplyNavBar />
      <div className={`cart-modal cart-container ${showCartModal ? "cart-show" : ""}`}>
        <Cart setShowCartModal={setShowCartModal} />
      </div>
      <div
        className={`cart-overlay ${showCartModal ? "cart-show" : ""}`}
        onClick={() => setShowCartModal(!showCartModal)}
      />
      <div className="single-product">
        <Carousel infinite imageLength={imgList.length}>
          {imgList.map((img, idx) => (
            <img key={idx} src={img} alt="single-product" />
          ))}
        </Carousel>
        <div className="single-product-details-wrapper">
          <div className="single-product-details">
            <p className="single-product-category">
              <NavLink
                to={`/category/${singleProduct.productCategory.name.toLowerCase()}`}
              >
                {singleProduct.productCategory.name}
              </NavLink>
            </p>
            <h1>
              {singleProduct.title.toUpperCase()} / ${usDollar.format(singleProduct.price)}
            </h1>
            <p className="single-product-detailed-description">
              {singleProduct.detailedDescription}
            </p>
            <p className="single-product-details-greentxt">
              IN STOCK AND SHIPS FREE WITH EASY RETURNS.
            </p>
            <div className="single-product-details-btns">
              {user ? (
                <button
                  className="single-product-details-btn btn-add-cart"
                  onClick={async (e) => {
                    e.preventDefault();
                    if (thisCartItem) {
                      if (thisCartItem.quantity < 10) {
                        await dispatch(
                          editCartItem(thisCartItem, thisCartItem.quantity + 1)
                        );
                      }
                    } else {
                      await dispatch(postCartItem(singleProduct.id));
                    }
                    await dispatch(getCart());
                    setShowCartModal(true);
                  }}
                >
                  ADD TO CART
                </button>
              ) : (
                <button
                  className="single-product-details-btn btn-add-cart"
                  onClick={() => {
                    setShowLoginModal(true);
                  }}
                >
                  ADD TO CART
                </button>
              )}
              {showLoginModal && (
                <Modal onClose={() => setShowLoginModal(false)}>
                  <LoginForm setShowLoginModal={setShowLoginModal} />
                </Modal>
              )}
              {!favorites[singleProduct.id] ? (
                <button
                  className="single-product-details-btn btn-stash-later"
                  onClick={async (e) => {
                    e.preventDefault();
                    await dispatch(addToFavorites(singleProduct.id));
                    user
                      ? dispatch(getFavorites(user.id))
                      : setShowLoginModal(true);
                  }}
                >
                  STASH FOR LATER
                </button>
              ) : (
                <span className="already-in-stash">Stashed</span>
              )}
            </div>
          </div>
        </div>
        <div className="suggested-products">
          {suggested.length ? suggested.map((product, idx) => (
            <SuggestedProduct key={idx} product={product} />
          )) : <h1 style={{ textAlign: "center", margin: "219px auto" }}>Loading Suggested Products...</h1>}
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default SingleProduct;
