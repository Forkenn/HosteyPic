<template>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>main screen</title>

    </head>

    <body>
        <div class="page">
            <header class="header">
                <div class="wrapper__header">
                    <div class="header__logo" @click="goToHome">
                        <p> <span class="color__white">Hostey</span>
                            <span class="color__black">PIC</span>
                        </p>
                    </div>

                    <div class="user__icon">
                        <img src="../assets/img/svg/userIconmain.svg" alt="">
                    </div>
                </div>
            </header>
            <div class="userinfo__wrap">
                <div class="userinfo">
                    <div class="userIcon">
                        <img src="../assets/img/svg/userIconmain.svg" alt="">
                    </div>
                    <div class="userName">
                        <p>{{ userName }}</p>
                    </div>
                    <div class="subscribers">
                        <span class="countsubscribers">
                            <p>{{ countSubscribers }} подписчики</p>
                        </span>

                    </div>
                    <div class="socialmedia">
                        <div class="github">
                            <img src="../assets/img/svg/GitHub.svg" alt="">
                        </div>
                        <div class="gitlab">
                            <img src="../assets/img/svg/GitLab.svg" alt="">
                        </div>
                        <div class="rutube">
                            <img src="../assets/img/svg/RuTube.svg" alt="">
                        </div>
                        <div class="vk">
                            <img src="../assets/img/svg/VK.svg" alt="">
                        </div>
                        <div class="ok">
                            <img src="../assets/img/svg/OK.svg" alt="">
                        </div>
                    </div>
                </div>
            </div>
            <div class="tabs__wrap">
                <div class="create-line"></div>
                <div class="tabs">

                    <div class="tabs-header">

                        <button class="tabs-btn" @click="activeTab = 1, loadImg()"
                            :class="{ active: activeTab === 1 }">Созданные
                        </button>
                        <button class="tabs-btn" @click="activeTab = 2, loadImg()"
                            :class="{ active: activeTab === 2 }">Понравившееся
                        </button>
                    </div>
                    <div class="tabs-body">
                        <div class="tabs-body-item" v-show="activeTab === 1">
                            <p v-if="countImg == 0" style="margin-top: 75px;">Здесь пока ничего нет... Тогда
                                <button class="create" @click="loadImg(6)">
                                    Создай
                                </button>

                                что-нибудь!
                            </p>
                            <button v-else class="create">
                                Создать
                            </button>
                            <Searchimg :res="result" />

                        </div>
                        <div class="tabs-body-item" v-show="activeTab === 2">
                            <Searchimg :res="result" />
                        </div>
                    </div>
                </div>
            </div>
            <Bottom />
        </div>


    </body>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');
@import '../assets/reset.css';

/* chewy-regular - latin */
@font-face {
    font-display: swap;
    /* Check https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display for other options. */
    font-family: 'Chewy';
    font-style: normal;
    font-weight: 400;
    src: url('../assets/fonts/chewy-v18-latin-regular.woff2') format('woff2');
    /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
}

html {
    box-sizing: border-box;
    caret-color: transparent;
}

*,
*::before,
*::after {
    box-sizing: inherit;
}

.page {
    overflow: hidden;
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
}

.user__icon img {
    max-width: 100%;
    max-height: 100%;
}


.userinfo {

    width: 418px;
    height: 433px;
    margin-top: 60px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
}

.userIcon {
    margin-left: auto;
    margin-right: auto;
}

.userName {
    margin-left: auto;
    margin-right: auto;
    margin-top: 9px;
    font-family: Balsamiq Sans;
    font-size: 64px;
    font-weight: 400;
    line-height: 76.8px;
}

.subscribers {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;


    margin-left: auto;
    margin-right: auto;
    margin-top: 9px;
}

.socialmedia {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-left: auto;
    margin-right: auto;
    margin-top: 40px;
}

.github {
    margin-right: 14px;
}

.gitlab {
    margin-right: 14px;
}

.rutube {
    margin-right: 14px;
}

.vk {
    margin-right: 14px;
}

.ok {
    margin-right: 14px;
}


.tabs__wrap {
    position: sticky;
    margin-top: 47px;

    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
}


.tabs {

    max-width: 1440px;
    margin-left: auto;
    margin-right: auto;
}

.tabs-header {
    position: relative;
    display: block;
    margin-left: 80px;
}

button {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;
    padding: 0;
}

.tabs-btn {


    height: 50px;
    width: 280px;
    background-color: inherit;
    display: inline-block;
    color: rgba(53, 50, 50, 0.5);
    border-radius: 25px 25px 0 0;
    border: 4px solid rgba(177, 167, 63, 0.5)
}



.tabs-btn.active {


    color: rgba(53, 50, 50, 1);
    border: 4px solid rgba(177, 167, 63, 1);
    border-bottom-color: rgb(255, 255, 255);
    /* border-bottom-width: 10px; */
    z-index: 10;
}

.create-line {
    position: absolute;
    top: 46px;
    width: 100%;
    border: 2px solid rgba(177, 167, 63, 1)
}


.tabs-body-item {
    margin-top: 34px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;

    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;


}

.create {
    width: 150px;
    height: 50px;

    margin-left: auto;
    margin-right: auto;
    margin-bottom: 20px;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1)
}
</style>

<script>
import Bottom from "../components/Bottom.vue"
import Searchimg from "../components/Searchimg.vue";

const data = ['searchicon.svg', 'userIcon.svg', 'logo.svg']

export default {
    components: { Bottom, Searchimg },
    data() {
        return {
            activeTab: 1,
            userName: "Пользователь",
            countSubscribers: 0,
            result: [],
            countImg: 0,
        }

    },
    mounted() {
        this.loadImg(this.countImg);
    },
    methods: {
        goToHome() {
            this.$router.push({ name: 'homeview' })
        },


        loadImg(tagImg) {
            this.result = []

            if (this.activeTab == 1) {
                if (tagImg)
                    this.countImg = tagImg
                tagImg = this.countImg
            }
            else {
                tagImg = 10
            }

            for (let index = 0; index < tagImg; index++) {

                this.srcimg = data[index % 3],
                    this.result.push({
                        src1: this.srcimg,
                        tag: this.tag
                    })
            }
        },
    }
}
</script>