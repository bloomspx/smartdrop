import { DynamoDB, GetItemCommand, QueryCommand } from "@aws-sdk/client-dynamodb";
import { buildResponse }from "../utils/utils.mjs";
import { generateToken } from '../utils/auth.mjs';
import bcrypt from "bcryptjs";

const client = new DynamoDB ({region: 'ap-southeast-1'});
const userTable = 'User';
const orderTable = 'Order';

export default async function login(user) {
    const {phoneNumber, password} = user;
    
    // check for blank fields
    if (!phoneNumber || !password) {
        return buildResponse(401, {message: "phone number and password are required fields to login"})
    }
    
    const dynamoUser = await getUser(phoneNumber);
    console.log("dynamoUser:", dynamoUser)
    
    if (!dynamoUser) {
        return buildResponse(401, {message: "user does not exist"});
    }
    if (!bcrypt.compareSync(password, dynamoUser[0].password.S)) {
        return buildResponse(401, {message: "invalid password"});
    }

    const orders = await getOrders(phoneNumber);
    
    const userInfo = {
        phoneNumber: dynamoUser[0].phoneNumber.S,
    }
    
    const token = generateToken(userInfo)
    const response = {
        user: userInfo,
        token: token,
        orders: orders
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

async function getOrders(phoneNumber) {

    const params = {
        TableName: orderTable,
        KeyConditionExpression: 'phoneNumber = :phoneNumber',
        ExpressionAttributeValues: {
            ':phoneNumber': { S: phoneNumber },
        },
    };

    try {
        const command = new QueryCommand(params);
        const response = await client.send(command);
        console.log("getOrders:", response.Items); // This will contain the items from the 'Order' table for the specified username
        return response.Items
    } catch (error) {
        console.error('getOrders Error:', error.message, error.stack);
    }
}