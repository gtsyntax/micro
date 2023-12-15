<template>
    <BaseLayout>
        <template v-slot:center_column>
            <div class="empty-post-list" v-if="posts.length === 0">
                <p>POSTS OF USERS YOU FOLLOW WILL APPEAR HERE.</p>
            </div>
            <PostList :posts="posts" v-else/>
        </template>
    </BaseLayout>
</template>

<script setup lang="ts">
    import BaseLayout from '@/components/BaseLayout.vue';
    import PostList from '@/components/PostList.vue';
    import axios from "axios";
    import { ref } from 'vue';

    const posts = ref([]) 

    const fetchHomeTimeline = async () => {
        await axios.get("/api/home-timeline")
            .then(response => {
                console.log(response.data)
                posts.value = response.data
            })
            .catch(error => console.error("Error fetching tweets", error))
    }
    fetchHomeTimeline()
</script>

<style scoped>
.empty-post-list {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
</style>
