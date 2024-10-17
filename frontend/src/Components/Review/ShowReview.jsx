import { useEffect,useState } from "react";

function ShowReview(props) {
    const product_id = props.product;
    const [reviews, setReviews] = useState([]);
   useEffect(() => {
    if (product_id) {
      const api = `http://localhost:5000/api/reviews/get?product_id=${product_id}`;
      console.log("api")
      console.log(api)
      fetch(api)
        .then((res) => res.json())
        .then((data) => setReviews(data))
        .catch((error) => console.error('Error fetching reviews:', error));
    }
  }, [product_id]);
   console.log("product_id")
   console.log(product_id)
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Reviews</h1>
      {reviews.map((review, index) => (
        <div key={index} className="review-box">
          <h2>{review.user_name}</h2>
          <p className="rating">Rating: {review.rate}</p>
          <p>{review.description}</p>
        </div>
      ))}
    </>
  );
}

export default ShowReview;
