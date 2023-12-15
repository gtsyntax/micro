<template>
    <div class="wrapper">
        <aside class="left_column">
            <div class="top">
                <RouterLink to="/home">
                    <HomeIcon />
                    <h2 class="menu-name">Home</h2>
                </RouterLink>

                <RouterLink to="#">
                    <SearchIcon />
                    <h2 class="menu-name">Explore</h2>
                </RouterLink>

                <RouterLink to="#">
                    <NotificationIcon />
                    <h2 class="menu-name">Notifications</h2>
                </RouterLink>

                <RouterLink to="/messages">
                    <MessageIcon />
                    <h2 class="menu-name">Messages</h2>
                </RouterLink>

                <RouterLink to="#">
                    <ContactIcon />
                    <h2 class="menu-name">Communities</h2>
                </RouterLink>

                <RouterLink to="#">
                    <BookmarkIcon />
                    <h2 class="menu-name">Bookmarks</h2>
                </RouterLink>

                <RouterLink :to="{name: 'profile', params: {username:username}}">
                    <ProfileIcon />
                    <h2 class="menu-name">Profile</h2>
                </RouterLink>

                <RouterLink to="" @click="openPostModal">
                    <CreateIcon class="create_icon"/>
                    <h2 class="menu-name">Post</h2>
                </RouterLink>
            </div>

            <div class="bottom">
                <RouterLink to="#">
                    <LogoutIcon />
                    <h2 class="menu-name">Logout</h2>
                </RouterLink>
            </div>
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
import LogoutIcon from './icons/IconLogout.vue';

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

.menu-name {
    display: none;
}

.left_column {
    border-right: 1px solid #ccc;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
}

.left_column .top {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    flex: 1;
    gap: 2rem;
}

.left_column .top a,
.left_column .bottom a {
    color: #000;
}

@media (min-width: 768px) {
    .wrapper {
        grid-template-columns: 1fr 4fr;
    }
}
</style>
