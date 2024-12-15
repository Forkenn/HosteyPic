<template>
    <div class="page">
        <HeaderAuth />
        <div>
            <div class="menu">
                <div class="tabs-header">
                    <button v-show="user_cur.is_superuser" class="tabs-btn" style="margin-top: 65px;"
                        @click="activeTab = 1" :class="{ active: activeTab === 1 }">Пользователи
                    </button>
                    <button v-show="user_cur.is_superuser" class="tabs-btn" @click="activeTab = 2"
                        :class="{ active: activeTab === 2 }">Теги
                    </button>
                    <button class="tabs-btn" @click="activeTab = 3" :class="{ active: activeTab === 3 }">Жалобы
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
                            <input v-model="serach_user" v-on:keyup.enter="get_user()">
                        </div>
                        <div class="searchbar__icon">
                            <img src="../assets/img/svg/searchicon.svg" @click="get_user()" alt="">
                        </div>
                    </div>
                </div>
                <div class="user_wrap">
                    <div class="user_info" v-show="user.username">
                        <img v-if="user.is_active" @click="goToUser" :src="'../../dist/uploads/avatars/original/' + user.avatar" alt="">
                        <img v-else @click="goToUser" :src="'../../dist/uploads/avatars/original/' + user.avatar" style="border: 4px solid rgb(255, 0, 0)" alt="">
                        <div class="user_text">
                            <p>{{ user.username }}</p>
                            <div class="sub">
                                <p>Подписчики {{ user.followers_count }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="btn_wrap">
                    <div class="btn_user">
                        <button v-if="!user.is_moderator" @click="mod_user()">
                            Повысить
                        </button>
                        <button v-else @click="unmod_user()">
                            Понизить
                        </button>
                    </div>
                    <div class="btn_user">
                        <button @click="delete_user()">
                            Удалить
                        </button>
                    </div>
                    <div class="btn_user">
                        <button v-if="user.is_active" v-on:click="ban_user()">
                            Заблокировать
                        </button>
                        <button v-else v-on:click="unban_user()">
                            Разблокировать
                        </button>
                    </div>
                </div>
            </div>
            <div class="tabs-body-item" v-show="activeTab === 2">
                <div class="user_wrap">
                    <label>Тег</label>
                    <div class="searchbar">
                        <div class="input">
                            <input v-model="serach_tag" id="idSearch">
                        </div>
                        <!-- <div class="searchbar__icon">
                            <img src="../assets/img/svg/searchicon.svg" @click="loadImg" alt="">
                        </div> -->
                    </div>
                    <div v-show="serach_tag.length > 0" style="position: relative; border-radius: 25px; margin-top: 10px; border: 4px solid rgb(5, 0, 49); overflow: hidden;">
                        <div id="searchResults" class="tagul">
                            <ul class="tagli" style="color: black;">
                                <li v-for="el in tags.items">
                                    {{ el.name }}</li>
                            </ul>
                        </div>
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
            <div class="tabs-body-item" style="background-color: white; max-width: 713px;" v-show="activeTab === 3">
                <div class="completed" v-show="report.completed">
                    Жалоб нет! Все просто умнички!
                </div>
                <div v-show="!report.completed" v-for="(item, index ) in reports" :key="item.id">
                    <div className="report_item" v-for="value in item.items" :key="value.id">
                        <div class="close">
                            <img @click="delete_report(index, value.id)" src="../assets/img/svg/X_dark.svg" alt="">
                        </div>
                        <div class="report_info">
                            <p>
                                <a target="_blank" :href='"../" + "user/" + value.user_id'>
                                    {{ value.report_author.username }}
                                </a>
                                <br>
                                Пост:
                                <a target="_blank" :href='"../" + "post/" + value.post_id'>
                                    {{ link + "post/" + value.post_id }}
                                </a>
                            </p>
                        </div>
                        <div class="report_body">
                            <p>{{ value.body }}</p>
                        </div>
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

a {
    /* text-decoration: none; */
    color: rgba(71, 67, 25, 1);

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
    position: fixed;
    top: 80px;
    left: 80px;
    width: 190px;
    height: 197px;

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
    padding-left: 10px;
    background: rgba(239, 237, 217, 1);
}

.tabs-btn.active {

    background: rgba(224, 220, 178, 1);

}

.tabs_body {
    margin: auto;
    height: 100%;
}

.tabs-body-item {
    background: rgba(239, 237, 217, 1);
    max-width: 583px;
    margin-top: 40px;
    display: flex;
    flex-wrap: wrap;
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;
    justify-content: center;
    border-radius: 50px;
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

.btn_user {
    width: 100%;
    display: flex;
    justify-content: center;
}

.btn_user button {
    width: 263px;
}

.btn_wrap button {
    margin-left: auto;
    margin-right: auto;
    /* width: 263px; */
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

button {
    background-color: white;
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

.tagul {
    /* position: absolute; */
    padding: 20px;
    width: 100%;
    height: auto;
    max-height: 200px;
    overflow: scroll;
    scroll-margin: 20px;
    /* background-color: black; */
}

.hide {
    display: none;
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

.report_wrap {

    overflow-y: scroll;
    display: flex;
}

.report_item {
    position: relative;
    width: 574px;
    flex-grow: 1;
    height: 400px;
    border-radius: 50px;
    display: flex;
    flex-wrap: wrap;
    background: rgba(239, 237, 217, 1);
    margin-bottom: 30px;
    justify-content: flex-start;
    color: rgba(71, 67, 25, 1);
}

.report_info {
    margin-top: 40px;
    margin-left: 30px;
    max-height: 128px;

}

.close {
    position: absolute;
    right: 20px;
    top: 20px;
}

.report_info p {
    max-width: 100%;
}

.report_body {
    margin: 20px 30px 20px 30px;
    width: 100%;
    height: calc(100% - 140px);
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;
    overflow-wrap: break-word;
    overflow-y: auto;
}

.completed {
    width: 713px;
    /* height: 58px; */
    height: 100%;
    margin-top: auto;
    margin-bottom: auto;
    font-family: Balsamiq Sans;
    font-size: 48px;
    font-weight: 400;
    line-height: 57.6px;
    text-align: left;
    color: rgba(71, 67, 25, 1);
}
</style>

<script>
import HeaderAuth from '@/components/HeaderAuth.vue';
import Bottom from '@/components/Bottom.vue'

import axios from 'axios';

export default {
    data() {
        return {
            tags: "",
            link: import.meta.env.VITE_FRONTEND_URL,
            reports: [],
            activeTab: 1,
            serach_user: "",
            serach_tag: "",
            report: {
                page: 1,
                loadstop: true,
                completed: false,
            },
            user: {
            },
            user_cur: {},
        }

    },
    components: { HeaderAuth, Bottom },
    mounted() {
        window.addEventListener('scroll', () => {
            const documentReact = document.documentElement.getBoundingClientRect();
            if (documentReact.bottom < document.documentElement.clientHeight + 300)
                this.loadreport()
        });


        document.querySelector('#idSearch').oninput = function () {
            let val = this.value.trim();
            let itemli = document.querySelectorAll('.tagli li');
            if (val != '') {
                itemli.forEach(function (elem) {
                    if (elem.innerText.search(val) == -1) {
                        elem.classList.add('hide');
                    }
                    else {
                        elem.classList.remove('hide');
                    }
                });
            }
            else {
                itemli.forEach(function (elem) {
                    elem.classList.remove('hide');
                });
            }
        }


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
                else {
                    this.user_cur = response.data
                    if (!this.user_cur.is_superuser) {
                        this.activeTab = 3
                    }
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
            url: (import.meta.env.VITE_BACKEND_URL + `tags`),
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.tags = response.data

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
            url: (import.meta.env.VITE_BACKEND_URL + `reports?start=0&end=5`),
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.reports.push(response.data)
                if (response.data.count == 0) {
                    this.report.completed = true
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


            if (/^[+-]?\d+(\.\d+)?$/.test(this.serach_user)) {
                if (this.serach_user != this.user_cur.id)
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
                            }

                        })
                        .catch(error => {
                            if (error.status != null) {

                            }
                        });
            }
            else {
                if (this.serach_user != this.user_cur.username)
                    axios({
                        timeoute: 1000,
                        method: 'get',
                        url: (import.meta.env.VITE_BACKEND_URL + `users/search/${this.serach_user}`),
                        withCredentials: true,
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                        .then(response => {
                            if (response.status == 200) {

                                this.user = response.data
                            }

                        })
                        .catch(error => {
                            if (error.status != null) {

                            }
                        });
            }
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
                    window.location.reload();
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
                    name: this.serach_tag.toLowerCase()
                },
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.tags.items.push({ name: this.serach_tag.toLowerCase() })

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
                    this.user = {}

                })
                .catch(error => {
                    if (error.status != null) {
                        console.log(error)
                    }
                });
        },
        loadreport() {

            if (this.report.loadstop)

                axios({
                    timeoute: 1000,
                    method: 'get',
                    url: (import.meta.env.VITE_BACKEND_URL + `reports?start=${this.report.page * 5}&end=${(this.report.page + 1) * 5}`),
                    withCredentials: true,
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(response => {

                        this.reports.push(response.data)
                        this.report.page += 1
                        if (response.data.count != 5)
                            this.report.loadstop = false


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
        delete_report(item, id) {
            let count = 0
            this.reports[item].items.forEach(elem => {

                if (elem.id == id) {
                    this.reports[item].items.splice(count, 1)
                }

                count++
            });

            axios({
                timeoute: 1000,
                method: 'delete',
                url: (import.meta.env.VITE_BACKEND_URL + `reports?report_id=${id}`),
                withCredentials: true,
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
            if (this.reports[item].items.length == 0) {

                this.loadreport()
            }
        },
        goToUser() {
            this.$router.push({ name: 'userview', params: { id: this.user.id } })
        },
    },
}
</script>
