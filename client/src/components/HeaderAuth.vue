<template>
    <Announcement v-show="showannouncement" @showannouncement=ShowAnnouncement :email="this.user.email" :edit="true" />
    <header class="header">
        <div v-show="loading" class="wrapper__header">
            <div v-if="!user.is_verified" @click="verefi(); ShowAnnouncement()" class="alert">
                <p>Подтвердите почту!</p>
            </div>
            <div v-if="countshow == '11'" class="confirme">
                <p>Почта подтверждена!</p>
            </div>
            <div class="header__logo">
                <p> <span class="color__white">Hostey</span>
                    <span class="color__black">PIC</span>
                </p>
                <img v-show="this.$route.name == 'userview' & user.is_moderator & user.id != this.$route.params.id"
                    style="margin-left: 40px;" @click="show_moder()" src="../assets/img/svg/Settings.svg" alt="">
                <div v-show="showmoder" class="moder_menu">
                    <div class="moder_head">
                        <div class="moder-btn" style="margin-top: 26px;"></div>
                        <button v-show="user.is_superuser" class="moder-btn" v-if="!userid.is_moderator"
                            @click="mod_user()">
                            Повысить
                        </button>
                        <button v-show="user.is_superuser" class="moder-btn" v-else @click="unmod_user()">
                            Понизить
                        </button>
                        <button class="moder-btn" v-if="userid.is_active" v-on:click="ban_user()">
                            Заблокировать
                        </button>
                        <button class="moder-btn" v-else v-on:click="unban_user()">
                            Разблокировать
                        </button>
                        <button v-show="user.is_superuser" class="moder-btn" @click="delete_user()">
                            Удалить
                        </button>
                    </div>
                </div>
            </div>
            <div class="nav">
                <p style="margin-left: 0;" @click="goToHome">Главная</p>
                <p @click="goToSubs">Подписки</p>
            </div>
            <div class="user__icon">
                <img :src="`../../dist/uploads/avatars/original/${this.user.avatar}`" @click="show" id="icon" alt="">

                <div v-show="usershow" class="wrap" id="menu">
                    <div class="user__menu">
                        <div class="user__icon" @click="goToUser">
                            <img :src="`../../dist/uploads/avatars/original/${this.user.avatar}`" alt="">
                        </div>
                        <p>{{ user.username }}</p>
                        <button @click="goToEdit">Редактировать профиль</button>
                        <button v-show="user.is_verified" @click="goToUpload">Создать</button>
                        <button v-show="user.is_superuser | user.is_moderator" @click="goToAdm">Управление</button>
                        <button @click="goToAbout">О нас</button>
                        <button style="margin-bottom: 20px;" @click="exit()">Выход</button>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>

<style scoped>
@import url(../assets/reset.css);

button {
    cursor: pointer;
}

.header {
    position: sticky;
    z-index: 1000;
    overflow: visible;
    top: 0;
    background: #B1A73F;
    height: 80px;
}

.wrapper__header {
    max-width: 1440px;
    height: 80px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    position: relative;
}

.moder_menu {
    position: relative;
    max-width: 1440px;
    margin-left: 80px;
    margin-right: auto;
}

.moder_head {
    position: absolute;
    top: 40px;
    left: -350px;
    width: 190px;
    height: auto;

    border-radius: 0px 0px 16px 16px;
    background: rgba(239, 237, 217, 1);
    display: flex;
    flex-wrap: wrap;
    align-items: end;
    justify-content: center;
}

.moder-btn {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

    width: 180px;
    height: 39px;
    margin-bottom: 5px;
    border-radius: 16px;
    border: 0;
    padding-left: 10px;
    background: rgba(239, 237, 217, 1);
}

.header__logo {
    font-family: Chewy;
    font-size: 48px;
    font-weight: 400;
    line-height: 64px;
    color: white;
    cursor: default;
    height: 80px;
    width: 190px;
    margin-left: 80px;
    display: flex;
    align-items: center;
    position: relative;
}

.color__white {
    color: white;
}

.color__black {
    color: #474319;
}

.user__icon {
    width: 50px;
    height: 50px;
    margin-right: 80px;
    position: relative;
}

.user__icon img {
    border-radius: 50%;
    max-width: 100%;
    max-height: 100%;
    cursor: pointer;
}

/* style="position: fixed; top:80px; overflow: hidden;  display:block;" */

.wrap {
    position: absolute;
    top: 65px;
    right: 211px;
}

.user__menu {
    /* margin-right: 80px; */
    z-index: 2000;
    position: fixed;
    /* top: 66px; */
    /* right: 0px; */
    /* right: 50vh; */
    /* margin-left: 200px; */
    /* height: 330px; */
    width: 211px;
    /* top: 80px;
    right: 80px; */
    border-radius: 0 0 20px 20px;
    background: rgba(239, 237, 217, 1);
}

.user__menu p {
    font-family: Balsamiq Sans;
    font-size: 20px;
    font-weight: 400;
    line-height: 24px;
    text-align: center;
    margin-bottom: 11px;
    margin-top: 5px;
}

