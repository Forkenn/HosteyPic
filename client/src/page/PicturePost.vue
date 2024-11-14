<template>
    <div v-if="show">
        <Login :login1="login" @authorised1="authorised1" @show_ch='show_login' />
        <div class="gray" @click=show_login(true)></div>
    </div>
    <div v-show="visable.post & visable.user & visable.userid" class="page">
        <HeaderNoAuth v-if="!authorised" @login='login_ch' @show_ch='show_login' />
        <HeaderAuth v-if="authorised" />

        <div>
            <div class="wrap">
                <div class="picture_wrap">
                    <img :src="'../../dist/uploads/attachments/original/' + image.attachment" alt="">
                </div>

                <div class="info_wrap">
                    <div class="actio_wrap">
                        <div style="  max-width: 798px; height: 60px; display: flex; flex-wrap: wrap;">
                            <div class="button_act">
                                <button v-if="!image.is_liked" @click="liked">
                                    <img src="../assets/img/svg/Heart.svg" alt="Like">
                                </button>
                                <button v-else @click="unliked" style="background: rgba(177, 167, 63, 1);">
                                    <img src="../assets/img/svg/Heartwhite.svg" alt="Like">
                                </button>
                                <span class="text_p">
                                    <p>{{ image.likes_count }}</p>
                                </span>

                            </div>
                            <div class="button_act">
                                <button>
                                    <img src="../assets/img/svg/Plus.svg" alt="add">
                                </button>
                            </div>
                            <div class="button_act">
                                <button>
                                    <a download :download="image.name"
                                        :href="'../../dist/uploads/attachments/original/' + image.attachment"
                                        title="ImageName">
                                        <img src="../assets/img/svg/Download_white.svg" alt="Download">
                                    </a>

                                </button>
                            </div>
                            <!-- <div class="button_act">
                                <button style="background: rgba(189, 38, 38, 1);">
                                    <img width="30px" src="../assets/img/svg/AlertCircle.svg" alt="Alert">
                                </button>
                            </div> -->
                            <div v-if="user.is_moderator | image.is_deletable" class="button_act">
                                <button style="background: rgba(189, 38, 38, 1);">
                                    <img width="30px" src="../assets/img/svg/Trash.svg" alt="Trash">
                                </button>
                            </div>
                        </div>
                        <div>
                            <div class="button_go">
                                <button style="background: rgba(177, 167, 63, 1);">
                                    <img width="30px" src="../assets/img/svg/go_back.svg" alt="go back"></button>
                            </div>
                        </div>
                    </div>

                    <div class="user_info">
                        <img @click="goToUser" :src="'../../dist/uploads/avatars/original/' + userid.avatar" alt="">
                        <div class="user_text">
                            <p>{{ userid.username }}</p>
                            <div class="sub">
                                <p>Подписчики {{ userid.followers_count }}</p>
                            </div>
                        </div>
                        <button v-show="user.id != userid.id & !userid.is_following"
                            @click="followed">Подписаться</button>


                        <button v-show="user.id != userid.id & userid.is_following" @click="unfollowed">
                            Отписаться
                        </button>
                    </div>

                    <div class="post_info">
                        <div class="title">
                            <p>{{ image.title }}
                            </p>
                        </div>
                        <div class="description">
                            <p>{{ image.body }}</p>
                        </div>

                    </div>
                </div>


            </div>
        </div>
        <Bottom />
    </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');
@import '../assets/reset.css';

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


.wrap {

    max-width: 1440px;
    margin: auto;
    display: flex;
    justify-content: space-between;
}

.picture_wrap {
    margin-top: 40px;
    width: 420px;
    min-width: 200px;
    height: 600px;
    margin-left: 80px;

}

.picture_wrap img {
    width: 100%;
    border-radius: 50px;
    border: 4px solid rgba(177, 167, 63, 1)
        /* height: 100%; */
}

.info_wrap {
    margin-top: 40px;
    /* width: 100%; */
    /* max-width: 782px; */
    width: calc(100% - 420px - 62px - 80px);
    /* height: 600px; */
    /* display: flex;
    flex-wrap: wrap; */
    margin-left: 62px;
    margin-right: 80px;
}

.actio_wrap {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    height: 60px;
    justify-content: space-between;
}

.actio_wrap button {

    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 0;
    background: rgba(71, 67, 25, 1);
    display: flex;
    align-items: center;
    justify-content: center;
}

.button_act {
    display: flex;
    align-items: center;
    height: 60px;
    margin-right: 30px;

}

.button_act .text_p {
    max-width: 135px;
    overflow: hidden;
}

.button_act p {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

    width: 100%;
    margin-left: 15px;
}



