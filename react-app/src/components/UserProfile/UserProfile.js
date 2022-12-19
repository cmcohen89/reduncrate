import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import { AiOutlinePlusCircle } from "react-icons/ai";
import { getProducts, deleteProduct } from "../../store/all_products";
import Navigation from "../Navigation/Navigation";
import Footer from "../Footer/Footer";
import "./UserProfile.css";
import ProfileNav from '../ProfileNav/ProfileNav';

const UserProfile = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const user = useSelector((state) => state.session.user);

  const allProducts = useSelector(state => Object.values(state.products));
  const userProducts = allProducts.filter(product => product.productOwner.id === user.id)

  useEffect(() => {
    dispatch(getProducts());
  }, [dispatch]);

  if (!allProducts || allProducts.length === 0) return null;

  return (
    <>
      <Navigation />
      <ProfileNav />
      <div className="my-listings">
        <div className="hidden-spacer"></div>
        <span className="my-listings-title">{`${user.first_name}'s Listings`}</span>
        <NavLink className="add-product-btn" to={"/products/new"}>
          <AiOutlinePlusCircle size={30} />
        </NavLink>
      </div>
      <div className="profile-page">

        {userProducts.length ?
          <div className="user-products">
            {userProducts.map(
              (product, idx) =>
                <div key={idx} className="product-details">
                  <NavLink className="image" to={`/products/${product.id}`}>
                    <img
                      alt="product-main-img"
                      className="product-preview-img"
                      src={product.productImages[product.previewImgId].url}
                    ></img>
                  </NavLink>
                  {product.title}
                  <button
                    className="edit-listing"
                    onClick={() => {
                      history.push(`/products/${product.id}/update`);
                    }}
                  >
                    Edit Product Details
                  </button>
                  <button
                    className="edit-listing"
                    onClick={() => {
                      history.push(`/${product.id}/images/add-edit`);
                    }}
                  >
                    Add/Edit Images
                  </button>
                  <button
                    className="delete-listing"
                    onClick={async (e) => {
                      e.preventDefault();
                      await dispatch(deleteProduct(product.id));
                      dispatch(getProducts());
                    }}
                  >
                    Delete From Reduncrate
                  </button>
                </div>
            )}
          </div> : <h1 className="empty-message">You don't have any listings!</h1>
        }
      </div>
      <Footer />
    </>
  );
};

export default UserProfile;
