import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './page/Main_page.vue'
import AboutView from './page/About.vue'
import UserView from './page/User.vue'
import CodeErrorView from './page/CodeError.vue'
import UploadimgView from './page/Uploadimg.vue';
import EditProfileView from './page/EditProfile.vue'

const routes = [
    { path: '/', component: HomeView, name: "homeview" },
    { path: '/about', component: AboutView, name: "aboutview" },
    { path: '/user/:id', component: UserView, name: "userview" },
    { path: '/error', component: CodeErrorView, name: "codeerrorview", props: true },
    { path: '/upload', component: UploadimgView, name: "uploadimgview", props: true },
    { path: '/edit', component: EditProfileView, name: "editprofileview", props: true },
    { path: '/:pathMatch(.*)*', component: CodeErrorView }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router