.user__menu .user__icon {
    margin: auto;
    margin-top: 20px;
    height: 51px;
    width: 51px;
    border-radius: 50%;
    border: 2px solid rgba(177, 167, 63, 1)
}

.user__menu button {
    width: 211px;
    height: 40px;
    font-family: Balsamiq Sans;
    font-size: 14px;
    font-weight: 400;
    line-height: 16.8px;
    text-align: center;
    color: rgba(71, 67, 25, 1);
    padding: 0;
    border: 0;
    background-color: inherit;
}


button:hover {
    background: rgba(208, 202, 140, 1);

}

button:active {
    background: rgba(193, 185, 101, 1);

}

.alert {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: center;
    color: rgba(255, 255, 255, 1);
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    z-index: 2000;
    width: 211px;
    height: 29px;
    top: 80px;
    left: 80px;
    gap: 0px;
    border-radius: 0px 0px 16px 16px;
    background: rgba(189, 38, 38, 1);
}

.confirme {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: center;
    color: rgba(255, 255, 255, 1);
    position: absolute;
    z-index: 2000;
    width: 211px;
    height: 29px;
    top: 80px;
    left: 80px;
    gap: 0px;
    border-radius: 0px 0px 16px 16px;
    background: rgba(22, 127, 30, 1);
}

.nav {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    /* width: calc(100% - 190px - 80px - 463px); */
}

.nav p {
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;
    color: #FFFFFF;
    cursor: pointer;
    margin-left: 30px;
}
</style>

<script>
import axios from 'axios';
import Announcement from './Announcement.vue';

export default {
    data() {
        return {
            loading: false,
            showannouncement: false,
            userName: "",
            email: "",
            showmoder: false,
            usershow: false,
            userId: 1,
            userid: {},
            avatar: "",
            is_verified: Boolean,
            countshow: localStorage.showver,
            user: {},
        }
    },
    props: {
    },
    components: {
        Announcement
    },
    mounted() {
        const menu = document.getElementById('menu');
        const icon = document.getElementById('icon');
        document.addEventListener('click', (e) => {
            if (!icon.contains(e.target) & this.usershow) {
                if (!menu.contains(e.target))
                    this.hide()

            }
        });
        if (this.$route.name == 'userview')
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
                        this.userid = response.data

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
                    if (this.user.is_verified & this.$route.name == "homeview" & localStorage.showver.length < 3) {
                        localStorage.showver += 1
                        this.countshow = localStorage.showver
                    }
                    else if (this.user.is_verified & localStorage.showver.length == 2) {
                        localStorage.showver += 1
                        this.countshow = localStorage.showver
                    }
                    // this.email = response.data.email

                }

            })
            .catch(error => {
                if (error.status != null) {
                    if (error.status != 401)
                        this.$router.push({
                            name: 'codeerrorview',
                            query: {
                                ErrorNum: error.status
                            }
                        })
                }
            })
            .finally(() => {
                this.loading = true
            });

    },
    methods: {
        goToUser() {
            this.$router.push({ name: 'userview', params: { id: this.user.id } })
        },
        goToHome() {
            if (this.$route.name != 'homeview')
                this.$router.push({ name: 'homeview' })
            else
                window.location.reload()
        },
        goToSubs() {
            this.$router.push({ name: 'subscriptionsview' })
        },
        goToEdit() {
            this.$router.push({ name: 'editprofileview' })
        },
        goToUpload() {
            this.$router.push({ name: 'uploadimgview' })
        },
        goToAbout() {
            this.$router.push({ name: 'aboutview' })
        },
        goToAdm() {
            this.$router.push({ name: 'adminpanelview' })
        },
        show() {
            this.usershow = !this.usershow
        },
        hide() {
            this.usershow = false
        },
        show_moder() {
            this.showmoder = !this.showmoder
        },
        exit() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `logout`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    window.location.reload()
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

        },
        verefi() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `auth/request-verify-token`),
                withCredentials: true,
                data: {
                    email: this.user.email
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
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
        },
        ShowAnnouncement() {
            this.showannouncement = !this.showannouncement
        },
        ban_user() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.userid.id}/ban`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.userid.is_active = !this.userid.is_active
                    window.location.reload();
                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
        unban_user() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.userid.id}/unban`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.userid.is_active = !this.userid.is_active
                    window.location.reload();
                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
        mod_user() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.userid.id}/moder`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.userid.is_moderator = !this.userid.is_moderator

                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
        unmod_user() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.userid.id}/unmoder`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.userid.is_moderator = !this.userid.is_moderator
                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
        delete_user() {
            axios({
                timeoute: 1000,
                method: 'DELETE',
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.userid.id}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.goToHome()
                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
    },

    watch: {
        countshow(newVal) {
            if (newVal == '11') {

                setTimeout(() => {
                    localStorage.showver += 1
                    this.countshow = localStorage.showver
                }, 3000);
            }
        }
    },

}
</script>