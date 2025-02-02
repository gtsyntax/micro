import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProfileStore = defineStore('profile', () => {
    const userDetails = ref({
        id: null,
        firstName: null,
        lastName: null,
        username: null,
        email: null,
        following: 0,
        followers: 0,
        posts: 0,
        bio: null,
        dateJoined: null,
    })

    const userPosts = ref([])
    const userFollowers = ref([])

    function setUserDetails(userInfo) {
        userDetails.value.id = userInfo.id
        userDetails.value.firstName = userInfo.first_name
        userDetails.value.lastName = userInfo.last_name
        userDetails.value.username = userInfo.username
        userDetails.value.email = userInfo.email
        userDetails.value.following = userInfo.following
        userDetails.value.followers = userInfo.followers
        userDetails.value.posts = userInfo.posts
        userDetails.value.bio = userInfo.bio
        userDetails.value.dateJoined = userInfo.date_joined
    }

    async function getUserDetails(username) {
        await axios.get(`/api/accounts/users/${username}`)
            .then(response => {
                setUserDetails(response.data);
                getUserFollowers(username);
            }).catch(error => {
                console.log('error', error)
            })
    }

    const getUserPosts = async username => {
        await axios.get(`/api/posts/${username}/all_posts/`)
            .then(response => {
                console.log("user posts", response.data)
                userPosts.value = response.data
            }).catch(error => {
                console.log('error', error)
            })
    }

    async function getUserFollowers(username) {
        await axios.get(`/api/accounts/users/${username}/followers`)
            .then(response => {
                console.log(response.data)
                userFollowers.value = response.data
            }).catch(error => console.log(error))
    }

    return { userDetails, userPosts, getUserDetails, getUserPosts, userFollowers, getUserFollowers }
})
