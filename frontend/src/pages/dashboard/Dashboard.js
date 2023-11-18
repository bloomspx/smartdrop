import { useNavigate } from "react-router-dom";
import { getUser, resetUserSession } from "../../service/AuthService"

const Dashboard = () => {

    let navigate = useNavigate()
    const user = getUser();
    const name = (user !== 'undefined' && user) ? user.name.S : '';

    console.log(user)

    const logoutHandler = () => {
        resetUserSession();
        navigate("/login");
    }

    
    return (
        <div className="dashboard-container">
            <div className="header-container">
                <h1>Dashboard</h1>
            </div>
            <h2>Hello, {name}! </h2>
            <input type="button" value="Logout" onClick={logoutHandler}/>
        </div>
    )
}
    
export default Dashboard