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
                        <button @click="goToUpload">Создать</button>
                        <button v-show="user.is_moderator" @click="goToAdm">Управление</button>
                        <button>О нас</button>
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
            usershow: false,
            userId: 1,
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
                    this.loading = true
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
            });

    },
    methods: {
        goToUser() {
            this.$router.push({ name: 'userview', params: { id: this.user.id } })
        },
        goToHome() {
            this.$router.push({ name: 'homeview' })
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
        goToAdm() {
            this.$router.push({ name: 'adminpanelview' })
        },
        show() {
            this.usershow = !this.usershow
        },
        hide() {
            this.usershow = false
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
                    console.log(response)
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