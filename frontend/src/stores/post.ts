import axios from "axios";
import { defineStore } from "pinia";

export const usePostStore = defineStore('post', () => {
    async function publishPost(content) {
        await axios.post('/api/posts/create/', {content: content})
            .then(response => {
                console.log(response)
            }).catch(error => {
                console.log('error', error)
            })   
    }

    return { publishPost, }
})