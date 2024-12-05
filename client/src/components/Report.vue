<template>



    <div v-if="showreport">

        <div @click="hide()" class="gray">

        </div>
        <div class="wrap" v-if="showreport">
            <div class="title">
                <p>Жалоба</p>
                <img @click="hide()" src="../assets/img/svg/X_dark.svg" alt="">
            </div>
            <div class="text">
                <textarea v-model="this.textReport" maxlength="300"
                    placeholder="Пожалуйста, укажите причину жалобы"></textarea>
                <div class="count">
                    {{ textReport.length }} / 300
                </div>
            </div>
            <button @click="report">Отправить</button>
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
    width: 574px;
    max-height: 303px;
    border-radius: 50px;
    transform: translate(-50%, -50%);
    background: #EFEDD9;
    display: flex;
    flex-wrap: wrap;
    padding: 40px 30px 40px 30px;
    z-index: 1600;
}

.title {
    display: flex;
    width: 100%;
    justify-content: space-between;
    align-items: center;

    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;
    color: rgba(71, 67, 25, 1);


}

.title img {
    cursor: pointer;
}

.text {
    max-width: 514px;
    flex-grow: 1;
    position: relative;
}

.count {
    position: absolute;
    right: 12px;
    bottom: -15px;
    font-family: Balsamiq Sans;
    font-size: 14px;
    font-weight: 400;
    line-height: 16.8px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

}

textarea {
    width: 100%;
    height: 96px;
    border-radius: 16px;
    outline: none;
    resize: none;
    border: 2px solid rgba(177, 167, 63, 1);
    caret-color: rgba(71, 67, 25, 1);
    padding: 10px 20px 10px 20px;

    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;
    color: rgba(71, 67, 25, 1);


}

textarea::-webkit-scrollbar {
    width: 0;
}

textarea::placeholder {
    color: rgba(71, 67, 25, 0.7);

}

button {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;
    color: rgba(71, 67, 25, 1);
    cursor: pointer;

    width: 239px;
    height: 58px;
    margin: 30px 137px 40px 138px;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1);
    background-color: white;

}

button:active {
    transform: scale(0.9);
}
</style>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            textReport: "",
        }

    },
    mounted() {
        this.textReport = ""
    },
    props: {
        showreport: Boolean,
        reportid: Number
    },
    watch: {
        showreport: function (newVal, oldVal) {
            this.textReport = ""

        },
    },
    methods: {
        hide() {
            this.$emit('showreport', true)
        },
        report() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `reports?post_id=${this.reportid}&text_body=${this.textReport}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    this.hide()
                })
                .catch(error => {
                    console.log(error)
                });
        },
    },


}
</script>
