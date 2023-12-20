import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";

export const useAccountStore = defineStore('account', () => {
    const user = ref({
        isAuthenticated: false,
        id: null,
        firstName: null,
        lastName: null,
        username: null,
        email: null,
        following: null,
        followers: null,
        bio: null,
        access: null,
        refresh: null,
    })

    const currentUserPosts = ref([])

    function storeInit() {
        if (localStorage.getItem('user.access')) {
            console.log('User has access', localStorage.getItem('user.access'))
            user.value.access = localStorage.getItem('user.access')
            user.value.refresh = localStorage.getItem('user.refresh')
            user.value.id = localStorage.getItem('user.id')
            user.value.firstName = localStorage.getItem('user.firstName')
            user.value.lastName = localStorage.getItem('user.lastName')
            user.value.username = localStorage.getItem('user.username')
            user.value.email = localStorage.getItem('user.email')
            user.value.following = localStorage.getItem('user.following')
            user.value.followers = localStorage.getItem('user.followers')
            user.value.bio = localStorage.getItem('user.bio')
            user.value.isAuthenticated = true

            refreshToken()
            console.log('Initialized user:', user.value)
        } else {
            console.log("User doesn't have access", localStorage.getItem('user.access'))
        }
    }

    function setToken(data) {
        console.log('setToken', data)

        user.value.access = data.access
        user.value.refresh = data.refresh
        user.value.isAuthenticated = true

        localStorage.setItem('user.access', data.access)
        localStorage.setItem('user.refresh', data.refresh)
    }

    function setUserInfo(userInfo) {
        console.log('Set User Info', userInfo)

        user.value.id = userInfo.id
        user.value.email = userInfo.email
        user.value.username = userInfo.username 
        user.value.firstName = userInfo.first_name
        user.value.lastName = userInfo.last_name
        user.value.following = userInfo.following
        user.value.followers = userInfo.followers
        user.value.bio = userInfo.bio

        localStorage.setItem('user.id', userInfo.id)
        localStorage.setItem('user.email', userInfo.email)
        localStorage.setItem('user.username', userInfo.username)
        localStorage.setItem('user.firstName', userInfo.first_name)
        localStorage.setItem('user.lastName', userInfo.last_name)
        localStorage.setItem('user.following', userInfo.following)
        localStorage.setItem('user.followers', userInfo.followers)
        localStorage.setItem('user.bio', userInfo.bio)
    }

    function removeToken() {
        console.log('removeToken')

        user.value.access = null
        user.value.refresh = null
        user.value.id = null
        user.value.firstName = null
        user.value.lastName = null
        user.value.username =null
        user.value.email = null
        user.value.following = null
        user.value.followers = null
        user.value.isAuthenticated = false

        localStorage.setItem('user.access', '')
        localStorage.setItem('user.refresh', '')
        localStorage.setItem('user.id', '')
        localStorage.setItem('user.name', '')
        localStorage.setItem('user.username', '')
        localStorage.setItem('user.email', '')
    }

    async function refreshToken() {
        await axios.post('/api/accounts/token/refresh/', {
            refresh: user.value.refresh
        }).then(response => {
            user.value.access = response.data.access
            localStorage.setItem('user.access', response.data.access)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
        }).catch(error => {
            console.log(error)
            removeToken()
        })
    }

    async function getCurrentUserPosts() {
        await axios.get(`/api/posts/my_posts/`)
            .then(response => {
                console.log("current user posts", response.data)
                currentUserPosts.value = response.data
            }).catch(error => {
                console.log('error', error)
            })
    }

    return { user, storeInit, setToken, setUserInfo, currentUserPosts, getCurrentUserPosts }
})
