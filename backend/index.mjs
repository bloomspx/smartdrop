import register from "./service/register.mjs";
import login from "./service/login.mjs";
import verify from "./service/verify.mjs";
import {buildResponse, buildCORSResponse} from "./utils/utils.mjs";

const homePath = '/home';
const registerPath = '/register';
const loginPath = '/login';
const verifyPath = '/verify';

export const handler = async (event) => {
    console.log("Request Event:", event);
    let response;
    
    try{
        switch(true) {
            case event.httpMethod === 'GET' && event.path === homePath:
                response = buildResponse(200, "Welcome to the Home Page");
                break;
            case event.httpMethod === 'POST' && event.path === registerPath:
                const registerBody = JSON.parse(event.body)
                response = await register(registerBody)
                break;
            case event.httpMethod === 'POST' && event.path === loginPath:
                const loginBody = JSON.parse(event.body)
                response = await login(loginBody)
                break;
            case event.httpMethod === 'POST' && event.path === verifyPath:
                const verifyBody = JSON.parse(event.body)
                response = await verify(verifyBody)
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
