import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import "./SignUpForm.css";

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    let errors = [];
    if (/\d/.test(first_name) || /\d/.test(last_name))
      errors.push("Your name has numbers in it? Doubt it.");
    if (!/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email))
      errors.push("That's not a valid email address. Told you we'd check.");
    if (username.length < 5)
      errors.push(
        "Let's make that username a bit longer. 5 characters should do."
      );
    if (password !== repeatPassword)
      errors.push('You really botched that whole "repeat password" thing.');
    if (errors.length > 0) {
      setErrors(errors);
    } else {
      errors = [];
      const data = await dispatch(
        signUp(first_name, last_name, username, email, password)
      );
      if (data) {
        if (errors) setErrors(data);
      }
    }
  };

  const updateFirstName = (e) => {
    setFirstName(e.target.value);
  };

  const updateLastName = (e) => {
    setLastName(e.target.value);
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <form className="signup-form" onSubmit={onSignUp}>
      <h1 className="signup-form-title">SIGN UP</h1>
      <div className="signup-form-errors">{errors[0]}</div>
      <div className="signup-form-field-top">
        <label className="signup-form-label">FIRST NAME</label>
        <input
          required
          className="signup-form-input"
          placeholder="It's that thing your friends call you."
          type="text"
          name="first_name"
          onChange={updateFirstName}
          value={first_name}
        ></input>
      </div>
      <div className="signup-form-field-top">
        <label className="signup-form-label">LAST NAME</label>
        <input
          required
          className="signup-form-input"
          placeholder="It's that thing your coach called you."
          type="text"
          name="last_name"
          onChange={updateLastName}
          value={last_name}
        ></input>
      </div>
      <div className="signup-form-field-top">
        <label className="signup-form-label">EMAIL</label>
        <input
          required
          className="signup-form-input"
          type="text"
          name="email"
          placeholder="Must be a valid email address. We'll check."
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div className="signup-form-field-top">
        <label className="signup-form-label">USERNAME</label>
        <input
          required
          className="signup-form-input"
          type="text"
          name="username"
          placeholder="We're excited to see how clever you are."
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
      <div className="signup-form-field-top">
        <label className="signup-form-label">PASSWORD</label>
        <input
          required
          className="signup-form-input"
          type="password"
          name="password"
          placeholder='Make it "password" if you dig identity theft.'
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div className="signup-form-field">
        <label className="signup-form-label">REPEAT PASSWORD</label>
        <input
          className="signup-form-input"
          type="password"
          name="repeat_password"
          placeholder="Typing is hard. Don't blow this."
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <button type="submit" className="signup-submit">
        Sign Up
      </button>
    </form>
  );
};

export default SignUpForm;
