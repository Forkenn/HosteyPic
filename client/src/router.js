import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './page/Main_page.vue'
import AboutView from './page/About.vue'
import UserView from './page/User.vue'
import CodeErrorView from './page/CodeError.vue'
import UploadimgView from './page/Uploadimg.vue';
import EditProfileView from './page/EditProfile.vue'
import PicturePost from './page/PicturePost.vue'
import ChangeEmail from './page/ChangeEmail.vue'
import Verify from './page/Verify.vue'
import Adminpanel from './page/Adminpanel.vue'
import Subs from './page/Subs.vue'
import ResetPasword from './page/ResetPasword.vue'

const routes = [
    { path: '/', component: HomeView, name: "homeview" },
    { path: '/about', component: AboutView, name: "aboutview" },
    { path: '/user/:id', component: UserView, name: "userview" },
    { path: '/error', component: CodeErrorView, name: "codeerrorview", props: true },
    { path: '/upload', component: UploadimgView, name: "uploadimgview", props: true },
    { path: '/edit', component: EditProfileView, name: "editprofileview", props: true },
    { path: '/:pathMatch(.*)*', component: CodeErrorView },
    { path: '/post/:id', component: PicturePost, name: "postview" },
    { path: '/change-email', component: ChangeEmail, name: "changeemailview" },
    { path: '/verify', component: Verify, name: "verifyview" },
    { path: '/admin', component: Adminpanel, name: "adminpanelview" },
    { path: '/subscriptions', component: Subs, name: "subscriptionsview" },
    { path: '/reset-password', component: ResetPasword, name: "resetpasswordview" },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router