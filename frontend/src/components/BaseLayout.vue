<template>
    <div class="wrapper">
        <aside class="left_column">
            <RouterLink to="#">
                <HomeIcon />
            </RouterLink>

            <RouterLink to="#">
                <SearchIcon />
            </RouterLink>

            <RouterLink to="#">
                <NotificationIcon />
            </RouterLink>

            <RouterLink to="#">
                <MessageIcon />
            </RouterLink>

            <RouterLink to="#">
                <ContactIcon />
            </RouterLink>

            <RouterLink to="#">
                <BookmarkIcon />
            </RouterLink>

            <RouterLink to="">
                <ProfileIcon />
            </RouterLink>

            <CreateIcon @click="openPostModal" class="create_icon"/>
        </aside>
        <main class="center_column">
            <slot name="center_column"/>
        </main>
        <aside class="right_column">
            <slot name="right_column"/>
        </aside>
    </div>
    <Modal ref="childPostModal">
        <template v-slot:modal-body>
            <PostForm />
        </template>
    </Modal>
</template>

<script setup lang="ts">
import { ref } from 'vue';
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
const childPostModal = ref(null)

function openPostModal() {
    childPostModal.value.openModal()
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
        grid-template-columns: 1fr 1.5fr 1fr;
    }
}
</style>