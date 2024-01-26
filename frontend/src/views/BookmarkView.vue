<template>
    <BaseLayout>
        <template v-slot:center_column>
        </template>
    </BaseLayout>
</template>

<script setup lang="ts">
import BaseLayout from '@/components/BaseLayout.vue';
import ReplyIcon from '@/components/icons/IconReply.vue';
import LikeIcon from '@/components/icons/IconLike.vue';
import RepostIcon from '@/components/icons/IconRepost.vue';
import ViewIcon from '@/components/icons/IconView.vue';
import FavouriteIcon from '@/components/icons/IconFavourite.vue';
import ShareIcon from '@/components/icons/IconShare.vue';
import { formatRelativeTime } from '@/utils/formatTime';
import { ref } from 'vue';
import axios from 'axios';

const bookmarks = ref([]) 

    const fetchUserBookmarks = async () => {
        try {
            const response = await axios.get('/api/bookmarks/')
            console.log(response.data)
            bookmarks.value = response.data
        } catch(error) {
            console.error('Error fetching bookmarks:', error)
        }
    }
    fetchUserBookmarks()
</script>

<style scoped>
</style>