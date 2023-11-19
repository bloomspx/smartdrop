import './dashboard.css'
import { useNavigate } from "react-router-dom";
import { getOrders, getUser, resetUserSession } from "../../service/AuthService"
import { useState } from 'react';

const Dashboard = () => {

    let navigate = useNavigate()
    // TODO: Save states of users and orders
    const user = getUser();
    // TODO: convert orders (JSONify from original list) into readable data
    const orders = getOrders();

    console.log(user, orders)

    const addItemHandler = () => {
        navigate("/newdelivery")
    }

    const logoutHandler = () => {
        resetUserSession();
        navigate("/");
    }

    return (
        <div className="container">
            <div className="header-container">
                <h1>Parcel Management Dashboard</h1>
                <input type="button" value="Create New Delivery" onClick={addItemHandler}/>
                <input type="button" value="Logout" onClick={logoutHandler}/>
            </div>
            <div className="user-table">
                <div>
                    <p><b>Phone Number:</b> {user.phoneNumber}</p>
                </div>
            </div>
            <h4>My Orders</h4>
            <p>{orders}</p> 
        </div>
    )
}
    
export default Dashboard