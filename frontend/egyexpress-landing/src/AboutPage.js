import React from "react";

const AboutPage = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>About EgyExpress</h1>
      <p style={styles.description}>
        At <strong>EgyExpress</strong>, we are committed to providing affordable and efficient delivery
        solutions tailored specifically for Egypt. Our mission is to help people shop internationally
        without dealing with the hassles of currency exchange or complicated logistics.
      </p>
      <p style={styles.description}>
        Whether you are an individual looking to purchase goods from abroad or a business seeking to expand
        your reach, EgyExpress makes the process seamless. We handle everything from the moment you purchase
        your product until it arrives safely at your door.
      </p>
      <p style={styles.description}>
        Our services are designed with the customer in mind, offering affordable rates, reliable delivery
        times, and a user-friendly platform to track your shipments.
      </p>
      <h2 style={styles.subtitle}>Why Choose Us?</h2>
      <ul style={styles.list}>
        <li>✔ Affordable delivery solutions tailored to your needs</li>
        <li>✔ Easy-to-use platform for managing your shipments</li>
        <li>✔ Reliable delivery times with real-time tracking</li>
        <li>✔ Support for international shopping without currency hassles</li>
      </ul>
      <p style={styles.description}>
        Join us on our mission to simplify global shopping for Egyptians. At <strong>EgyExpress</strong>, your
        satisfaction is our priority.
      </p>
    </div>
  );
};

const styles = {
  container: {
    padding: "20px",
    textAlign: "center",
    backgroundColor: "#3E2723", // Dark brown background to match the theme
    color: "#FBC02D", // Golden yellow text for visibility
    minHeight: "100vh",
  },
  title: {
    fontSize: "2.5rem",
    fontWeight: "bold",
    marginBottom: "20px",
  },
  subtitle: {
    fontSize: "2rem",
    fontWeight: "bold",
    margin: "40px 0 20px",
  },
  description: {
    fontSize: "1.2rem",
    lineHeight: "1.6",
    maxWidth: "800px",
    margin: "auto",
    marginBottom: "20px",
  },
  list: {
    listStyleType: "none",
    padding: 0,
    fontSize: "1.2rem",
    lineHeight: "1.6",
    margin: "20px auto",
    maxWidth: "600px",
    textAlign: "left",
  },
};

export default AboutPage;
