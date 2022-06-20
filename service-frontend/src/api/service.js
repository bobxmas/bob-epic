import request from "../api/request";

export function callA(token) {
    if (token=='') return request.get(`/a`)
    const headers = {'Authorization': "Bearer " + token}
    return request.get(`/a`, {headers: headers})
}

export function callAB(token) {
    if (token=='') return request.get(`/a/b`, {headers: headers})
    const headers = {'Authorization': "Bearer " + token}
    return request.get(`/a/b`, {headers: headers})
}

export function callABTest(token) {
    if (token=='') return request.get(`/a/b/test`, {headers: headers})
    const headers = {'Authorization': "Bearer " + token}
    return request.get(`/a/b/test`, {headers: headers})
}

export function callAC(token) {
    if (token=='') return request.get(`/a/c`, {headers: headers})
    const headers = {'Authorization': "Bearer " + token}
    return request.get(`/a/c`, {headers: headers})
}