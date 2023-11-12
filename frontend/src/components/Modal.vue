<template>
    <div class="modal" v-if="showModal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>{{ headerText }}</h2>
                <span class="close" @click="closeModal"><CloseIcon /></span>
            </div>
            <div class="modal-body">
                <slot name="modal-body" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import CloseIcon from './icons/IconClose.vue';

const showModal = ref(false)

const props = defineProps({
    headerText: String
})

function openModal() {
    showModal.value = true;
}

function closeModal() {
    showModal.value = false;
}

defineExpose({
    openModal,
    closeModal,
})
</script>

<style scoped>
.modal {
    position: fixed;
    background-color: rgba(0, 0, 0, 0.5);
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
}

.modal-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgb(255, 255, 255);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    width: 700px;
    min-width: 400px;
    max-width: 500px;
    padding: 60px 40px;
}

.modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.close {
    display: flex;
    border-radius: 50%;
    padding: 5px;
    font-size: 20px;
    cursor: pointer;
    transition: color 0.3s, background-color 0.3s, transform 0.3s;
}

.close:hover {
    background-color: rgb(229, 233, 236);
}
</style>