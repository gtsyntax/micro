<template>
    <div class="wrapper">
        <aside class="left_column">
            <RouterLink to="/timeline">
                <HomeIcon />
            </RouterLink>

            <RouterLink to="#">
                <SearchIcon />
            </RouterLink>

            <RouterLink to="#">
                <NotificationIcon />
            </RouterLink>

            <RouterLink to="/messages">
                <MessageIcon />
            </RouterLink>

            <RouterLink to="#">
                <ContactIcon />
            </RouterLink>

            <RouterLink to="#">
                <BookmarkIcon />
            </RouterLink>

            <RouterLink :to="{name: 'profile', params: {username:username}}">
                <ProfileIcon />
            </RouterLink>

            <CreateIcon @click="openPostModal" class="create_icon"/>
        </aside>
        <main class="center_column">
            <slot name="center_column"/>
        </main>
    </div>
    <Modal ref="childPostModal">
        <template v-slot:modal-body>
            <PostForm @closePostModal="closePostModal"/>
        </template>
    </Modal>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { RouterLink } from 'vue-router';
import HomeIcon from './icons/IconHome.vue';
import SearchIcon from './icons/IconSearch.vue';
import NotificationIcon from './icons/IconNotification.vue';
import MessageIcon from './icons/IconMessage.vue';
import ContactIcon from './icons/IconContact.vue';
import BookmarkIcon from './icons/IconBookmark.vue';
import ProfileIcon from './icons/IconProfile.vue';
import CreateIcon from './icons/IconCreate.vue';

import PostForm from './PostForm.vue';
import Modal from './Modal.vue';
import { useAccountStore } from "@/stores/account";

const childPostModal = ref(null)
const username = ref(null)
const accountStore = useAccountStore()

username.value = accountStore.user.username;

function openPostModal() {
    childPostModal.value.openModal()
}

function closePostModal() {
    childPostModal.value.closeModal()
}
</script>

<style>
.wrapper {
    max-width: 1280px;
    min-width: 456px;
    margin: 0 auto;
    min-height: 100vh;
    display: grid;
    grid-template-columns: 70px 1fr;
}

.left_column {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
    padding-top: 20px;
}

.center_column {
    padding: 0 1rem;
}

/* .right_column {
    border: 1px solid red;
} */

.create_icon {
    cursor: pointer;
}

@media (min-width: 768px) {
    .wrapper {
        grid-template-columns: 1fr 4fr;
    }
}
</style>
