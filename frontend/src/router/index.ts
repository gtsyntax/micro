import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '@/views/IndexView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView
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
      path: '/home',
      name: 'home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/messages',
      name: 'messages',
      component: () => import('@/views/MessageView.vue')
    },
    {
      path: '/bookmarks',
      name: 'bookmarks',
      component: () => import('@/views/BookmarkView.vue')
    }
  ]
})

export default router
