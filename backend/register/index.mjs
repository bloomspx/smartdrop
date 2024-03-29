import {buildResponse, buildCORSResponse} from "./utils.mjs";
import { DynamoDB, PutItemCommand, QueryCommand } from "@aws-sdk/client-dynamodb";
import bcrypt from "bcryptjs";

const client = new DynamoDB ({region: 'ap-southeast-1'});
const userTable = 'User';

export const handler = async (event) => {
    console.log("Request Event:", event);
    let response;
    
    try{
        switch(true) {
            case event.httpMethod === 'POST' && event.path === '/register':
                const registerBody = JSON.parse(event.body)
                response = await register(registerBody)
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


// registers new users
async function register(userInfo) {
    const { deviceID, phoneNumber, password, address } = userInfo;

    if (!deviceID || !phoneNumber || !password || !address) {
        return buildResponse(401, { message: "All fields are required" });
    }

    // check for duplicate usernames
    const dynamoUser = await getUser(phoneNumber);

    if (!dynamoUser || (Array.isArray(dynamoUser) && dynamoUser.length !== 0)) {
        return buildResponse(401, { message: "Phone number already exists in database, please choose a different phone number" });
    }

    const encryptedPass = bcrypt.hashSync(password, 10);
    const user = {
        deviceID: deviceID,
        phoneNumber: phoneNumber,
        password: encryptedPass,
        address: address
    }
    console.log('Register User:', user)

    // save new user to database
    const saveUserResponse = await saveUser(user);
    if (!saveUserResponse) {
        return buildResponse(503, { message: "Server Error, please try again later" });
    }

    return buildResponse(200, {message: "true"});
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

async function saveUser(user){
    const command = new PutItemCommand ({
        TableName: userTable,
        Item: {
            phoneNumber: { S: user.phoneNumber },        
            deviceID: { S: user.deviceID },
            password: { S: user.password },
            address: { S: user.address },
        }
    })
    const response = await client.send(command).then(response => {
        return true;
    }, error => {
        console.error("There is an error:", error)
    });;
    console.log("saveUser:", response);
    return response;
}