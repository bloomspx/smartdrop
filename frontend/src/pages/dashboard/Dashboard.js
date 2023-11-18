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

    }

    const logoutHandler = () => {
        resetUserSession();
        navigate("/");
    }

    
    return (
        <div className="container">
            <div className="header-container">
                <h1>Dashboard</h1>
            </div>
            <h3>Welcome Back!</h3>
            <div className="user-table">
                <div>
                    <p><b>Phone Number:</b> {user.phoneNumber}</p>
                </div>
            </div>
            <input type="button" value="Add Item" onClick={addItemHandler}/>
            <input type="button" value="Logout" onClick={logoutHandler}/>
            <h4>My Orders</h4>
            <p>{orders}</p> 
        </div>
    )
}
    
export default Dashboard