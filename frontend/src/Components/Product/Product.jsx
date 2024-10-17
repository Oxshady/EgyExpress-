import { Link } from "react-router-dom";
function Product(props) {
      console.log(props);
  const {product} = props;
  console.log(product);
  return (
    <>
      <div className="card">
        <img src={product.image} className="card-img-top" alt={product.title} />
        <div className="card-body">
          <h5 className="card-title">{product.title}</h5>
          <p className="card-text">{product.description}</p>
          <button href="#" className="btn btn-primary">
            <Link
              className="nav-link active"
              aria-current="page"
              to={`/product/${product.id}`}
            >
              Details
            </Link>
          </button>
        </div>
      </div>
    </>
  );
}
export default Product;
