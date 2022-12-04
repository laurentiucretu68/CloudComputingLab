import axios from "axios";

export default function axiosClient(){
    return axios.create({
        baseURL: "http://localhost:5000/api",
        timeout: 5000
    })
}