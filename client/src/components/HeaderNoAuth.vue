<template>




    <header class="header">
        <div class="wrapper__header">
            <div class="header__logo">
                <p> <span class="color__white">Hostey</span>
                    <span class="color__black">PIC</span>
                </p>

            </div>
            <div class="nav">
                <p @click="goToHome">Главная</p>
                <p>Подписки</p>
            </div>
            <div class="wrap_login">
                <button class="login" v-on:click="show_login()">
                    Вход
                </button>
                <button class="sing_in" v-on:click="show_registration()">
                    Регистрация
                </button>
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
    cursor: default;
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

.wrap_login {
    height: 80px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
}

.login {
    width: 111px;
    height: 46px;
    margin-right: 40px;
    gap: 0px;
    border-radius: 30px 30px 30px 30px;
    border-width: 0px;

    padding: 0px 9px 2px 11px;

    display: flex;
    align-items: center;
    justify-content: center;

    color: #474319;

    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;


}

button.login:active {
    transform: scale(0.90);
}

button.sing_in:active {
    transform: scale(0.90);
}

.sing_in {
    width: 222px;
    height: 46px;
    margin-right: 80px;
    gap: 0px;
    border-radius: 30px 30px 30px 30px;
    border-width: 0px;
    padding: 0px 9px 2px 11px;

    color: #474319;

    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;


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

export default {
    data() {
        return {

        }
    },
    props: {
    },
    methods: {
        show_login() {
            this.$emit('show_ch', false)
            this.$emit('login', false)
        },
        show_registration() {
            this.$emit('show_ch', false)
            this.$emit('login', true)
        },
        goToHome() {
            this.$router.push({ name: 'homeview' })
        },
    }
}
</script>