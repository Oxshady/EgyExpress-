import { fetchWithAuth } from "../../http";
import { logout } from "../../state/authSlice";
import { clearUser } from "../../state/userSlice";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
function DeleteAcount(){
const naviagte = useNavigate();
const dispatch = useDispatch();
    const deleteAccount = async () => {
        const options = {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetchWithAuth(
          "http://localhost:5000//api/profile/delete",
          options
        );
        dispatch(logout());
        dispatch(clearUser());
        naviagte("/");
    }
return(
    <div>
        <h1>Are you sure you want to delete your account?</h1>
        <button onClick={deleteAccount}>Delete Account</button>
    </div>
)
}
export default DeleteAcount;
