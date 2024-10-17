import { useEffect } from "react";
import "../css/About.css"; // Import the CSS file

function About() {
  useEffect(() => {
    const container = document.querySelector(".about-container");
    container.classList.add("fade-in");
  }, []);

  return (
    <div className="about-container">
      <h1 className="about-title">About EgyExpress</h1>
      <p className="about-description">
        At <strong>EgyExpress</strong>, we are committed to providing affordable
        and efficient delivery solutions tailored specifically for Egypt. Our
        mission is to help people shop internationally without dealing with the
        hassles of currency exchange or complicated logistics.
      </p>
      <p className="about-description">
        Whether you are an individual looking to purchase goods from abroad or a
        business seeking to expand your reach, EgyExpress makes the process
        seamless. We handle everything from the moment you purchase your product
        until it arrives safely at your door.
      </p>
      <p className="about-description">
        Our services are designed with the customer in mind, offering affordable
        rates, reliable delivery times, and a user-friendly platform to track
        your shipments.
      </p>
      <h2 className="about-subtitle">Why Choose Us?</h2>
      <ul className="about-list">
        <li>✔ Affordable delivery solutions tailored to your needs</li>
        <li>✔ Easy-to-use platform for managing your shipments</li>
        <li>✔ Reliable delivery times with real-time tracking</li>
        <li>✔ Support for international shopping without currency hassles</li>
      </ul>
      <p className="about-description">
        Join us on our mission to simplify global shopping for Egyptians. At{" "}
        <strong>EgyExpress</strong>, your satisfaction is our priority.
      </p>
    </div>
  );
}

export default About;
