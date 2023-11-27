import {generateToken, verifyToken, buildResponse, buildCORSResponse} from "./utils.mjs";
import { DynamoDB, QueryCommand } from "@aws-sdk/client-dynamodb";
import bcrypt from "bcryptjs";

const client = new DynamoDB ({region: 'ap-southeast-1'});
const userTable = 'User';

export const handler = async (event) => {
    console.log("Request Event:", event);
    let response;
    
    try{
        switch(true) {
            case event.httpMethod === 'POST' && event.path === '/login':
                const loginBody = JSON.parse(event.body)
                response = await login(loginBody)
                break;
            case event.httpMethod === 'POST' && event.path === '/verify':
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

async function login(user) {
    const {phoneNumber, password} = user;
    
    // check for blank fields
    if (!phoneNumber || !password) {
        return buildResponse(401, {message: "phone number and password are required fields to login"})
    }
    
    const dynamoUser = await getUser(phoneNumber);
    
    if (!dynamoUser) {
        return buildResponse(401, {message: "user does not exist"});
    }
    if (!bcrypt.compareSync(password, dynamoUser[0].password.S)) {
        return buildResponse(401, {message: "invalid password"});
    }

    const userInfo = {
        phoneNumber: dynamoUser[0].phoneNumber.S,
        deviceID: dynamoUser[0].deviceID.S,
    }
    
    const token = generateToken(userInfo)
    const response = {
        user: userInfo,
        token: token,
    }
    return buildResponse(200, response);
}

async function getUser(phoneNumber) {
    const params = {
        TableName: userTable,
        KeyConditionExpression: 'phoneNumber = :phoneNumber',
        ExpressionAttributeValues: {
            ':phoneNumber': { S: phoneNumber },
        },
    };

    try {
        const command = new QueryCommand(params);
        const response = await client.send(command);
        console.log("getUser:", response); // This will contain the items from the 'User' table for the specified phoneNumber
        return response.Items; // Return the items for the specified phoneNumber
    } catch (error) {
        console.error('getUser error:', error.message, error.stack);
        throw error; // Rethrow the error if you want to propagate it further
    }
}

async function verify(requestBody) {
    console.log("verify:", requestBody);
    if (!requestBody.user || !requestBody.user.phoneNumber || !requestBody.token) {
        return buildResponse(401, {
            verified: false,
            message: "incorrect request body"
        })
    }

    const user = requestBody.user
    const token = requestBody.token
    const verification = verifyToken(user.phoneNumber, token)
    
    if (!verification.verified) {
        return buildResponse(401, verification);
    }

    return buildResponse(200, {
        verified: true,
        message: 'success',
        user: user,
        token: token
    })
}