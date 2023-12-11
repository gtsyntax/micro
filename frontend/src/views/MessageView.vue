<template>
    <BaseLayout>
        <template v-slot:center_column>
            <div class="container">
                <template v-if="chats">
                    <aside class="contacts">
                        <div v-for="chat in chats" v-bind:key="chat.id" class="contact-item">
                            <div class="avatar">
                                <img src="https://picsum.photos/150/" alt="User Avatar">
                            </div>
                            <div class="contact-item-info">
                                <header>
                                    <p class="name" v-for="user in chat.participants" 
                                    v-bind:key="user.id">
                                    <span v-if="user.id !== accountStore.user.id">
                                        {{ `${user.first_name} ${user.last_name}` }}
                                    </span></p>
                                    <p class="silent">{{ humanizedDate }}</p>
                                </header>
                                <p class="silent">It's so nice hearing from you...</p>
                            </div>
                        </div>
                    </aside>
                    <section class="chat-area">
                        <div class="chat-history" v-if="activeChat">
                            <!-- Chat history will go here -->
                            <template v-for="message in activeChat.messages" v-bind:key="message.id">
                                <div class="message outgoing" v-if="message.sender.id === accountStore.user.id">
                                    <p>{{ message.content }}</p>
                                </div>
                                <div class="message incoming" v-else>
                                    <p>{{ message.content }}</p>
                                </div>
                            </template>
                        </div>
                        <form @submit.prevent="sendMessage" class="chat-box">
                            <input type="text" v-model="chatMessage" placeholder="Chat message..." />
                            <button>Send</button>
                        </form>
                    </section>
                </template>
                <template v-else>
                    <h1>No active chats</h1>
                </template>
            </div>
        </template>
    </BaseLayout>
</template>

<script setup lang="ts">
    import {ref, computed,} from "vue";
    import axios from "axios";
    import BaseLayout from '@/components/BaseLayout.vue';
    import { useAccountStore } from "@/stores/account";
    import { formatRelativeTime } from '@/utils/formatTime';

    const chats = ref(null);
    const chatMessage = ref("");
    const activeChat = ref(null);
    const accountStore = useAccountStore()

    const getChatMessage = async chat => {
        try {
            const response = await axios.get(`/api/chats/${chat.id}/`);
                //console.log(response.data);
                activeChat.value = response.data;
        } catch(error) {
            console.error("Error:", error)
        }
    }

    const getChats = async () => {
        try {
            const response = await axios.get(`/api/chats/`);
               //console.log(response.data)
               if (response.data) {
                    chats.value = response.data
                    getChatMessage(chats.value[0])
                }
        } catch(error) {
            console.error("Error:", error)
        }
    }
    getChats()
    
    const sendMessage = async () => {
        console.log({content:chatMessage.value});
        await axios.post(`/api/chats/${activeChat.value.id}/send-chat/`,{content:chatMessage.value})
            .then(response => {
               activeChat.value.messages.push(response.data)
            })
            .catch(error => console.error(error))
        chatMessage.value = ""
    }

    const humanizedDate = computed(() => {
        for(const chat of chats.value){
            return formatRelativeTime(chat.updated_at)
        }
    })
</script>

<style scoped>
.container {
    display: grid;
    grid-template-columns: 1fr 2fr;
    margin-top: 20px;
    height: 90vh;
}

.contacts {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.contact-item {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 1rem;
}
.contact-item-info header {
    display: flex;
    justify-content: space-between;
}

.name {
    font-weight: bold;
    font-size: 1.1rem;
}

.silent {
    color: #777;
}

.chat-area {
    display: flex;
    flex-direction: column;
}

.chat-history {
    flex: 1 0 500px;
    overflow-y: scroll;
    padding: 0 10px;
}

.message p {
    background-color: #e6e6e6;
    padding: 10px;
    border-radius: 10px;
    display: inline-block;
    color: #000000;
    max-width: 70%;
}

.incoming {
    text-align: left;
    margin: 10px 0;
}


.outgoing {
    text-align: right;
    margin: 10px 0;
}

.outgoing p {
    background-color: #007BFF;
    color: #FFFFFF;
}


.chat-box {
    display: flex;
}

.chat-box input {
    flex: 1;
    outline: none;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
}

.chat-box button {
    padding: 10px;
    margin-left: 10px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    overflow: hidden;
}
</style>