/* .button_go {} */

.user_info {
    margin-top: 40px;
    width: 100%;
    height: 100px;
    display: flex;
    flex-wrap: wrap;
    /* justify-content: space-between; */
    align-items: center;
    /* width: 100px; */
}

.user_info img {
    width: 100px;
    border-radius: 50%;
    border: 4px solid rgba(177, 167, 63, 1)
}

.user_text {
    max-width: calc(100% - 100px - 226px - 60px);
    margin-left: 30px;
    display: flex;
    flex-wrap: wrap;
    justify-content: start;
    overflow: hidden;
}


.user_text p {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

    width: 100%;
}



.user_text .sub p {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;

    color: rgba(71, 67, 25, 1);

    width: 100%;
}

.user_info button {
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: center;
    color: rgba(71, 67, 25, 1);


    margin-left: 30px;
    width: 226px;
    height: 55px;

    border-radius: 30px;

    border: 4px solid rgba(177, 167, 63, 1)
}

.user_info button:active {
    transform: scale(0.9);
}

.post_info {
    margin-top: 40px;
    width: 100%;
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

}

.title {
    width: 100%;
    height: 38px;
}

.description {
    font-family: Balsamiq Sans;
    font-size: 20px;
    font-weight: 400;
    line-height: 24px;
    text-align: left;

}

button {
    cursor: pointer;
}
</style>

<script>
import HeaderAuth from '@/components/HeaderAuth.vue';
import HeaderNoAuth from "@/components/HeaderNoAuth.vue";
import Login from "@/components/Login.vue";
import Bottom from '@/components/Bottom.vue';
import axios from 'axios';

export default {
    components: { Login, Bottom, HeaderAuth, HeaderNoAuth },
    data() {
        return {
            visable: {
                userid: false,
                user: false,
                post: false,
            },
            authorised: false,
            file: Object,
            username: "asd",
            avatar: "",
            subscribers: 0,
            image: {},
            show: false,
            user: {},
            userid: {},
            moder: false
        }
    },
    mounted() {
        axios({
            timeoute: 1000,
            method: 'get',
            url: (import.meta.env.VITE_BACKEND_URL + `posts/${this.$route.params.id}`),
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.image = response.data
                console.log(response.data)

                axios({
                    timeoute: 1000,
                    method: 'get',
                    url: (import.meta.env.VITE_BACKEND_URL + `users/${this.image.user_id}`),
                    // params: {
                    //     user_id: this.$route.params.id
                    // },
                    withCredentials: true,
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(response => {
                        console.log(response.data)
                        if (response.status == 200) {

                            this.userid = response.data
                        }

                    })
                    .catch(error => {
                        console.log(error.message);
                    })
                    .finally(() => {
                        this.visable.userid = true
                    });

            })
            .catch(error => {
                console.log(error.message);
            })
            .finally(() => {
                this.visable.post = true
            });;
        axios({
            timeoute: 1000,
            method: 'get',
            url: (import.meta.env.VITE_BACKEND_URL + `users/current`),
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
                    this.user = response.data

                    // this.moder = response.data.is_moderator
                    this.authorised = true
                }

            })
            .catch(error => {
                if (error.status != null) {
                    // this.$router.push({
                    //     name: 'codeerrorview',
                    //     query: {
                    //         ErrorNum: error.status
                    //     }
                    // })
                }
            })
            .finally(() => {
                this.visable.user = true
            });
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
        goToUser() {
            this.$router.push({ name: 'userview', params: { id: this.userid.id } })
        },
        liked() {
            console.log(123)
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `likes/posts/${this.image.id}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {

                    this.image.is_liked = true
                    this.image.likes_count++

                })
                .catch(error => {
                    console.log(error)
                });
        },
        unliked() {
            axios({
                timeoute: 1000,
                method: 'delete',
                url: (import.meta.env.VITE_BACKEND_URL + `likes/posts/${this.image.id}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {

                    this.image.is_liked = false
                    this.image.likes_count--

                })
                .catch(error => {
                    console.log(error)
                });
        },
        followed() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: import.meta.env.VITE_BACKEND_URL + `users/${this.userid.id}/follow`,

                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.userid.followers_count++
                    this.userid.is_following = true
                    console.log(response);
                })
                .catch(error => {
                    // console.log(error.message);
                });
        },
        unfollowed() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: import.meta.env.VITE_BACKEND_URL + `users/${this.userid.id}/unfollow`,

                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.userid.followers_count--
                    this.userid.is_following = false
                    console.log(response);
                })
                .catch(error => {
                    // console.log(error.message);
                });
        },
    },

}

</script>
