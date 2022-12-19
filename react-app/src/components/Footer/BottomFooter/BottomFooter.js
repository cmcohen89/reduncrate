import React from "react";
import "./BottomFooter.css";

export default function BottomFooter() {
  return (
    <div className="bottom-footer-container">
      <div className="copyright-section">
        <img src="/images/reduncrate-white2.png" className="footer-logo" />
        <p className="copyright-statement">
          © 2022 REDUNCRATE LLC. ALL RIGHTS RESERVED. INDEPENDENTLY PUBLISHED
          SINCE 2022.
        </p>
        <p className="copyright-statement">
          ALL ITEMS ON UNCRATE ARE HAND-CHOSEN BY EDITORS FOR QUALITY AND
          RELEVANCE TO OUR READERS. SUPPLY ITEMS ARE STOCKED AND SHIPPED BY
          UNCRATE. SOME EDITORIAL MAY BE SPONSORED OR ALLOW US TO RECEIVE A
          COMMISSION.
        </p>
      </div>
      <img className="payment-info" src="https://uncrate.com/img/payment.jpg" />
    </div>
  );
}
