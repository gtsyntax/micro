<template>
    <form @submit.prevent="addComment" class="comment-form-wrapper">
        <img src="https://picsum.photos/60/" alt="" class="profile-image">
        <textarea v-model="newComment" placeholder="Add a comment..."></textarea>
        <button type="submit">Post</button>
    </form>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const newComment = ref("")
const router = useRouter()

const postId = router.currentRoute.value.params.postId

async function addComment() {
    try {
        const response = await axios.post(`/api/posts/${postId}/add_comment/`, {content: newComment.value})
        console.log(response.data)
    } catch(error) {
        console.error('Error adding comment:', error)
    }
}
</script>

<style scoped>
.comment-form-wrapper {
    padding: 1rem;
    display: grid;
    grid-template-columns: auto 1fr auto;
    gap: 1rem;
    border-bottom: 1px solid #ccc;
}

.profile-image {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 50%;
}

textarea {
    resize: none;
    font-size: 1rem;
    font-family: inherit;
    border: none;
    outline: none;
}

button {
    width: 100px;
    border-radius: 100px;
    outline: none;
    border: none;
    height: 40px;
    font-weight: bold;
    align-self: center;
    background-color: #1DA1F2;
    color: #FFFFFF;
}
</style>