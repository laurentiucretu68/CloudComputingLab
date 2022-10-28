import axios from "axios";

export default function axiosClient(){
    return axios.create({
        baseURL: "http://localhost:8081/api",
        timeout: 5000
    })
}