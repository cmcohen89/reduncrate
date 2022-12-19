import React from "react";
import { NavLink } from "react-router-dom";
import "./SuggestedProducts.css";

export default function SuggestedProduct({ product }) {

  return (
    <div className="suggested-product-item">
      <NavLink to={`/products/${product.id}`}>
        <img className='suggested-img' src={product.cartImgUrl ? product.cartImgUrl : product.productImages[product.previewImgId].url} alt="Example" />
        <span className="suggested-products-label">
          {product.title} &nbsp;/&nbsp; ${product.price}
        </span>
      </NavLink>
    </div>
  );
}
