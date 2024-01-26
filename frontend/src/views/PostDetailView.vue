<template>
    <BaseLayout>
    <template v-slot:center_column>
        <div class="container">
            <main>
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
                    <div class="post-stats-item">
                        <ReplyIcon />
                        {{ postDetails && postDetails.comments.length }}
                    </div>
                    <div class="post-stats-item">
                        <RepostIcon />
                        {{ postDetails && postDetails.reposts.length }}
                    </div>
                    <div class="post-stats-item">
                        <LikeIcon />
                        {{ postDetails && postDetails.likes.length }}
                    </div>
                    <div class="post-stats-item">
                        <FavouriteIcon />
                        {{ postDetails && postDetails.bookmarks.length }}
                    </div>
                </div>
                <CommentForm />
                <CommentList v-if="postDetails" :comments="postDetails.comments" />
            </main>
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
import ReplyIcon from '@/components/icons/IconReply.vue';
import LikeIcon from '@/components/icons/IconLike.vue';
import RepostIcon from '@/components/icons/IconRepost.vue';
import FavouriteIcon from '@/components/icons/IconFavourite.vue';
import ShareIcon from '@/components/icons/IconShare.vue';
import CommentList from '@/components/CommentList.vue';
import CommentForm from '@/components/CommentForm.vue';

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
    display: grid;
    grid-template-columns: 2fr 1fr;
    height: 100vh;
}

main {
    border-right: 1px solid #ccc;
}


.card {
    width: 100%;
    padding: 1rem;
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
    width: 100%;
    gap: 2rem;
    border-bottom: 1px solid #ccc;
    border-top: 1px solid #ccc;
    padding: 1rem;
    color: #777;
    justify-content: space-between;
}

.post-stats-item {
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 5px;
}
</style>
