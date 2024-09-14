import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import LandingPage from "./LandingPage";
import AboutPage from "./AboutPage";
import ReviewModal from "./ReviewModal"; // Import the ReviewModal component

const HomePage = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <div style={styles.container}>
      <h1>Welcome to the Home Page!</h1>
      <Link to="/about" style={styles.link}>About Us</Link>

      {/* Button to open the review modal */}
      <button onClick={openModal} style={styles.reviewButton}>Review</button>

      {/* Review modal, passing `isOpen` and `onClose` props */}
      <ReviewModal isOpen={isModalOpen} onClose={closeModal} />
    </div>
  );
};

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
      </Routes>
    </Router>
  );
}

const styles = {
  container: {
    textAlign: "center",
    padding: "50px",
  },
  link: {
    padding: "10px 20px",
    backgroundColor: "#FBC02D", // Golden yellow background
    color: "#3E2723", // Dark brown text
    textDecoration: "none",
    borderRadius: "5px",
    fontSize: "1.2rem",
    fontWeight: "bold",
    cursor: "pointer",
    transition: "background-color 0.3s ease",
  },
  reviewButton: {
    padding: "10px 20px",
    marginTop: "20px",
    backgroundColor: "#FBC02D",
    color: "#3E2723",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
};

export default App;
