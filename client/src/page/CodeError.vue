<template>
    <div class="page">
        <header class="header">
            <div class="wrapper__header">
                <div class="header__logo" @click="goToHome">
                    <p> <span class="color__white">Hostey</span>
                        <span class="color__black">PIC</span>
                    </p>
                </div>
            </div>
        </header>
        <div v-if="this.Error == 50" class="text_ban">

            <p>У-у-упс вы были забанены</p>
            <p>
                <span class="lower">(не без причины)</span>
            </p>
        </div>

        <div v-if="this.Error == 404" class="text_404">
            <p>404</p>
            <img style="margin-left: 34px;" src="../assets/img/svg/404svg.svg" alt="">
            <p style="display: flex;"><span class="lower_text">Страница не найдена</span></p>
        </div>
        <div v-if="this.Error == 500" class="text_404">
            <p>500</p>
            <img style="margin-left: 34px;" src="../assets/img/svg/500.svg" alt="">
            <p style="display: flex;"><span class="lower_text">Внутренняя ошибка сервера... <br> Администраторы
                    уведомлены!</span></p>
        </div>
        <Bottom />
    </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');
@import url(../assets/reset.css);

.page {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

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
    margin-left: auto;
    margin-right: auto;
    display: flex;
    align-items: center;
}

.color__white {
    color: white;


}

.color__black {
    color: #474319;
}

.text_ban {
    height: 100%;
    font-family: Balsamiq Sans;
    font-size: 96px;
    font-weight: 400;
    line-height: 115.2px;
    /* text-align: center; */
    margin: auto;
    margin-top: 325px;
    display: flex;
    flex-direction: column;
    position: relative;
    align-items: center;
}

.lower {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: right;
    position: absolute;
    right: 0;
    top: 95px;

}

.text_404 {
    font-family: Balsamiq Sans;
    font-size: 256px;
    font-weight: 400;
    line-height: 307.2px;
    text-align: center;
    color: rgba(71, 67, 25, 1);
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: auto;
    max-width: 877px;

}

.lower_text {
    font-family: Balsamiq Sans;
    font-size: 64px;
    font-weight: 400;
    line-height: 76.8px;
    text-align: center;
}
</style>

<script>
import Bottom from "../components/Bottom.vue"
import axios from "axios";

export default {
    components: { Bottom },
    data() {
        return {
            Error: 404,
        }

    },
    mounted() {
        if (this.$route.query.ErrorNum)
            this.Error = this.$route.query.ErrorNum
    },
    methods: {
        goToHome() {
            this.$router.push({ name: 'homeview' })
        },
    }
}
</script>