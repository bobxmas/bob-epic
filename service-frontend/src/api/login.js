import request from "../api/request";

export function login(username, password) {
    return request.get(`/login/${username}/${password}`)
}
