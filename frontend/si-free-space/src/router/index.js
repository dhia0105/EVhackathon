import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import CreatePostPage from '../components/CreatePostPage.vue';
import SubmitInfoPage from '../components/SubmitInfoPage.vue'; // Import the new page

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/create-post',
    name: 'CreatePost',
    component: CreatePostPage
  },
  {
    path: '/submit-info',
    name: 'SubmitInfo',
    component: SubmitInfoPage // Add the new route for SubmitInfoPage
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;