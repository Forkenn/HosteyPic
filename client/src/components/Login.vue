<template>

    <body>
        <div class="wrapper_login">

            <form>
                <label v-if="login">
                    Имя пользователя:
                </label>
                <input v-if="login" maxlength="27" v-model="Username" type="text" required>
                <div style="position: relative;">
                    <label class="error_inp" v-if="login & error.includes('REGISTER_USERNAME_ALREADY_TAKEN')">
                        Никнейм уже занят
                    </label>
                    <label class="error_inp" v-if="login & error.includes('username')">
                        Неверный формат ника
                    </label>
                </div>
                <label>
                    Почта:
                </label>
                <input v-model="e_mail" type="text" required>
                <div style="position: relative;">
                    <label class="error_inp" v-if="login & error.includes('REGISTER_USER_ALREADY_EXISTS')">
                        Почта уже занята
                    </label>
                    <label class="error_inp" v-if="login & error.includes('email')">
                        Неверный формат почты
                    </label>
                </div>


                <label>
                    Пароль:
                </label>
                <input v-model="Password" type="password" required>
                <div style="position: relative;">
                    <label class="error_inp" v-if="login & !valid_pas">
                        Пароль слишком легкий
                    </label>
                </div>

                <label v-if="login">
                    Повторите пароль
                </label>

                <input id="conf_pas" v-show="login" v-model="confirm_password" type="password" required>
                <div style="position: relative;">
                    <label class="error_inp" v-if="login & !conf_err">
                        Пароли не совпадают
                    </label>
                </div>
                <p class="forgot" v-if="!login">
                    <a href="http://localhost:5173/reset-password">Забыли пароль?</a>
                </p>


                <label class="error_log" v-if="!login & !login_err">
                    Неверная почта или пароль
                </label>



                <div v-if="!login" class="wrap">
                    <button class="login" type="button" @click=fun_login()>
                        Войти
                    </button>
                </div>
                <div class="wrap__line__or" v-if="!login">
                    <div class="line"></div>
                    <p> <span class="or">или</span>
                    </p>
                    <div class="line"></div>
                </div>
                <div class="wrap" v-if="login">
                    <button class="sing_in1" type="button" @click=sing_in()>
                        Зарегистрироваться
                    </button>
                </div>
                <div v-else class="wrap">
                    <button class="sing_in2" type="button" @click=change_show()>
                        Зарегистрироваться
                    </button>
                </div>

            </form>

        </div>
    </body>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');


body {


    font-family: Chewy;
    font-size: 32px;
    font-weight: 400;
    line-height: 41.81px;
    text-align: left;


    display: flex;
    align-items: center;
    justify-content: center;
    background: #f3f3f3;
    flex-direction: column;
    margin: 0;

}

.wrapper_login {
    position: fixed;
    left: 50%;

    top: 50%;
    transform: translate(-50%, -50%);


    z-index: 1600;
    background-color: #EFEDD9;
    border-radius: 50px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
    padding: 10px 20px;
    transition: transform 0.2s;
    width: 500px;
    height: 557px;

    text-align: center;
    justify-content: center;
}

h1 {
    color: #4CAF50;
}

label {
    display: block;
    width: 100%;
    margin-top: 27px;

    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;


    color: #474319;
    margin-left: 10px;
    margin-bottom: 6px;
}


input {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;

    padding-left: 10px;
    padding-right: 10px;
    outline: none;
    width: 461px;
    height: 40px;
    gap: 0px;
    border-radius: 20px;
    border: 2px solid rgba(177, 167, 63, 1)
        /* margin-bottom: 12px; */

}

button.login {

    font-family: Balsamiq Sans;
    font-size: 36px;
    font-weight: 400;
    line-height: 43.2px;
    text-align: center;

    text-align: center;


    border-radius: 10px;
    margin-top: 20px;

    border: 4px solid #B1A73F;

    color: #474319;
    cursor: pointer;

    border-radius: 30px;
    width: 180px;
    height: 58px;
}

button:active {
    transform: scale(0.90);
}

button.sing_in1 {

    font-family: Balsamiq Sans;
    font-size: 36px;
    font-weight: 400;
    line-height: 43.2px;
    text-align: center;

    color: #474319;

    margin-top: 39px;
    width: 424px;
    height: 58px;
    border-radius: 30px;
    border: 4px solid #B1A73F;
    opacity: 0px;

}

