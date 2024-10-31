<template>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>main screen</title>

    </head>

    <body>
        <div v-if="show">
            <Login :login1="login" @authorised1="authorised1" @show_ch='show_login' />
            <div class="gray" @click=show_login(true)></div>
        </div>
        <div class="page">
            <HeaderNoAuth v-if="!authorised" @login='login_ch' @show_ch='show_login' />
            <HeaderAuth v-if="authorised" />


            <div class="userinfo__wrap">
                <div class="userinfo">
                    <div class="userIcon">
                        <img src="../assets/img/svg/userIconmain.svg" alt="">
                    </div>
                    <div class="userName">
                        <p>{{ userName }}</p>
                    </div>
                    <div class="subscribers">
                        <span class="countsubscribers">
                            <p>{{ countSubscribers }} подписчики</p>
                        </span>

                    </div>
                    <div class="socialmedia">
                        <div v-if="github" class="github">
                            <a :href=this.github target="_blank">
                                <img src="../assets/img/svg/GitHub.svg" alt="">
                            </a>
                        </div>
                        <div v-if="gitlab" class="gitlab">
                            <a :href=this.gitlab target="_blank">
                                <img src="../assets/img/svg/GitLab.svg" alt="">
                            </a>
                        </div>
                        <div v-if="vk" class="vk">
                            <a :href=this.vk target="_blank">
                                <img src="../assets/img/svg/VK.svg" alt="">
                            </a>
                        </div>
                        <div v-if="ok" class="ok">
                            <a :href=this.ok target="_blank">
                                <img src="../assets/img/svg/OK.svg" alt="">
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="tabs__wrap">
                <div class="create-line"></div>
                <div class="tabs">

                    <div class="tabs-header">

                        <button class="tabs-btn" @click="activeTab = 1" :class="{ active: activeTab === 1 }">Созданные
                        </button>
                        <button class="tabs-btn" @click="activeTab = 2"
                            :class="{ active: activeTab === 2 }">Понравившееся
                        </button>

                        <!-- <button class="tabs-btn" @click="activeTab = 3" :class="{ active: activeTab === 3 }">Альбомы
                        </button> -->
                    </div>
                    <div class="tabs-body">
                        <div class="tabs-body-item" v-show="activeTab === 1">
                            <p v-if="countImg == 0" style="margin-top: 75px;">Здесь пока ничего нет... Тогда
                                <button class="create" @click="goToUpload">
                                    Создай
                                </button>

                                что-нибудь!
                            </p>
                            <button v-else class="create" @click="goToUpload">
                                Создать
                            </button>
                            <Searchimg :res="result" :urlstr="'users/' + this.$route.params.id + '/posts'" />

                        </div>
                        <div class="tabs-body-item" v-show="activeTab === 2">
                            <Searchimg :res="liked" :urlstr="'users/' + this.$route.params.id + '/posts/liked'" />
                        </div>
                        <!-- <div class="tabs-body-item" v-show="activeTab === 3">
                            <div class="collections">
                                <img src="../assets/img/svg/Newcollection.svg" alt="">
                            </div>

                        </div> -->
                    </div>
                </div>
            </div>
            <Bottom />
        </div>


    </body>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');
@import '../assets/reset.css';

/* chewy-regular - latin */
@font-face {
    font-display: swap;
    /* Check https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display for other options. */
    font-family: 'Chewy';
    font-style: normal;
    font-weight: 400;
    src: url('../assets/fonts/chewy-v18-latin-regular.woff2') format('woff2');
    /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
}

html {
    box-sizing: border-box;
    caret-color: transparent;
}

*,
*::before,
*::after {
    box-sizing: inherit;
}

.gray {
    background-color: rgba(1, 1, 1, 0.75);
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    z-index: 1500;
}

.page {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}




.userinfo {

    width: 418px;
    height: 433px;
    margin-top: 60px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
}

.userIcon {
    margin-left: auto;
    margin-right: auto;
}

.userName {
    margin-left: auto;
    margin-right: auto;
    margin-top: 9px;
    font-family: Balsamiq Sans;
    font-size: 64px;
    font-weight: 400;
    line-height: 76.8px;
}

.subscribers {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;


    margin-left: auto;
    margin-right: auto;
    margin-top: 9px;
}

.socialmedia {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-left: auto;
    margin-right: auto;
    margin-top: 40px;
}

.github {
    margin-right: 14px;
}

.gitlab {
    margin-right: 14px;
}

.rutube {
    margin-right: 14px;
}

.vk {
    margin-right: 14px;
}

.ok {
    margin-right: 14px;
}


.tabs__wrap {
    position: sticky;
    margin-top: 47px;

    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
}


.tabs {

    max-width: 1440px;
    margin-left: auto;
    margin-right: auto;
}

