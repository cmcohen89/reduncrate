import React from "react";
import "./Footer.css";
import UpperFooter from "./UpperFooter/UpperFooter";
import LowerFooter from "./LowerFooter/LowerFooter";
import BottomFooter from "./BottomFooter/BottomFooter";

export default function Footer() {
  return (
    <div className="footer-wrapper">
      <div className="footer">
        <UpperFooter />
        <LowerFooter />
        <BottomFooter />
      </div>
    </div>
  );
}
