import axios from "axios";
import { defineStore } from "pinia";

import { useAccountStore} from "@/stores/account";

const accountStore = useAccountStore()

export const usePostStore = defineStore('post', () => {
    async function publishPost(content) {
        await axios.post('/api/posts/create/', {content: content})
            .then(response => {
                accountStore.getCurrentUserPosts()
                accountStore.currentUserPosts.unshift(response.data)
            }).catch(error => {
                console.log('error', error)
            })   
    }

    return { publishPost, }
})
