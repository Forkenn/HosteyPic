<template>
    <div class="page">

        <HeaderNoAuth />
        <Announcement v-show="showannouncement" @showannouncement=ShowAnnouncement :email="this.email" :edit="true" />
        <div class="wrap_pass">
            <p>Восстановление пароля</p>
            <div class="wrap_newpas" v-show="this.$route.query.token">
                <label>Новый пароль</label>
                <input v-model="password" type="password">
                <div style="position: relative; width: 100%;">
                    <label class="error_inp" v-if="!valid_pas">
                        Пароль слишком легкий
                    </label>
                </div>
            </div>
            <div class="wrap_confpas" v-show="this.$route.query.token">
                <label>Подтвердите пароль</label>
                <input id="conf_pas" v-model="confirm_password" type="password">
                <div style="position: relative; width: 100%;">
                    <label class="error_inp" v-if="!conf_err">
                        Пароли не совпадают
                    </label>
                </div>
            </div>
            <button v-if="this.$route.query.token" @click="reset_pas">Отправить запрос</button>

            <div class="wrap_newpas" v-show="!this.$route.query.token">
                <label>Почта</label>
                <input v-model="email" type="text">

            </div>
            <button v-if="!this.$route.query.token" @click="forgot_pas()">Запрос на почту</button>
        </div>


        <Bottom />
    </div>
</template>

<style scoped>
.page {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.wrap_pass {
    max-width: 540px;
    border-radius: 50px;
    display: flex;
    flex-wrap: wrap;

    /* justify-content: center; */
    background: rgba(239, 237, 217, 1);
    margin: auto;

}


.wrap_newpas {
    width: 100%;
    margin: 5px 40px 0 40px;
    max-width: 460px;
    display: flex;
    flex-wrap: wrap;
}

.wrap_confpas {
    width: 100%;
    margin: 27px 40px 0 40px;
    max-width: 460px;
    display: flex;
    flex-wrap: wrap;
}

p {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;
    color: rgba(71, 67, 25, 1);
    margin: 40px 0 0 50px;
}

label {
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;
    color: rgba(71, 67, 25, 1);
    margin-left: 10px;
}

input {
    width: 100%;
    height: 40px;
    padding: 10px 0 10px 20px;
    border-radius: 20px;
    border: 2px solid rgba(177, 167, 63, 1);
    outline: none;

    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;
    color: rgba(71, 67, 25, 1);


}

button {
    cursor: pointer;
    margin: 42px 94px 40px 95px;
    width: 351px;
    height: 58px;

    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1);

    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;
    color: rgba(71, 67, 25, 1);
}

.error_inp {
    position: absolute;
    top: 5px;
    left: 0;
    margin: 0;
    margin-left: 10px;
    font-family: Balsamiq Sans;
    font-size: 14px;
    font-weight: 400;
    line-height: 16.8px;
    text-align: left;
    color: rgba(189, 38, 38, 1);

}
</style>

<script>

import axios from 'axios';
import HeaderNoAuth from '@/components/HeaderNoAuth.vue';
import Bottom from '@/components/Bottom.vue'
import Announcement from '@/components/Announcement.vue';

export default {
    data() {
        return {
            showannouncement: false,
            password: "",
            email: "",
            valid_pas: true,
            confirm_password: "",
            conf_err: true,
        }

    },
    components: { HeaderNoAuth, Bottom, Announcement },
    watch: {
        password: function (newval) {
            let reg = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*#?&]{6,}$/
            if (newval.length > 0)
                this.valid_pas = reg.test(newval)
        },
        confirm_password: function (newval) {

            if (newval == this.Password)
                this.conf_err = true
        }
    },
    mounted() {

        if (!this.$route.query.token)
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
                        this.$router.push({
                            name: 'homeview',
                        })
                    }
                    // console.log(response);
                })
                .catch(error => {
                    // console.log(error.message);
                });

        const conf_pas = document.getElementById('conf_pas')
        conf_pas.addEventListener('blur', () => {
            if (this.confirm_password != this.password)
                this.conf_err = false
            else
                this.conf_err = true
        })
    },
    methods: {
        ShowAnnouncement() {
            this.showannouncement = !this.showannouncement
        },
        forgot_pas() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `auth/forgot-password`),
                withCredentials: true,
                data: {
                    email: this.email
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.ShowAnnouncement()
                    setTimeout(() => {
                        this.$router.push({
                            name: 'homeview',
                        })
                    }, 5000);

                })
                .catch(error => {
                    console.log(error.message)
                });
        },
        reset_pas() {
            if (this.conf_err & this.valid_pas)
                axios({
                    timeoute: 1000,
                    method: 'post',
                    url: (import.meta.env.VITE_BACKEND_URL + `auth/reset-password`),
                    withCredentials: true,
                    data: {
                        token: this.$route.query.token,
                        password: this.password
                    },
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(response => {
                        setTimeout(() => {
                            this.$router.push({
                                name: 'homeview',
                            })
                        }, 5000);

                    })
                    .catch(error => {
                        console.log(error.message)
                    });
        }
    }
}

</script>
