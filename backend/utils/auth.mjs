import jwt from "jsonwebtoken";

// generates a token for a valid login session
export function generateToken(userInfo) {
    if (!userInfo) {
        return null;
    }

    // sign using a token from Lambda function
    return jwt.sign(userInfo, process.env.JWT_secret, {
        expiresIn: "10000"
    })
}

// verifies if token is valid
export function verifyToken(username, token) {
    return jwt.verify(token, process.env.JWT_secret, (error, response) => {
        if (error) {
            return {
                verified: false,
                message: "invalid token"
            }
        }
        if (response.username !== username) {
            return {
                verified: false,
                message: "invalid user"
            }
        }
        return {
            verified: true,
            message: "verified user"
        }
    })
}

export default {generateToken, verifyToken};