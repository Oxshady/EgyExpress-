import { useEffect, useState } from "react";
import Product from "./Product";
function ProductList() {
  const api_url = "https://fakestoreapi.com/products";
  const [products, setProducts] = useState([]);
  useEffect(() => {
    fetch(api_url)
      .then((res) => res.json())
      .then((data) => setProducts(data));
  }, []);
  console.log(products);
  return (
    <>
      <h2 className="text-center p-3">FeaturedProduct </h2>
      <div className="container">
        <div className="row">
          {products.map((product) => {
            return (
              <div className="col-3" key={product.id}>
                <Product product={product} />
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
}
export default ProductList;
