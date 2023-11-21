import { useNavigate } from "react-router-dom";
import { getOrders, getUser } from "../../service/AuthService"
import { useState } from 'react';
import axios from "axios";

const addDeliveryUrl = 'https://woqp7vxlb1.execute-api.ap-southeast-1.amazonaws.com/beta/neworder';

const Delivery = () => {

    let navigate = useNavigate()
    const [itemName, setItemName] = useState('');
    const [shopName, setShopName] = useState('');
    const [message, setMessage] = useState('');
    const [loading, setLoading] = useState('');

    const user = getUser();

    const handleSubmit = (event) => {
        event.preventDefault();
        setLoading(true);
        setMessage(null);
        
        const requestConfig = {
            headers: {
                'x-api-key': 'geWKcJIsit3toxhMxHcTy4Ei4gKsa3EUapZEggT6'
            }
        }

        const requestBody = {
            deviceID: user.deviceID,
            itemName: itemName,
            shopName: shopName,
        }
        axios.post(addDeliveryUrl, requestBody, requestConfig).then(response => {
            setLoading(false);
            setMessage('New delivery successfully added, you will be redirected to dashboard in 3s...')
            // Reset form fields after submission
            setItemName('');
            setShopName('');
            setTimeout(() => {
                navigate('/')
            }, 3000)
        }).catch(error => {
            setLoading(false);
            // 401: user error
            if (error.response.status === 401) {
                setMessage(error.response.data.message);
            } else {
                setMessage('Backend server is down, please try again later')
            }
        })
    }


    return (
        <div className="container">
            <div className="header-container">
                <h1>Create New Delivery</h1>
            </div>
            {loading && <p>Loading....</p>}
            {!loading && <form onSubmit={handleSubmit}>
                <label>
                    Item Name:
                    <input type="text" value={itemName} onChange={(e) => setItemName(e.target.value)} required/>
                </label>
                <br />

                <label>
                    Ordered From:
                    <input type="text" value={shopName} onChange={(e) => setShopName(e.target.value)} required/>
                </label>
                <br />
                <button type="submit">Create New Delivery</button>
            </form>}
            {message && <p className='message'>{message}</p>}
        </div>
    )
}
    
export default Delivery