import React, { useState } from "react";
import "./UpperFooter.css";

export default function UpperFooter() {
  const [email, setEmail] = useState("");
  const [errors, setErrors] = useState([]);
  const [display, setDisplay] = useState(false);
  const [errorDisplay, setErrorDisplay] = useState(false);

  const handleClick = (e) => {
    e.preventDefault();
    let errors = [];

    if (
      email.length <= 0 ||
      !/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email) ||
      (email.length <= 0 &&
        !/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email))
    ) {
      errors.push("PLEASE ENTER A VALID EMAIL ADDRESS.");
      setDisplay(false);
      setErrorDisplay(true);
    } else {
      errors = [];
      setErrors(errors);
      setErrorDisplay(false);
      setEmail("");
      setDisplay(true);
    }

    if (errors.length > 0) {
      setErrors(errors);
    }

  };
  return (
    <div className="upper-footer-container">
      <div className="footer-module-container">
        <div className="subscribe-module">
          <h1 className="subscribe-module-title">Get on the Black List.</h1>
          <p>
            Be the first to know about the newest gear, automobiles, and
            apparel.
          </p>
          <div className="subscribe-module-wrapper">
            <form onSubmit={handleClick}>
              {display && !errorDisplay ? (
                <div className="email-input-wrapper-black">
                  <input
                    type="text"
                    placeholder="YOUR EMAIL"
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                    className="subscribe-input"
                  />
                  <div className="subscribe-msg">YOU'RE NOW ON THE LIST.</div>
                </div>
              ) : !display && errorDisplay ? (
                <div className="email-input-wrapper-red">
                  <input
                    type="text"
                    placeholder="YOUR EMAIL"
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                    className="subscribe-input"
                  />
                  <ul className="email-error-msg">
                    {errors.map((error) => (
                      <li key={error}>{error}</li>
                    ))}
                  </ul>
                </div>
              ) : !display && !errorDisplay ? (
                <div className="email-input-wrapper">
                  <input
                    type="text"
                    placeholder="YOUR EMAIL"
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                    className="subscribe-input"
                  />
                </div>
              ) : (
                ""
              )}
              <button className="subscribe-btn" onClick={handleClick}>
                SUBSCRIBE
              </button>
            </form>
          </div>
        </div>
      </div>
      <div className="footer-module-container">
        <div className="quote-module">
          <div className="quote-module-left">
            <h2>
              “If James Bond were to make an app for the stuff he wanted to buy,
              this would be the app.”
            </h2>
            <p>— DOUG STEPHENS, RETAIL FUTURIST</p>
          </div>
          <div className="quote-module-right">
            <div className="quote-module-right-left">
              <img
                src="https://uncrate.com/img/app-devices.png"
                alt="devices"
              />
            </div>
            <div className="quote-module-right-right">
              <img
                alt="app store"
                className="app-store-icon"
                src="https://uncrate.com/img/app-store.jpg"
              />
              <img
                src="https://uncrate.com/img/google-play.jpg"
                alt="google play"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
