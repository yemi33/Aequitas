import React from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import OurNavbar from "../components/OurNavbar";

export default function AboutUsScreen () {
  return (
    <div>
      <OurNavbar></OurNavbar>
      <Header>About Us</Header>
      <div className="container">
        We are a group of seniors (&apos;22) studying computer science at Carleton College. <br />
        This is our senior project, and we hope you enjoy it!
      </div>
      <Footer></Footer>
    </div>
  );
}
