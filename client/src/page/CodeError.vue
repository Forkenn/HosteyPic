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
        <div class="text">

            <p v-if="!this.Error">У-у-упс вы были забанены</p>
            <p v-if="!this.Error">
                <span class="lower">(не без причины)</span>
            </p>
            <p v-if="this.Error">{{ this.Error }}</p>
        </div>
        <Bottom />
    </div>
</template>

<style>
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

.text {
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
</style>

<script>
import Bottom from "../components/Bottom.vue"
export default {
    components: { Bottom },
    data() {
        return {
            Error: this.$route.query.ErrorNum,
        }

    },
    methods: {
        goToHome() {
            this.$router.push({ name: 'homeview' })
        },
    }
}
</script>