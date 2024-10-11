<template>

    <body>
        <div class="wrapper_login">

            <form>
                <label>
                    Имя пользователя:
                </label>
                <input v-model="Username" type="text" required>

                <label v-if="login">
                    Почта:
                </label>
                <input v-if="login" v-model="e_mail" type="text" required>



                <label>
                    Пароль:
                </label>
                <input v-model="Password" type="password" required>
                <label v-if="login">
                    Повторите пароль:
                </label>
                <input v-if="login" v-model="confirm_password" type="password" required>


                <div v-if="!login" class="wrap">
                    <button class="login" type="button" @click=printinfo2()>
                        Войти
                    </button>
                </div>
                <div class="wrap__line__or" v-if="!login">
                    <div class="line"></div>
                    <p> <span class="or">ИЛИ</span>
                    </p>
                    <div class="line"></div>
                </div>
                <div class="wrap" v-if="login">
                    <button class="sing_in1" type="button" @click=printinfo()>
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
    width: 1000px;
    height: 685px;

    text-align: center;
    justify-content: center;
}

h1 {
    color: #4CAF50;
}

label {
    display: block;
    width: 100%;
    margin-top: 10px;

    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;
    color: #474319;
    padding-left: 53px;
    margin-bottom: 6px;
}


input {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;


    width: 874px;
    height: 40px;
    gap: 0px;
    border-radius: 20px;
    border: 2px 0px 0px 0px;
    opacity: 0px;
    margin-bottom: 12px;

}

button.login {

    font-family: Balsamiq Sans;
    font-size: 48px;
    font-weight: 400;
    line-height: 57.6px;
    text-align: center;


    border-radius: 10px;
    margin-top: 64px;

    border: 4px solid #B1A73F;

    color: #474319;
    cursor: pointer;

    border-radius: 30px;
    width: 180px;
    height: 100px;
}

button:active {
    transform: scale(0.90);
}

button.sing_in1 {

    font-family: Balsamiq Sans;
    font-size: 48px;
    font-weight: 400;
    line-height: 57.6px;
    text-align: center;
    color: #474319;

    margin-top: 58px;
    width: 484px;
    height: 100px;
    gap: 0px;
    border-radius: 30px;
    border: 4px solid #B1A73F;
    opacity: 0px;

}

form {
    margin-top: 30px;
}

button.sing_in2 {

    font-family: Balsamiq Sans;
    font-size: 48px;
    font-weight: 400;
    line-height: 57.6px;
    text-align: center;
    color: #474319;

    margin-top: 44px;
    width: 484px;
    height: 100px;
    gap: 0px;
    border-radius: 30px;
    border: 4px solid #B1A73F;
    opacity: 0px;

}

.wrap__line__or {
    margin-top: 38px;
    /* margin-bottom: 38px; */
    display: flex;
    justify-content: center;
    align-items: center;
}

.or {
    font-family: Balsamiq Sans;
    font-size: 40px;
    font-weight: 400;
    line-height: 48px;
    text-align: center;
    color: #474319;


    margin: 0px 17px 0px 17px;
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
</style>

<script>

export default {
    data() {
        return {
            Username: "",
            Password: "",
            confirm_password: "",
            e_mail: "",
            login: this.login1,
            hiedth: "350px"
        }
    },
    props: {
        login1: Boolean,
    },
    methods: {
        change_show() {

            this.login = !this.login

        },
        printinfo() {
            setTimeout(() => {
                this.$emit('login', {
                    email: this.e_mail,
                    Username: this.Username,
                    Password: this.Password
                })
                this.$emit('show_ch', true)
                this.$emit('authorised1', true)
            }, 200);



        },

        printinfo2() {
            setTimeout(() => {
                this.$emit('show_ch', true)
                this.$emit('authorised1', true)
                this.$emit('login', {
                    Username: this.Username,
                    Password: this.Password

                })
            }, 200);

        }
    },

}


</script>