import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getProducts } from "../../store/all_products";
import { NavLink } from "react-router-dom";
import Navigation from "../Navigation/Navigation";
import { searchQuery } from "../../store/all_products";
import "./Search.css";

export default function Search() {
  const [searchValue, setSearchValue] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [searchResults, setSearchResults] = useState([]);
  const dispatch = useDispatch();

  const products = useSelector((state) => Object.values(state.products));

  useEffect(() => {
    dispatch(getProducts());
  }, [dispatch]);

  const handleChange = (e) => {
    e.preventDefault();
    setSearchValue(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSearchResults(await dispatch(searchQuery(searchValue)).query);
    setTimeout(() => setSubmitted(true), 300);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSubmit(e);
    }
  };

  return (
    <div>
      <Navigation />
      <div className="search-container">
        <div className="search-area">
          <div className="search-form">
            <p className="search-title">Search for something on Reduncrate.</p>
            <div className="search-field">
              <label className="searchbar-search">Search</label>
              <input
                onKeyPress={(e) => handleKeyPress(e)}
                className="searchbar"
                placeholder="Enter a search term."
                type="text"
                onChange={handleChange}
                value={searchValue}
              />
            </div>
            <button className="submit-search" onClick={handleSubmit}>
              Submit
            </button>
          </div>
        </div>
        <div className="search-results">
          {submitted ? (
            Object.keys(products).length > 0 ? (
              products.map((product) => (
                <div className="search-result">
                  <NavLink to={`/products/${product.id}`}>
                    <img
                      src={product.productImages[product.previewImgId].url}
                      alt="search-result-product"
                    />
                  </NavLink>
                  <div className="search-result-details">
                    {/* {" "} */}
                    <NavLink to={`/products/${product.id}`}>
                      {product.title}
                    </NavLink>
                  </div>
                </div>
              ))
            ) : (
              <div className="no-results">No search results found.</div>
            )
          ) : (
            ""
          )}
        </div>
      </div>
    </div>
  );
}
