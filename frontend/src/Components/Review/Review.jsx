import React, { useState } from "react";
import "./Review.css";
import { fetchWithAuth } from "../../http";
const Review = ({ isOpen, onClose, productId }) => {
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
        product_id: productId,  // You can set the actual product ID here
        description: review,
        rate: rating,
    };
    try {
        // Send POST request to the API
        const response = fetchWithAuth('http://localhost:5000/api/reviews', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: reviewData,
        });
        console.log("review data");
        console.log(reviewData);
        if (response.ok) {
          // Clear fields and close modal if successful
          console.log("Review submitted successfully");
          onClose(); // Close the modal after submitting
          setReview('');
          setRating('');
          setError(''); // Clear error message after successful submit
        } else {
          // Handle server-side errors
          const errorData =  response.json();
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
    <div className="modalOverlay">
      <div className="modalContent">
        <h2 className="modalTitle">Leave a Review</h2>
        
        {/* Display error if fields are invalid */}
        {error && <p className="errorText">{error}</p>}
        
        <textarea
          className="textarea"
          placeholder="Write your review here (min 20 characters)..."
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />
        <input
          type="text" // Use type="text" to enforce custom validation on the input
          className="input"
          placeholder="Rate out of 5 (e.g., 1, 1.5, 2...)"
          value={rating}
          onChange={(e) => setRating(e.target.value)}
        />
        <div className="modalButtons">
          <button
            onClick={handleSubmit}
            className="submitButton"
          >
            Submit
          </button>
          <button
            onClick={onClose}
            className="closeButton"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );

};

export default Review;
