<template>
    <BaseLayout>
    <template v-slot:center_column>
        <div class="profile-header">
            <div class="avatar">
                <img src="https://picsum.photos/150/" alt="User Avatar">
            </div>
            <div class="user-info">
                <div class="user-info-row-1">
                    <div class="username">@{{ profileStore.userDetails.username }}</div>
                    <div class="cta" v-if="accountStore.user.username !== username">
                        <button class="btn" @click="followUser(username)">{{ checkFollowing }}</button>
                        <button class="btn" @click="messageUser(username)">message</button>
                    </div>
                </div>
                <div class="user-info-row-2">
                    <p>{{ userPostCount }} posts</p>
                    <p>{{ userFollowerCount }} followers</p>
                    <p>{{ profileStore.userDetails.following }} following</p>
                </div>
                <div class="user-info-row-3">
                    <div class="name">{{ fullName }}</div>
                    <div class="bio">Front-End Developer</div>
                    <div class="location">New York, USA</div>
                    <div class="join-date">Joined {{ formattedDate }}</div>
                </div>
            </div>
        </div>
        <div class="empty-post-list" v-if="postList.length === 0">
            <p>POSTS OF USERS YOU FOLLOW WILL APPEAR HERE.</p>
        </div>
        <PostList :posts="postList" v-else/>
    </template>
  </BaseLayout>
</template>

<script setup lang="ts">
import BaseLayout from '@/components/BaseLayout.vue';
import PostList from '@/components/PostList.vue';

import axios from "axios";
import { computed, ref, watchEffect } from 'vue';
import { useRouter } from 'vue-router';
import { useProfileStore } from '@/stores/profile';
import { useAccountStore } from '@/stores/account';

import PostItem from '@/components/PostItem.vue';

const router = useRouter()
const profileStore = useProfileStore()
const accountStore = useAccountStore()
const username = ref(null)
const postList = ref([])

watchEffect(() => {
    username.value = router.currentRoute.value.params.username
    profileStore.getUserDetails(username.value)
    profileStore.getUserPosts(username.value)
});

const fullName = computed(() => {
    return `${profileStore.userDetails.firstName} ${profileStore.userDetails.lastName}`
})

const checkFollowing = computed(() => {
   const followSearch = profileStore.userFollowers.find(item => item.username === accountStore.user.username)
   if (followSearch) {
    return "following"
   } else {
    return "follow"
   }
})

const userPosts = async () => {
    if(username.value === accountStore.user.username){
        await accountStore.getCurrentUserPosts()
        postList.value = accountStore.currentUserPosts
    }else{
        await profileStore.getUserPosts(username.value)
        postList.value = profileStore.userPosts 
    }
}
userPosts()

const userFollowerCount = computed(() => {
    return profileStore.userFollowers.length
})

const userPostCount = computed(() => {
    return postList.value.length
})

const formattedDate = computed(() => {
    const date = new Date(profileStore.userDetails.dateJoined);
    const options = {year: 'numeric', month: 'long'};
    return date.toLocaleDateString('en-US', options)
})

const followUser = async username => {
    const followSearch = profileStore.userFollowers.find(item => item.username === accountStore.user.username)
    const currentUserId = accountStore.user.id;
    if(followSearch){
        await axios.post(`/api/accounts/${username}/unfollow/`, currentUserId)
            .then(response => {
                profileStore.getUserFollowers(username)
                console.log(profileStore.userFollowers)
            })
            .catch(error => console.log(error))
    }else{
        await axios.post(`/api/accounts/${username}/follow/`, currentUserId)
            .then(response => {
                profileStore.getUserFollowers(username)
                console.log(profileStore.userFollowers)
            })
            .catch(error => console.log(error))
    }
}

const messageUser = username => {
    console.log("messageUser clicked")
}
</script>

<style scoped>
.profile-header {
    display: flex;
    margin: 0 auto;
    padding: 20px;
    border-bottom: 1px solid #ccc;
}

.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    overflow: hidden;
}

.user-info {
    margin-left: 20px;
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    gap: 1rem;
}

.user-info-row-1 {
    display: flex;
    gap: 1rem;
}

.user-info-row-2 {
    display: flex;
    gap: 1rem;
}

.user-info-row-2 p {
    font-weight: bold;
}

.username {
    font-size: 1.3rem;
    color: #777;
}

.name {
    font-weight: bold;
}

.bio {
}

.location, .join-date {
    color: #777;
}

.cta {
    display: flex;
    gap: .4rem;
}

.btn {
    display: block;
    width: 100px;
    background-color: #000;
    color: white;
    border: none;
    cursor: pointer;
}
</style>
