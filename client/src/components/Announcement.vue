<template>
    <div @click="hide()" class="gray" v-if="!showannouncement">
        <div class="wrap">
            <div class="title">
                <p>{{ title }}</p>
            </div>
            <div class="text">
                <p>На почту {{ email }}
                    {{ text }}</p>
            </div>
            <button>OK</button>
        </div>
    </div>
</template>

<style scoped>
.gray {
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1500;
}

.wrap {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 500px;
    max-height: 500px;
    border-radius: 50px;
    transform: translate(-50%, -50%);
    background: #EFEDD9;

}

.title {
    margin-top: 40px;
    margin-left: 30px;
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

}

.text {
    width: 440px;
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: justify;
    color: rgba(71, 67, 25, 1);
    margin: 12px 30px 0px 30px;
}

button {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;
    color: rgba(71, 67, 25, 1);
    cursor: pointer;

    width: 124px;
    height: 60px;
    margin: 34px 188px 34px 188px;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1)
}

button:active {
    transform: scale(0.9);
}
</style>

<script>
export default {
    data() {
        return {
            text: "",
            title: "",
            notificationIsShow: true
        }

    },
    mounted() {
        // this.hideNotification()
        if (this.edit) {
            this.title = 'Смена почты'
            this.text = 'была отправлена ссылка для подтверждения смены почты.'

        }
        else {
            this.title = 'Подтверждение почты'
            this.text = 'была отправлена ссылка для подтверждения аккаунта.'
        }
    },
    props: {
        email: String,
        edit: Boolean,
        showannouncement: Boolean
    },
    methods: {
        hide() {
            this.$emit('showannouncement')
            this.notificationIsShow = true
        }
    },


}
</script>
