<template>
    <BaseLayout>
    <template v-slot:center_column>
        <div class="profile-header">
            <div class="avatar">
                <img src="https://picsum.photos/150/" alt="User Avatar">
            </div>

            <div class="user-info">
                <div class="name">{{ fullName }}</div>
                <div class="username">@{{ profileStore.userDetails.username }}</div>
                <div class="bio">Front-End Developer</div>
                <div class="location">New York, USA</div>
                <div class="join-date">Joined {{ formattedDate }}</div>
            </div>
        </div>

        <div class="stats">
            <div class="count"><span class="post-count">{{ profileStore.userDetails.posts }}</span> Posts</div>
            <div class="count"><span class="following-count">{{ profileStore.userDetails.following }}</span> Following</div>
            <div class="count"><span class="followers-count">{{ profileStore.userDetails.followers }}</span> Followers</div>
        </div>

        <section class="post-list">
            <PostItem v-for="post in profileStore.userPosts" :post="post" :key="post.id"/>
        </section>
    </template>
  </BaseLayout>
</template>

<script setup lang="ts">
import BaseLayout from '@/components/BaseLayout.vue';

import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useProfileStore } from '@/stores/profile';

import PostItem from '@/components/PostItem.vue';

const router = useRouter()
const profileStore = useProfileStore()
const username = ref(router.currentRoute.value.params.username)

profileStore.getUserDetails(username.value)
profileStore.getUserPosts(username.value)

const fullName = computed(() => {
    return `${profileStore.userDetails.firstName} ${profileStore.userDetails.lastName}`
})

const formattedDate = computed(() => {
    const date = new Date(profileStore.userDetails.dateJoined);
    const options = {year: 'numeric', month: 'long'};
    return date.toLocaleDateString('en-US', options)
})
</script>

<style scoped>
.profile-header {
    /* border: 1px solid blue; */
    display: flex;
    margin: 0 auto;
    padding: 20px;
    gap: 1rem;
}
.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    overflow: hidden;
    /* border: 1px solid green; */
}
.user-info {
    margin-left: 20px;
}

.name {
    font-size: 24px;
    font-weight: bold;
}

.username {
    color: #777;
}

.bio {
    margin-top: 10px;
}

.location {
    color: #777;
}

.join-date {
    color: #777;
}
.stats {
    display: flex;
    margin-top: 10px;
    justify-content: space-between;
    /* border: 1px solid blue; */
    padding: 0 20px;

}

.following-count, 
.followers-count,
.post-count {
    font-weight: 700;
    font-size: 16px;
    display: flex;
    justify-content: center;
    
}

.post-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 40px;
    gap: 1rem;
}
</style>