import React from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import OurNavbar from "../components/OurNavbar";

export default function AboutAequitasScreen() {
  return (
    <div>
      <OurNavbar></OurNavbar>
      <Header>About Aequitas</Header>
      <div className="container">
        <h3>History</h3>
        <p>
          This work is based on the technology developed in the following
          conference proceeding: <br />
          <strong>Title</strong>: Automated directed fairness testing <br />
          <strong>Authors</strong>: Udeshi, Sakshi and Arora, Pryanshu and
          Chattopadhyay, Sudipta <br />
          <strong>Book Title</strong>: Proceedings of the 33rd ACM/IEEE
          International Conference on Automated Software Engineering <br />
          <strong>Pages</strong>: 98--108 <br />
          <strong>Year</strong>: 2018 <br />
          Liscened by the original authors
        </p>
        <h3>Download the Aequitas Command Line Utility, <a href="https://pypi.org/project/Phemus/">Phemus!</a></h3>
        <p>
          Phemus is a baby of Aequitas, a tool that gives all the benefits of Aequitas in a simple command-line interface.
        </p>
      </div>
      <Footer></Footer>
    </div>
  );
}
