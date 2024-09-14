import React, { useState } from "react";

const ReviewModal = ({ isOpen, onClose }) => {
  const [review, setReview] = useState('');
  const [rating, setRating] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = () => {
    // Validation for review length
    if (review.length < 20) {
      setError("Review must be at least 20 characters long.");
      return;
    }

    // Validation for rating to accept only natural numbers or .5 increments
    const validRating = /^[1-5](\.5)?$/.test(rating);
    if (!validRating) {
      setError("Rating must be a number between 1 and 5, and can only include .5 increments.");
      return;
    }

    // Prepare the data for the API call
    const reviewData = {
        product_id: null,  // You can set the actual product ID here
        description: review,
        rate: rating,
    };

    try {
        // Send POST request to the API
        const response = await fetch('/api/review', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,  // Attach the JWT token to the Authorization header
          },
          body: JSON.stringify(reviewData),
        });
    
        if (response.ok) {
          // Clear fields and close modal if successful
          console.log("Review submitted successfully");
          onClose(); // Close the modal after submitting
          setReview('');
          setRating('');
          setError(''); // Clear error message after successful submit
        } else {
          // Handle server-side errors
          const errorData = await response.json();
          setError(`Error: ${errorData.message}`);
        }
      } catch (error) {
        // Handle client-side errors
        setError(`Error: ${error.message}`);
      }

    // Clear error and proceed if valid
    setError('');
    console.log("Review:", review);
    console.log("Rating:", rating);

    onClose(); // Close the modal after submitting
    setReview('');
    setRating('');
  };

  if (!isOpen) {
    return null;
  }

  return (
    <div style={styles.modalOverlay}>
      <div style={styles.modalContent}>
        <h2 style={styles.modalTitle}>Leave a Review</h2>
        
        {/* Display error if fields are invalid */}
        {error && <p style={styles.errorText}>{error}</p>}
        
        <textarea
          style={styles.textarea}
          placeholder="Write your review here (min 20 characters)..."
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />
        <input
          type="text" // Use type="text" to enforce custom validation on the input
          style={styles.input}
          placeholder="Rate out of 5 (e.g., 1, 1.5, 2...)"
          value={rating}
          onChange={(e) => setRating(e.target.value)}
        />
        <div style={styles.modalButtons}>
          <button
            onClick={handleSubmit}
            style={styles.submitButton}
          >
            Submit
          </button>
          <button
            onClick={onClose}
            style={styles.closeButton}
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );

};

// Inline styles for the modal
const styles = {
  modalOverlay: {
    position: "fixed",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: "rgba(0, 0, 0, 0.5)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    zIndex: 1000,
  },
  modalContent: {
    backgroundColor: "#fff",
    padding: "20px",
    borderRadius: "10px",
    maxWidth: "400px",
    width: "100%",
    textAlign: "center",
  },
  modalTitle: {
    fontSize: "1.5rem",
    marginBottom: "20px",
  },
  textarea: {
    width: "100%",
    height: "100px",
    padding: "10px",
    marginBottom: "10px",
    fontSize: "1rem",
    borderRadius: "5px",
    border: "1px solid #ccc",
    boxSizing: "border-box",
  },
  input: {
    width: "100%",
    padding: "10px",
    marginBottom: "20px",
    fontSize: "1rem",
    borderRadius: "5px",
    border: "1px solid #ccc",
    boxSizing: "border-box",
  },
  modalButtons: {
    display: "flex",
    justifyContent: "space-between",
  },
  submitButton: {
    padding: "10px 20px",
    backgroundColor: "#4CAF50",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
  closeButton: {
    padding: "10px 20px",
    backgroundColor: "#f44336",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
  errorText: {
    color: "red",
    marginBottom: "10px",
  },
};

export default ReviewModal;
