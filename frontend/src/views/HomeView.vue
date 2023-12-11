<template>
  <div class="wrapper">
      <h1 class="heading-lg">Happening now</h1>

      <div class="onboarding-wrapper">
        <h3 class="heading-md">Join today.</h3>
        <div class="onboarding-btns">
          <button class="base-btn">Sign up with Google</button>
          <button class="base-btn">Sign up with Apple</button>
          <button class="base-btn" @click="openSignUpModal">Create account</button>
        </div>
        <p class="terms-note">
            By signing up, you agree to the Terms of Service and
            Privacy Policy, including Cookie Use.
        </p>
      </div>

      <div class="sign-in-area">
        <h5 class="heading-sm">Already have an account?</h5>
        <button class="base-btn" @click="openSignInModal">Sign in</button>
      </div>
  </div>

  <Modal :headerText="signUpModal.header" ref="childSignUpModal">
    <template v-slot:modal-body>
      <SignUpForm />
    </template>
  </Modal>

  <Modal :headerText="signInModal.header" ref="childSignInModal">
    <template v-slot:modal-body>
      <SignInForm />
    </template>
  </Modal>
</template>

<script setup lang="ts">
import Modal from '@/components/Modal.vue';
import SignInForm from '@/components/SignInForm.vue';
import SignUpForm from '@/components/SignUpForm.vue';
import { ref } from 'vue';

const childSignUpModal = ref(null)
const signUpModal = ref({
  header: "Sign Up",
})

const childSignInModal = ref(null)
const signInModal = ref({
  header: "Sign In",
})

function openSignUpModal() {
  childSignUpModal.value.openModal()
}

function openSignInModal() {
  childSignInModal.value.openModal()
}
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  min-height: 100vh;
  border: 1px solid green;
}
.heading-lg {
  font-size: 64px;
  line-height: 84px;
  font-weight: 700;
  color: rgb(15, 20, 25);
}
.heading-md {
  font-size: 31px;
  line-height: 36px;
  font-weight: 700;
  color: rgb(15, 20, 25);
}
.heading-sm {
  font-size: 17px;
  line-height: 20px;
  font-weight: 700;
  color: rgb(15, 20, 25);
}

.onboarding-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: center;
  /* border: 1px solid green; */
}

.onboarding-btns {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.base-btn {
  height: 50px;
  width: 380px;
  background-color: rgba(0,0,0,0);
  cursor: pointer;
  outline-style: none;
  border: 1px solid rgb(207, 217, 222);
  border-radius: 100px;
  font-size: 15px;
  font-weight: 700;
}

.terms-note {
  line-height: 20px;
  font-size: 15px;
  font-weight: 400;
  width: 380px;
}

.sign-in-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}
</style>
