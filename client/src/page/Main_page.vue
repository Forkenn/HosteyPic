<template>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>main screen</title>

    </head>

    <body>
        <div v-if="show">
            <Login :login1="login" @authorised1="authorised1" @show_ch='show_login' />
            <div class="gray" @click=show_login(true)></div>
        </div>

        <div v-show="visable.user & visable.post" class="page">


            <HeaderNoAuth v-if="!authorised" @login='login_ch' @show_ch='show_login' />
            <HeaderAuth v-if="authorised" />



            <div class="wrapper__searchbar">
                <div class="searchbar">
                    <div class="input">
                        <input v-model="serach" v-on:keyup.enter="loadImg(this.serach)"
                            placeholder="Напишите здесь для поиска..." id="idSearch">
                    </div>
                    <div class="searchbar__icon">

                        <img src="../assets/img/svg/searchicon.svg" @click="loadImg(this.serach)" alt="">
                    </div>
                </div>
            </div>



            <Searchimg :res="result" :urlstr="urlstr" />

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
            srcimg: "",
            urlstr: "",
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
                this.loading = true

            })
            .catch(error => {
                this.loading = true
                console.log(error.message);
            })
            .finally(() => {
                this.visable.user = true
            });



        axios({
            timeoute: 1000,
            method: 'get',
            url: import.meta.env.VITE_BACKEND_URL + 'posts?start=0&end=20',

            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.result = response.data.items
                this.urlstr = 'posts'
                // console.log(this.result);
                // console.log(response.data)

            })
            .catch(error => {
                console.log(error.message);
            })
            .finally(() => {
                this.visable.post = true
            });;
    },
    methods: {
        show_login(show) {
            // console.log(show, this.login)
            if (show) {
                this.show = false
            }
            else {
                this.show = true
            }

        },
        login_ch(login) {
            this.login = login
        },
        loadImg(q) {
            if (this.serach.length > 0)
                axios({
                    timeoute: 1000,
                    method: 'get',
                    url: import.meta.env.VITE_BACKEND_URL + `posts/search?q=${q}&start=0&end=20`,

                    withCredentials: true,
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(response => {
                        this.result = response.data.items
                        this.urlstr = `posts/search?q=${q}&start=0&end=20`
                        // console.log(this.result);
                        // console.log(response.data)

                    })
                    .catch(error => {
                        console.log(error.message);
                    })
        },
        authorised1(authorised) {
            this.authorised = authorised
        },
        goToAbout() {
            this.$router.push('/about')
        },
        goToUser() {
            this.$router.push({ name: 'userview', params: { id: this.userId } })
        },
        // onEnter: function() {
        //   console.log(this.serach);
        // },

    },
};


</script>