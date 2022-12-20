import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink } from "react-router-dom";
import { getProducts } from "../../store/all_products";
import "./ProductIndex.css";
import Navigation from "../Navigation/Navigation";
import Footer from "../Footer/Footer";
import CategoriesNav from '../Navigation/CategoriesNav';

const ProductIndex = () => {
  const dispatch = useDispatch();
  const [products, setProducts] = useState([]);
  const user = useSelector((state) => state.session.user)

  function shuffle(array) {
    let currentIndex = array.length, temporaryValue, randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) {

      // Create a random index to pick from the original array
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;

      // Cache the value, and swap it with the current element
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }

    return array;
  }

  useEffect(() => {
    (async function fetchProducts() {
      const allProducts = await dispatch(getProducts());
      const shuffled = shuffle(allProducts.Products);
      setProducts(shuffled);
    })()
  }, [dispatch, user]);

  if (!products || products.length === 0) return null;

  return (
    <>
      <Navigation />
      <CategoriesNav />
      <div
        className="all-products-index">
        <div className="featured-product">
          <NavLink className="product-link" to={`/products/${products[0].id}`}>
            <img
              alt="main-product-img"
              className="featured-product-image"
              src={products[0].productImages[products[0].previewImgId].url}
            ></img>
          </NavLink>
          <div className="featured-product-text">
            <h6 className="featured-product-category">
              <NavLink to={`/category/${products[0].productCategory.name}`}>
                {products[0].productCategory.name.toUpperCase()}
              </NavLink>
            </h6>
            <h1 className="featured-product-title">
              <NavLink
                className="product-link"
                to={`/products/${products[0].id}`}
              >
                {products[0].title}
              </NavLink>
            </h1>
            <p className="featured-product-description">
              <NavLink
                className="product-link"
                to={`/products/${products[0].id}`}
              >
                {products[0].description}
              </NavLink>
            </p>
            <span className="featured-product-buy-link">
              <NavLink
                className="product-link-buy"
                to={`/products/${products[0].id}`}
              >
                Buy From Reduncrate Supply
              </NavLink>
            </span>
          </div>
        </div>
        <div className="all-other-products">
          {products.slice(1, 35).map((product) => (
            <div key={product.id} className="all-other-products-one-product">
              <NavLink className="product-link" to={`/products/${product.id}`}>
                <img
                  alt="main-product-img"
                  className="all-other-products-image"
                  src={product.productImages[product.previewImgId].url}
                ></img>
              </NavLink>
              <div className="all-other-products-text">
                <h6 className="featured-product-category">
                  <NavLink
                    className="featured-product-category"
                    to={`/category/${product.productCategory.name.toLowerCase()}`}
                  >
                    {product.productCategory.name.toUpperCase()}
                  </NavLink>
                </h6>
                <h1 className="all-other-products-title">
                  <NavLink
                    className="product-link"
                    to={`/products/${product.id}`}
                  >
                    {product.title.toUpperCase()}
                  </NavLink>
                </h1>
                <p className="all-other-products-description">
                  <NavLink
                    className="product-link"
                    to={`/products/${product.id}`}
                  >
                    {product.description}
                  </NavLink>
                </p>
                <span className="featured-product-buy-link">
                  <NavLink
                    className="product-link-buy"
                    to={`/products/${product.id}`}
                  >
                    Buy From Reduncrate Supply
                  </NavLink>
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
      <Footer />
    </>
  );
};

export default ProductIndex;
