<template>
    <form @submit.prevent="handleRegister">
        <section>
            <div class="txt_field">
                <input type="text" id="name" v-model="formData.first_name" required/>
                <span></span>
                <label for="name">Name</label>
            </div>

            <div class="txt_field">
                <input type="text" id="surname" v-model="formData.last_name" required/>
                <span></span>
                <label for="surname">Surname</label>
            </div>
        </section>

        <section>
            <div class="txt_field">
                <input type="text" id="username" v-model="formData.username" required/>
                <span></span>
                <label for="username">Username</label>
            </div>

            <div class="txt_field">
                <input type="email" id="email" v-model="formData.email" required/>
                <span></span>
                <label for="email">Email</label>
            </div>
        </section>

        <div class="txt_field">
            <input type="password" id="password" v-model="formData.password" required/>
            <span></span>
            <label for="password">Password</label>
        </div>

        <input type="submit" value="Sign Up">
    </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const formData = ref({
  email: '',
  password: '',
  username: '',
  first_name: '',
  last_name: ''
})

async function handleRegister() {
  await axios.post('/api/accounts/register/', formData.value)
  .then(response => {
    console.log(response)
  }).catch(error => {
    console.log('error', error)
  })
}
</script>

<style scoped>
form .txt_field {
  position: relative;
  margin: 30px 0;
}

section {
    display: flex;
    gap: 2rem;
}

.txt_field input {
  width: 100%;
  height: 50px;
  padding: 0 5px;
  font-size: 1rem;
  border: none;
  background: none;
  outline: none;
}

.txt_field label {
  position: absolute;
  top: 50%;
  left: 5px;
  color: #777;
  transform: translateY(-50%);
  font-size: 1rem;
  pointer-events: none;
  transition: .2s;
}

.txt_field span::before {
  content: '';
  position: absolute;
  top: 40px;
  left: 0;
  width: 0%;
  height: 2px;
  background: hsla(211, 100%, 50%, 1);
  transition: .2s;
}

.txt_field input:focus ~ label,
.txt_field input:valid ~ label {
  top: -5px;
  color: hsla(211, 100%, 50%, 1);
}

.txt_field input:focus ~ span::before,
.txt_field input:valid ~ span::before {
  width: 100%;
}

/* .note {
  margin: -5px 0 20px 5px;
  color: #777;
} */

input[type="submit"] {
  width: 100%;
  height: 50px;
  background-color: hsla(120, 33%, 1%, 1);
  border: 1px solid hsla(120, 33%, 1%, 1);
  color: rgb(255, 255, 255);
  cursor: pointer;
  outline: none;
  border-radius: 100px;
  font-size: 15px;
  font-weight: 700;
}

input[type="submit"]:hover {
  background-color: hsla(120, 33%, 1%, .9);
  transition: .3s;
}

.sign-link {
  text-align: center;
  margin: 30px 0;
  color: #777;
}

.sign-link a {
  color: hsla(211, 100%, 50%, 1);
}

.sign-link a:hover {
  text-decoration: underline;
}
</style>