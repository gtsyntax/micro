<template>
    <form @submit.prevent="publishPost" class="tweet-form">
        <img src="https://picsum.photos/60/" alt="" class="profile-image">
        <div class="tweet-form-actions">
            <textarea 
                name="tweet-form" 
                id="" 
                placeholder="What's happening?" 
                class="tweet-form-textarea"
                v-model="postContent"
            ></textarea>
            <div class="tweet-form-more-actions">
                <div 
                    class="tweet-char-tracker" 
                    v-bind:class="{
                        'success-color': postCharCount > 0,
                        'error-color': postCharCount > 280
                    }">{{ postCharCount }}</div>
                <button 
                    type="submit"
                    v-bind:class="{'disable-button': postCharCount === 0 || postCharCount > 280}"
                >Tweet</button>
            </div>
        </div>
    </form>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { usePostStore } from '@/stores/post';

const postContent = ref("");
const postStore = usePostStore()

const postCharCount = computed(() => {
    return postContent.value.trim().length
})

function publishPost() {
    console.log(postContent.value)
    postStore.publishPost(postContent.value)
    // postStore.publishNewTweet(tweetContent.value)
    // tweetContent.value = "";
    // showTweetModal.value = false;

}
</script>

<style scoped>
.profile-image {
    border-radius: 50%;
}
.tweet-form {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 10px;
}

.tweet-form-actions {
  display: grid;
  gap: 10px;
}
.tweet-form-textarea {
  resize: none;
  font-size: 16px;
  padding: 10px;
  height: 200px;
  outline: none;
  border: none;
  background-color: rgb(255, 255, 255);
  border-radius: 20px;
}

.tweet-form-more-actions {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 20px;
}

.success-color {
    color: rgb(0, 123, 255);
}

.error-color {
    color: rgb(248, 69, 69);;
}

.disable-button {
    pointer-events: none;
    opacity: 0.5;
}

button {
    display: block;
    width: 100px;
    height: 40px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 100px;
    cursor: pointer;
}
</style>