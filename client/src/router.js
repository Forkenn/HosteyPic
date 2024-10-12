import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './page/Main_page.vue'
import AboutView from './page/About.vue'
import UserView from './page/User.vue'

const routes = [
    { path: '/', component: HomeView, name: "homeview" },
    { path: '/about', component: AboutView, name: "aboutview" },
    { path: '/user/:id', component: UserView, name: "userview" },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router