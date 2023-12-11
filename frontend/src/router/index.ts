import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/:username',
      name: 'profile',
      component: () => import('@/views/ProfileView.vue'),
    },
    {
        path: '/:username/status/:postId',
        name: 'status', 
        component: () => import('@/views/PostDetailView.vue'),
    },
    {
      path: '/timeline',
      name: 'timeline',
      component: () => import('@/views/TimelineView.vue')
    },
    {
      path: '/messages',
      name: 'messages',
      component: () => import('@/views/MessageView.vue')
    },
  ]
})

export default router
