<template>
    <BaseLayout>
    <template v-slot:center_column>
        <div class="container">
            <div class="card" v-if="postDetails">
                <div class="header">
                    <div class="avatar">
                        <img src="https://picsum.photos/150/" alt="User Avatar">
                    </div>
                    <div class="user-info">
                        <p class="name">{{ fullName }}</p>
                        <p class="username">@{{ postDetails.user.username }}</p>
                    </div>
                </div>
                <div class="main-content">
                    <p>{{ postDetails.content }}</p>
                </div>
                <div class="post-time">
                    <p>{{ postDateTime }}</p>
                </div>
            </div>
            <div class="post-stats">
                <p><span>34K</span> Reposts</p>
                <p><span>234</span> Quotes</p>
                <p><span>434K</span> Likes</p>
                <p><span>34</span> Bookmarks</p>
            </div>
        </div>
    </template>
    </BaseLayout>
</template>

<script setup lang="ts">
import BaseLayout from '@/components/BaseLayout.vue';
import { ref, computed } from "vue";
import { useRouter } from 'vue-router';
import axios from "axios";
import { formatDateTime } from "@/utils/formatDateTime";

const router = useRouter()
const postId = router.currentRoute.value.params.postId
const postDetails = ref(null)

const fullName = computed(() => {
    if(postDetails){
        return `${postDetails.value.user.first_name} ${postDetails.value.user.last_name}`
    }
})

const postDateTime = computed(() => {
    return formatDateTime(postDetails.value.created_at)
})

const getPostDetails = async () => {
    await axios.get(`/api/posts/${postId}`)
        .then(response => {
            console.log(response.data)
            postDetails.value = response.data
        })
        .catch(error => console.log(error))
}
getPostDetails()
</script>

<style scoped>
.container {
    margin-top: 20px;
}

.card {
    width: 600px;
    padding: 1rem;
    border: 1px solid #ccc;
}

.header {
    display: flex;
    gap: 1rem;
    margin-bottom: 10px;
}

.avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    overflow: hidden;
}

.name {
    font-weight: bold;
}

.username {
    color: #777;
}

.main-content {
    color: #000;
    margin-bottom: 20px;
    font-size: 1.1rem;
}

.post-time {
    color: #777;
}

.post-stats {
    display: flex;
    width: 600px;
    gap: 2rem;
    border-left: 1px solid #ccc;
    border-right: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    padding: 1rem;
    color: #777;
}
.post-stats span {
    color: #000;
    font-weight: bold;
}
</style>
