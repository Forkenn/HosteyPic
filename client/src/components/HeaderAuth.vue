<template>




    <header class="header">

        <div class="wrapper__header">
            <div class="header__logo" @click="goToHome">
                <p> <span class="color__white">Hostey</span>
                    <span class="color__black">PIC</span>
                </p>

            </div>
            <div class="user__icon">
                <img src="../assets/img/svg/userIconmain.svg" @click="show" id="icon" alt="">

                <div v-show="usershow" class="wrap" id="menu">
                    <div class="user__menu">
                        <div class="user__icon" @click="goToUser">
                            <img src="../assets/img/svg/userIconmain.svg" alt="">
                        </div>
                        <p>{{ userName }}</p>
                        <button @click="goToEdit">Редактировать профиль</button>
                        <button>О нас</button>
                        <button @click="exit()">Выход</button>
                    </div>
                </div>
            </div>


        </div>
    </header>


</template>

<style scoped>
@import url(../assets/reset.css);

.header {
    position: sticky;
    z-index: 1000;
    overflow: hidden;
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
}



.header__logo {

    font-family: Chewy;
    font-size: 48px;
    font-weight: 400;
    line-height: 64px;
    color: white;

    height: 80px;
    width: 190px;
    margin-left: 80px;
    display: flex;
    align-items: center;
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
    max-width: 100%;
    max-height: 100%;
}

/* style="position: fixed; top:80px; overflow: hidden;  display:block;" */

.wrap {
    position: absolute;
    top: 65px;
    right: 250px;
}

.user__menu {
    /* margin-right: 80px; */
    z-index: 2000;
    position: fixed;
    /* top: 66px; */
    /* right: 0px; */
    /* right: 50vh; */
    /* margin-left: 200px; */
    height: 250px;
    width: 250px;
    /* top: 80px;
    right: 80px; */
    border-radius: 20px;
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
    width: 250px;
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
</style>

<script>

import axios from 'axios';



export default {
    data() {
        return {
            userName: "",
            usershow: false,
            userId: 1,
        }
    },
    props: {
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
            url: (`http://localhost/api/users/current`),
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
                    this.userName = response.data.username
                    this.userId = response.data.id
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
            this.$router.push({ name: 'userview', params: { id: this.userId } })
        },
        goToHome() {
            this.$router.push({ name: 'homeview' })
        },
        goToEdit() {
            this.$router.push({ name: 'editprofileview' })
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
                url: (`http://localhost/api/logout`),
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

        }
    },

}
</script>