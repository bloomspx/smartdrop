import { buildResponse } from "../utils/utils.mjs";
import { verifyToken } from '../utils/auth.mjs';


export default function verify(requestBody) {
    if (!requestBody.user || !requestBody.user.username || !requestBody.token) {
        return buildResponse(401, {
            verified: false,
            message: "incorrect request body"
        })
    }

    const user = requestBody.user
    const token = requestBody.token
    const verification = verifyToken(user.username.S, token)
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