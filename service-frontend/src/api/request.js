import axios from 'axios'

const service = axios.create({
    withCredentials: true,
    baseURL: '/api',
    timeout: 60000
})

service.interceptors.request.use(
    config => {
        return config
    },
    error => {
        return Promise.reject(error)
    }
)

service.interceptors.response.use(
    res => {
        return res.data
    },
    error => {
        console.error(JSON.stringify(error))
        return Promise.reject(error)
    }
)

export default service