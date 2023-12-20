<template>
    <div class="comment" v-for="comment in props.comments" :key="comment.id">
        <div class="comment-wrapper">
            <img src="https://picsum.photos/150/" alt="Profile Picture" class="profile-picture">
            <div class="content">
                <div class="header">
                    <span class="full_name">{{ comment.user.first_name }} {{ comment.user.last_name }}</span>
                    <span class="dot">•</span>
                    <span class="username">@{{ comment.user.username }}</span>
                    <span class="dot">•</span>
                    <span class="timestamp">{{ formatRelativeTime(comment.created_at) }}</span>
                </div>
                <p>{{ comment.content }}</p>
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
import ShareIcon from '@/components/icons/IconShare.vue';
import { formatRelativeTime } from '@/utils/formatTime';

const props = defineProps({
    comments: Array
})
</script>

<style scoped>
.comment {
      border-bottom: 1px solid #ccc;
      background-color: #fff;
      grid-template-rows: auto 1fr;
      padding: 1rem;
}

.comment-wrapper {
    display: grid;
    grid-template-columns: auto 1fr;
    color: #000;
    gap: 1rem;
}
.profile-picture {
      width: 50px;
      height: 50px;
      object-fit: cover;
      border-radius: 50%;
}

.dot {
    margin: 0 5px;
    color: #888;
}

.full_name {
    font-weight: bold;
}

.username, .timestamp {
      color: #666;
} 
</style>
