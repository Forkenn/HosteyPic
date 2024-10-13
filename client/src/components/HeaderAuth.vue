<template>




    <header class="header">
        <div class="wrapper__header">
            <div class="header__logo" @click="goToHome">
                <p> <span class="color__white">Hostey</span>
                    <span class="color__black">PIC</span>
                </p>

            </div>
            <div class="user__icon" v-on:click="goToUser">
                <img src="../assets/img/svg/userIconmain.svg" alt="">
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
}

.user__icon img {
    max-width: 100%;
    max-height: 100%;
}
</style>

<script>

export default {
    data() {
        return {
            userId: 0,
        }
    },
    props: {
    },
    methods: {
        goToUser() {
            this.$router.push({ name: 'userview', params: { id: this.userId } })
        },
        goToHome() {
            this.$router.push({ name: 'homeview' })
        },
    }

}
</script>