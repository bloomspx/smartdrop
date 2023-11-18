import { DynamoDB, GetItemCommand } from "@aws-sdk/client-dynamodb";
import { buildResponse }from "../utils/utils.mjs";
import { generateToken } from '../utils/auth.mjs';
import bcrypt from "bcryptjs";

const client = new DynamoDB ({region: 'ap-southeast-1'});
const userTable = 'User';

export default async function login(user) {
    const {username, password} = user;
    
    // check for blank fields
    if (!username || !password) {
        return buildResponse(401, {message: "username and password are required fields to login"})
    }
    
    const dynamoUser = await getUser(username);
    if (!dynamoUser || !dynamoUser.username) {
        return buildResponse(401, {message: "user does not exist"});
    }
    console.log(password, dynamoUser.password.S)
    if (!bcrypt.compareSync(password, dynamoUser.password.S)) {
        return buildResponse(401, {message: "invalid password"});
    }
    
    const userInfo = {
        username: dynamoUser.username,
        name: dynamoUser.name,
    }
    const token = generateToken(userInfo)
    const response = {
        user: userInfo,
        token: token
    }
    return buildResponse(200, response);
}

async function getUser(username) {
    const command = new GetItemCommand({
        TableName: userTable,
        Key: {
            "username": {
                "S": username
            }
        }
    });
    const response = await client.send(command).then(response => {
        return response.Item;
    }, error => {
        console.error("There is an error:", error)
    });
    console.log(response);
    return response;
}