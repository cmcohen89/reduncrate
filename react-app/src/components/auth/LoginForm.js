import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import "./LoginForm.css";

const LoginForm = ({ setShowLoginModal }) => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      errors ? setErrors(data) : setShowLoginModal(false);
    }
  };

  const handleDemo = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("demo@aa.io", "password"));
    if (data) {
      errors ? setErrors(data) : setShowLoginModal(false);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <>
      <form className="login-form" onSubmit={onLogin}>
        <h1 className="login-form-title">LOG IN</h1>
        <div className="login-form-errors">
          {errors.map((error, ind) => (
            <div className="login-errors" key={ind}>
              {error}
            </div>
          ))}
        </div>
        <div className="login-form-field-top">
          <label className="login-form-label" htmlFor="email">
            EMAIL
          </label>
          <input
            className="login-form-input"
            name="email"
            type="text"
            placeholder="Your email address goes here."
            value={email}
            onChange={updateEmail}
            required
          />
        </div>
        <div className="login-form-field">
          <label className="login-form-label" htmlFor="password">
            PASSWORD
          </label>
          <input
            className="login-form-input"
            name="password"
            type="password"
            placeholder={`Here's hoping it's not "password".`}
            value={password}
            onChange={updatePassword}
            required
          />
        </div>
        <div className="login-form-btns">
          <button className="login-submit" type="submit">
            Login
          </button>
          <button
            className="login-with-demo-submit login-submit"
            onClick={handleDemo}
          >
            Login With Demo User
          </button>
        </div>
      </form>
    </>
  );
};

export default LoginForm;