.tabs-header {
    position: relative;
    display: block;
    margin-left: 80px;
}

button {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;
    padding: 0;
}

.tabs-btn {


    height: 50px;
    width: 280px;
    background-color: inherit;
    display: inline-block;
    color: rgba(53, 50, 50, 0.5);
    border-radius: 25px 25px 0 0;
    border: 4px solid rgba(177, 167, 63, 0.5);
    position: relative;
}

/* .tabs-btn.active::after {
    content: "";
    background-color: #000;
    height: 10px;
    width: 10px;
    z-index: 100;
} */


.tabs-btn.active {


    color: rgba(53, 50, 50, 1);
    border: 4px solid rgba(177, 167, 63, 1);
    border-bottom-color: rgb(255, 255, 255);
    /* border-bottom-width: 10px; */
    z-index: 10;
}

.create-line {
    position: absolute;
    top: 46px;
    width: 100%;
    border: 2px solid rgba(177, 167, 63, 1)
}


.tabs-body-item {
    margin-top: 34px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;

    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;


}

.create {
    width: 150px;
    height: 50px;

    margin-left: auto;
    margin-right: auto;
    margin-bottom: 20px;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1)
}

button.create:active {
    transform: scale(0.90);
}

.collections {
    margin-top: 70px;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: left;
    margin-bottom: 200px;
}
</style>

<script>
import Bottom from "../components/Bottom.vue"
import Searchimg from "../components/Searchimg.vue";
import HeaderAuth from "@/components/HeaderAuth.vue";
import HeaderNoAuth from "@/components/HeaderNoAuth.vue";
import Login from "@/components/Login.vue";
import axios from "axios";

const data = ['красивый фон.jpg', 'пальмы.jpg', 'test.jpg', 'vkTm8xmeOTo.jpg']

export default {
    components: { Login, Bottom, Searchimg, HeaderAuth, HeaderNoAuth },
    data() {
        return {
            authorised: false,
            login: true,
            show: false,
            activeTab: 1,
            userName: "Пользователь",
            countSubscribers: 0,
            result: [],
            liked: [],
            countImg: Math.floor(Math.random() * 10),
            user: {},
            github: "",
            gitlab: "",
            vk: "",
            ok: "",

        }

    },
    mounted() {

        axios({
            timeoute: 1000,
            method: 'get',
            url: import.meta.env.VITE_BACKEND_URL + 'users/current',

            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                if (response.status == 200) {
                    this.user = response.data
                    this.authorised = true
                }
                // console.log(response);
            })
            .catch(error => {
                // console.log(error.message);
            });

        axios({
            timeoute: 1000,
            method: 'get',
            url: import.meta.env.VITE_BACKEND_URL + `users/${this.$route.params.id}/posts?start=0&end=20`,

            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.result = response.data.items
                // console.log(this.result);
                // console.log(response.data)

            })
            .catch(error => {
                console.log(error.message);
            });


        axios({
            timeoute: 1000,
            method: 'get',
            url: import.meta.env.VITE_BACKEND_URL + `users/${this.$route.params.id}/posts/liked?start=0&end=20`,

            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.liked = response.data.items
                // console.log(this.result);
                // console.log(response.data)

            })
            .catch(error => {
                console.log(error.message);
            });


        axios({
            timeoute: 1000,
            method: 'get',
            url: (import.meta.env.VITE_BACKEND_URL + `users/${this.$route.params.id}`),
            // params: {
            //     user_id: this.$route.params.id
            // },
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                if (response.status == 200) {
                    console.log(response);
                    this.userName = response.data.username
                    this.github = response.data.github_link
                    this.gitlab = response.data.gitlab_link
                    this.vk = response.data.vk_link
                    this.ok = response.data.ok_link
                }

            })
            .catch(error => {
                if (error.status != null) {
                    this.$router.push({
                        name: 'codeerrorview',
                        query: {
                            ErrorNum: error.status
                        }
                    })
                }
            });
        // this.loadImg(this.countImg);
    },
    methods: {
        authorised1(authorised) {
            this.authorised = authorised
        },
        show_login(show) {
            // console.log(show, this.login)
            if (show) {
                this.show = false
            }
            else {
                this.show = true
            }

        },
        login_ch(login) {
            this.login = login
        },
        goToUpload() {
            this.$router.push({ name: 'uploadimgview' })
        },
        loadImg(tagImg) {
            this.result = []

            if (this.activeTab == 1) {
                if (tagImg)
                    this.countImg = tagImg
                tagImg = this.countImg
            }
            else {
                tagImg = 10
            }

            for (let index = 0; index < tagImg; index++) {

                this.srcimg = data[index % 3],
                    this.result.push({
                        src1: this.srcimg,
                        tag: this.tag
                    })
            }
        },
    }
}
</script>