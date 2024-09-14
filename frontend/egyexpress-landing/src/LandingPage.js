import React from "react";
import { useNavigate, Link } from "react-router-dom"; // Import Link from react-router-dom

const LandingPage = () => {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate("/home");
  };

  return (
    <div style={styles.container}>
      <img src="/egyexpress-logo.png" alt="EgyExpress Logo" style={styles.logo} />
      <h1 style={styles.title}>Welcome to EgyExpress</h1>
      <p style={styles.description}>
        Affordable delivery solutions tailored for Egypt, allowing you to shop abroad without
        currency hassles.
      </p>
      <button onClick={handleGetStarted} style={styles.button}>
        Get Started
      </button>
      {/* Add About Us link */}
      <Link to="/about" style={styles.aboutLink}>
        Learn More About Us
      </Link>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
    backgroundColor: "#3E2723",
    color: "#FBC02D",
    textAlign: "center",
    padding: "20px",
  },
  logo: {
    width: "300px",
  },
  title: {
    fontSize: "2.5rem",
    fontWeight: "bold",
    marginBottom: "20px",
  },
  description: {
    fontSize: "1.2rem",
    marginBottom: "40px",
    maxWidth: "600px",
  },
  button: {
    padding: "10px 20px",
    fontSize: "1.2rem",
    fontWeight: "bold",
    backgroundColor: "#FBC02D",
    color: "#3E2723",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    transition: "background-color 0.3s ease",
    marginBottom: "20px",
  },
  aboutLink: {
    padding: "10px 20px",
    backgroundColor: "#FBC02D",
    color: "#3E2723",
    textDecoration: "none",
    borderRadius: "5px",
    fontSize: "1.2rem",
    fontWeight: "bold",
    cursor: "pointer",
    transition: "background-color 0.3s ease",
  },
};

export default LandingPage;
