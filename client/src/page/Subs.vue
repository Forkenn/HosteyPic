<template>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>main screen</title>

    </head>

    <body>
        <div v-show="visable.post & visable.user" class="page">

            <HeaderAuth />

            <Searchimg :res="result" :urlstr="'posts/followed'" />
            <div v-show="result.length == 0" class="text">
                <p>
                    Подпишитесь на кого-нибудь! <br> Здесь будут отображаться их творения! :)
                </p>
            </div>

            <Bottom />
        </div>


    </body>
</template>

<style scoped>
@import '../assets/reset.css';
@import '../assets/style_main.css';
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');

@font-face {
    font-display: swap;
    /* Check https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display for other options. */
    font-family: 'Chewy';
    font-style: normal;
    font-weight: 400;
    src: url('../assets/fonts/chewy-v18-latin-regular.woff2') format('woff2');
    /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
}


.text {
    max-width: 1228px;
    display: flex;
    justify-content: center;
    margin: auto;
    margin-top: 79px;
}

p {
    font-family: Balsamiq Sans;
    font-size: 64px;
    font-weight: 400;
    line-height: 76.8px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(71, 67, 25, 1);

}
</style>
<script>

import Searchimg from "../components/Searchimg.vue"
import Login from "../components/Login.vue"
import Bottom from "../components/Bottom.vue"
import HeaderNoAuth from "@/components/HeaderNoAuth.vue"
import HeaderAuth from "@/components/HeaderAuth.vue"
import axios from "axios";

const data = ['красивый фон.jpg', 'пальмы.jpg', 'test.jpg', 'vkTm8xmeOTo.jpg']

export default {
    components: { Searchimg, Login, Bottom, HeaderNoAuth, HeaderAuth },
    data() {
        return {
            visable: {
                user: false,
                post: false,
            },
            userId: 0,
            authorised: false,
            login: true,
            show: false,
            serach: "",
            result: [],
            data,
            tag: "123",
            srcimg: ""
        };
    },
    mounted() {

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
                if (response.status == 200) { this.authorised = true }
                // console.log(response);

            })
            .catch(error => {
                this.$router.push({
                    name: 'codeerrorview',
                    query: {
                        ErrorNum: 404
                    }
                })

            })
            .finally(() => {
                this.visable.user = true
            });


        axios({
            timeoute: 1000,
            method: 'get',
            url: import.meta.env.VITE_BACKEND_URL + 'posts/followed?start=0&end=20',

            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.result = response.data.items
                // console.log(this.result);
                // console.log(response.data)

            })
            .catch(error => {
                console.log(error.message);
            })
            .finally(() => {
                this.visable.post = true
            });

    },
    methods: {

    },
};


</script>