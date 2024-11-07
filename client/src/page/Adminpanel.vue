<template>

    <div class="page">
        <HeaderAuth />
        <div>
            <div class="menu">
                <div class="tabs-header">

                    <button class="tabs-btn" style="margin-top: 65px;" @click="activeTab = 1"
                        :class="{ active: activeTab === 1 }">Пользователи
                    </button>
                    <button class="tabs-btn" @click="activeTab = 2" :class="{ active: activeTab === 2 }">Теги
                    </button>

                </div>
            </div>
        </div>
        <div class="tabs_body">
            <div class="tabs-body-item" v-show="activeTab === 1">

                <div class="serach_wrap">
                    <label>
                        Пользователь
                    </label>
                    <div class="searchbar">
                        <div class="input">
                            <input v-model="serach_user" id="idSearch" v-on:keyup.enter="get_user()">
                        </div>
                        <div class="searchbar__icon">

                            <img src="../assets/img/svg/searchicon.svg" alt="">
                        </div>
                    </div>
                </div>
                <div class="user_wrap">
                    <div class="user_info" v-show="user.username">
                        <img @click="goToUser" :src="'../../dist/uploads/avatars/original/' + user.avatar" alt="">
                        <div class="user_text">
                            <p>{{ user.username }}</p>
                            <div class="sub">
                                <p>Подписчики {{ user.followers_count }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="btn_wrap">
                    <div style="display: flex; justify-content: space-between; width: calc(100% - 50px);">
                        <button v-if="!user.is_moderator" @click="mod_user()">
                            Повысить
                        </button>
                        <button v-else @click="unmod_user()">
                            Понизить
                        </button>
                        <button @click="delete_user()">
                            Удалить
                        </button>
                    </div>
                    <button v-if="user.is_active" v-on:click="ban_user()">
                        Заблокировать
                    </button>
                    <button v-else v-on:click="unban_user()">
                        Разблокировать
                    </button>
                </div>
            </div>

            <div class="tabs-body-item" v-show="activeTab === 2">
                <div class="user_wrap">
                    <label>Тег</label>
                    <div class="searchbar">
                        <div class="input">
                            <input v-model="serach_tag" id="idSearch">
                        </div>
                        <div id="searchResults"></div>
                        <!-- <div class="searchbar__icon">

                            <img src="../assets/img/svg/searchicon.svg" @click="loadImg" alt="">
                        </div> -->
                    </div>
                </div>
                <div class="btn_wrap">
                    <div style="display: flex; justify-content: space-between; width: calc(100% - 50px);">
                        <button @click="add_tag()">
                            Добавить
                        </button>
                        <button @click="del_tag()">
                            Удалить
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <Bottom />
    </div>

</template>

<style scoped>
button {
    cursor: pointer;
}

.page {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    /* box-sizing: border-box; */
}

.menu {
    position: relative;
    max-width: 1440px;
    margin-left: 80px;
    margin-right: auto;
}

.tabs-header {
    position: absolute;
    top: 0;
    left: 0;
    width: 190px;
    height: 153px;

    border-radius: 0px 0px 16px 16px;
    background: rgba(239, 237, 217, 1);

    display: flex;
    flex-wrap: wrap;
    align-items: end;
    justify-content: center;

}

.tabs-btn {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

    width: 180px;
    height: 40px;
    margin-bottom: 5px;
    border-radius: 16px;
    border: 0;
    background: rgba(239, 237, 217, 1);
}

.tabs-btn.active {

    background: rgba(224, 220, 178, 1);

}

.tabs_body {
    max-width: 583px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    justify-content: center;
}

.tabs-body-item {
    background: rgba(239, 237, 217, 1);

    margin-top: 40px;
    display: flex;
    flex-wrap: wrap;
    /* flex-direction: column; */
    /* align-items: center; */
    justify-content: center;
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;

    border-radius: 50px;
    width: 100%;
}

.serach_wrap {
    margin-top: 40px;
    margin-left: 20px;
    margin-right: 20px;
    width: 100%;
}

.user_wrap {
    margin-top: 30px;
    margin-left: 20px;
    margin-right: 20px;
    width: 100%;
}

.btn_wrap {
    margin-left: 20px;
    margin-right: 20px;
    margin-bottom: 40px;
    /* height: 50px; */
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;

}

.btn_wrap button {
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: center;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1);
    padding: 10px 40px 10px 40px;
    margin-top: 30px;
}

.searchbar {



    /* max-width: 835px; */
    height: 40px;
    margin-left: auto;
    margin-right: auto;
    top: 155px;
    left: 280px;
    gap: 0px;
    border-radius: 20px;
    border: 2px solid #B1A73F;
    opacity: 0px;


    background: #FFFFFF;

    display: flex;
    justify-content: space-between;

}

.searchbar__icon {

    margin-right: 10px;
    display: flex;
    align-items: center;
}

.searchbar .input {

    margin-left: 10px;
    position: relative;
    max-width: 835px;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    padding-right: 5px;
    justify-content: center;
}

.searchbar .input input {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;


    /* position: absolute; */

    width: 100%;
    height: 100%;
    border: 0;
    caret-color: #474319;
    color: #474319;
    outline: 0;
    background: none;
}



.searchbar input::-webkit-input-placeholder {
    color: rgba(71, 67, 25, 0.7);


}

.searchbar input:focus::placeholder {
    color: transparent;
}


.user_info {
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
    max-width: calc(100% - 100px);
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
</style>

<script>

import HeaderAuth from '@/components/HeaderAuth.vue';
import Bottom from '@/components/Bottom.vue'

import axios from 'axios';

export default {
    data() {
        return {
            activeTab: 1,
            serach_user: "",
            serach_tag: "",
            user: {
            },
        }

    },
    components: { HeaderAuth, Bottom },
    mounted() {


        axios({
            timeoute: 1000,
            method: 'get',
            url: (import.meta.env.VITE_BACKEND_URL + `users/current`),
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                if (!response.data.is_moderator) {
                    this.$router.push({
                        name: 'homeview',
                    })
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
    },
    methods:
    {
        get_user() {
            axios({
                timeoute: 1000,
                method: 'get',
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.serach_user}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (response.status == 200) {

                        this.user = response.data
                        console.log(this.user)
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
                });
        },
        ban_user() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.user.id}/ban`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('Забанен')
                    this.user.is_active = !this.user.is_active

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
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.user.id}/unban`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('Разбанен')
                    this.user.is_active = !this.user.is_active
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
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.user.id}/moder`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('moder')
                    this.user.is_moderator = !this.user.is_moderator

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
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.user.id}/unmoder`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('unmoder')
                    this.user.is_moderator = !this.user.is_moderator
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
                url: (import.meta.env.VITE_BACKEND_URL + `users/${this.user.id}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('delete')
                    this.user = {}

                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
        add_tag() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `tags`),
                data: {
                    name: this.serach_tag
                },
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('+тег')
                    this.user = {}

                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
        del_tag() {
            axios({
                timeoute: 1000,
                method: 'delete',
                url: (import.meta.env.VITE_BACKEND_URL + `tags`),
                data: {
                    name: this.serach_tag
                },
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('delete')
                    this.user = {}

                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
    },
}
</script>
