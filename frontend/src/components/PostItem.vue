<template>
    <div class="tweet-card">
        <img class="user-avatar" src="user-avatar.jpg" alt="User Avatar">
        <div class="user-info">
            <div>{{ fullName }}</div>
            <div>@{{ props.post.user.username }}</div>
        </div>
        <p class="tweet-text">{{ props.post.content }}</p>
        <div class="timestamp">{{ humanizedDate }}</div>
        <div class="interaction-buttons">
            <div class="interaction-buttons-left-col">
                <span class="interaction-button"><ReplyIcon /> 32K replies</span> <!-- Reply button -->
                <span class="interaction-button"><RepostIcon /> 12K reposts</span> <!-- Retweet button -->
                <span class="interaction-button"><LikeIcon /> 243K likes</span> <!-- Like button -->
                <span class="interaction-button"><ViewIcon /> 45.5M views</span> <!-- View button -->
            </div>

            <div class="interaction-buttons-right-col">
                <span class="interaction-button"><FavouriteIcon /></span> <!-- Favourite button -->
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import ReplyIcon from '@/components/icons/IconReply.vue';
import LikeIcon from '@/components/icons/IconLike.vue';
import RepostIcon from '@/components/icons/IconRepost.vue';
import ViewIcon from '@/components/icons/IconView.vue';
import FavouriteIcon from '@/components/icons/IconFavourite.vue';
import { computed } from 'vue';
import { formatRelativeTime } from '@/utils/formatTime';

const props = defineProps({
    post: Object
})

const fullName = computed(() => {
    return `${props.post.user.first_name} ${props.post.user.last_name}`
})

const humanizedDate = computed(() => {
    return formatRelativeTime(props.post.created_at)
})
</script>

<style scoped>
.tweet-card {
    width: 500px;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px;
    display: inline-block;
}

.user-avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    overflow: hidden;
    margin-right: 10px;
    float: left;
}

.user-info {
    font-weight: bold;
}

.tweet-text {
    clear: both;
    margin-top: 10px;
}

.timestamp {
    color: #777;
}

.interaction-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 5px;
    margin-bottom: 5px;
}

.interaction-button {
    color: #777;
    cursor: pointer;
    display: flex;
    gap: 5px;
    align-items: center;
}

.interaction-buttons-left-col {
    display: flex;
    gap: 10px;
}
</style>