form {
    margin-top: 30px;
}

button.sing_in2 {

    font-family: Balsamiq Sans;
    font-size: 36px;
    font-weight: 400;
    line-height: 43.2px;
    text-align: center;

    color: #474319;

    margin-top: 0px;
    width: 424px;
    height: 58px;
    gap: 0px;
    border-radius: 30px;
    border: 4px solid #B1A73F;
    opacity: 0px;

}

.wrap__line__or {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 19px 0px 19px 0px;
}

.or {
    font-family: Balsamiq Sans;
    font-size: 40px;
    font-weight: 400;
    line-height: 48px;
    text-align: center;


    color: #474319;


    margin: 0px 30px 0px 30px;
}

.line {
    width: 400px;
    height: 0px;
    text-align: center;
    gap: 0px;
    border: 2px solid #B1A73F;
    opacity: 0px;

}

.wrap {
    /* margin-top: 38px; */
    display: flex;
    justify-content: center;
    align-items: center;
}

.forgot {
    font-family: Balsamiq Sans;
    font-size: 14px;
    font-weight: 400;
    line-height: 16.8px;
    text-align: right;


    margin-top: 10px;
}

a {
    color: rgba(84, 51, 217, 1);

    /* text-decoration: none */
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

.error_log {
    font-family: Balsamiq Sans;
    font-size: 20px;
    font-weight: 400;
    line-height: 24px;
    text-align: center;
    color: rgba(189, 38, 38, 1);
    margin: 0;
    margin-top: 10px;

}
</style>

<script>
import axios from "axios";
export default {
    data() {
        return {
            Username: "",
            Password: "",
            valid_pas: true,
            confirm_password: "",
            e_mail: "",
            conf_err: true,
            login: this.login1,
            hiedth: "350px",
            error: [],
            login_err: true,
        }
    },
    mounted() {
        const conf_pas = document.getElementById('conf_pas')
        conf_pas.addEventListener('blur', () => {
            if (this.confirm_password != this.Password)
                this.conf_err = false
            else
                this.conf_err = true

        })
    },
    props: {
        login1: Boolean,
    },
    watch: {
        Password: function (newval) {
            let reg = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*#?&]{6,}$/
            if (newval.length > 0)
                this.valid_pas = reg.test(newval)
        },
        confirm_password: function (newval) {

            if (newval == this.Password)
                this.conf_err = true
        }
    },
    methods: {
        change_show() {

            this.login = !this.login

        },
        sing_in() {
            axios.post(import.meta.env.VITE_BACKEND_URL + 'auth/register', {
                username: this.Username,
                email: this.e_mail,
                password: this.Password
            })
                .then(response => {
                    console.log(response);

                    localStorage.showver = 1
                    this.fun_login()
                    // window.location.reload()
                })
                .catch(error => {
                    // this.$router.push({
                    //     name: 'codeerrorview',
                    //     query: {
                    //         ErrorNum: error.status
                    //     }
                    // })
                    this.error = error.response.data.detail
                    console.log(error.status);
                    if (error.status == 422)
                        error.response.data.detail.forEach(element => {
                            this.error.push(element.loc[1])
                        });
                    else {
                        this.error = error.response.data.detail
                    }
                    console.log(error.response.data.detail);
                });

        },
        fun_login() {
            // console.log(this.Username, this.Password)
            axios({
                timeoute: 1000,
                method: 'post',
                url: import.meta.env.VITE_BACKEND_URL + 'login',
                data: {
                    username: this.e_mail,
                    password: this.Password
                },
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
                .then(response => {
                    this.$emit('show_ch', true)
                    this.$emit('authorised1', true)
                    console.log(response);
                    window.location.reload()
                })
                .catch(error => {
                    console.log(error)
                    if (error.status != null) {
                        if (error.status == 400)
                            this.login_err = false
                        console.log(error.body.detail)
                        // this.$router.push({
                        //     name: 'codeerrorview',
                        //     query: {
                        //         ErrorNum: error.status
                        //     }
                        // })
                    }
                    console.log(error.message);
                    console.log(error.toJSON())
                });
        }
    },

}


</script>