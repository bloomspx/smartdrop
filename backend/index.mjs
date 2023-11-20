import register from "./service/register.mjs";
import login from "./service/login.mjs";
import verify from "./service/verify.mjs";
import {getAllOrders, newOrder, updateOrder} from "./service/delivery.mjs";
import {buildResponse, buildCORSResponse} from "./utils/utils.mjs";

export const handler = async (event) => {
    console.log("Request Event:", event);
    let response;
    
    try{
        switch(true) {
            case event.httpMethod === 'POST' && event.path === '/register':
                const registerBody = JSON.parse(event.body)
                response = await register(registerBody)
                break;
            case event.httpMethod === 'POST' && event.path === '/login':
                const loginBody = JSON.parse(event.body)
                response = await login(loginBody)
                break;
            case event.httpMethod === 'POST' && event.path === '/verify':
                const verifyBody = JSON.parse(event.body)
                response = await verify(verifyBody)
                break;
            case event.httpMethod === 'POST' && event.path === '/getallorders':
                const ordersBody = JSON.parse(event.body)
                response = await getAllOrders(ordersBody)
                break;
            case event.httpMethod === 'POST' && event.path === '/neworder':
                const newOrderBody = JSON.parse(event.body)
                response = await newOrder(newOrderBody)
                break;
            case event.httpMethod === 'POST' && event.path === '/updateorder':
                const updateOrderBody = JSON.parse(event.body)
                response = await updateOrder(updateOrderBody)
                break;
            case event.httpMethod === 'OPTIONS':
                response = buildCORSResponse(200, 'Success');
                break;
            default:
                response = buildResponse(404, '404 Not Found');
        }
    } catch (error) {
        console.error("Error:", error);
        response = buildResponse(500, 'Internal Server Error');
    }
    return response;
};
