<template>
    <div class="tweet" v-for="post in props.posts">
        <RouterLink :to="{name: 'status', params: {username: post.user.username, postId: post.id}}">
            <img src="https://picsum.photos/150/" alt="Profile Picture" class="profile-picture">
            <div class="content">
                <div class="header">
                    <span class="full_name">{{ post.user.first_name }} {{ post.user.last_name }}</span>
                    <span class="dot">•</span>
                    <span class="username">@{{ post.user.username }}</span>
                    <span class="dot">•</span>
                    <span class="timestamp">{{ formatRelativeTime(post.created_at) }}</span>
                </div>
                <p>{{ post.content }}</p>
            </div>
        </RouterLink>
        <div class="icons">
            <div class="stats">
                <div class="stats-item">
                    <ReplyIcon />
                    0
                </div>
                <div class="stats-item">
                    <RepostIcon />
                    0
                </div>
                <div class="stats-item">
                    <LikeIcon />
                    0
                </div>
                <div class="stats-item">
                    <ViewIcon />
                    0
                </div>
            </div>

            <div class="other-btns">
                <div class="stats-item">
                    <FavouriteIcon />
                </div>
                <div class="stats-item">
                    <ShareIcon />
                </div>
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
    posts: Array
})
</script>

<style scoped>
a {
    display: grid;
    grid-template-columns: auto 1fr;
    color: #000;
}

.tweet {
      border-bottom: 1px solid #ccc;
      background-color: #fff;
      grid-template-rows: auto 1fr;
      padding: 1rem;
}

.profile-picture {
      width: 50px;
      height: 50px;
      object-fit: cover;
      margin: 10px;
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

.icons {
    display: flex;
    gap: 5rem;
    padding-right: 30px;
    padding-left: 70px;
}

.stats {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 5px;
    margin-bottom: 5px;
    flex: 1;
}

.other-btns {
    display: flex;
    gap: 1rem;
}

.stats-item {
    color: #777;
    cursor: pointer;
    display: flex;
    gap: 5px;
    align-items: center;
}
</style>
