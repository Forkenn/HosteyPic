<template>
    <div v-if="show">
        <Login :login1="login" @authorised1="authorised1" @show_ch='show_login' />
        <div class="gray" @click=show_login(true)></div>
    </div>
    <div v-show="visable.user" class="page">
        <HeaderNoAuth v-if="!authorised" @login='login_ch' @show_ch='show_login' />
        <HeaderAuth v-if="authorised" />

        <div class="text">
            <div class="wrap_p" style="margin-top: 0px;">
                <p>
                    HosteyPIC — это веб-приложение, которое позволяет пользователям делиться своими изображениями и
                    находить
                    вдохновение в работах других. Пользователи могут легко загружать свои работы, а также просматривать
                    и
                    оценивать творчество, загруженное другими пользователями.
                </p>
            </div>
            <div class="wrap_p">
                <p>
                    Приложение предлагает удобный интерфейс для поиска интересных изображений по тексту, что позволяет
                    быстро
                    находить то, что вам нужно. Кроме того, у каждого пользователя есть возможность сохранять
                    понравившиеся
                    картинки в своем аккаунте или скачивать их на устройство.
                </p>
            </div>
            <div class="wrap_p">
                <p>
                    С HosteyPIC вы сможете не только делиться своим творчеством, но и вдохновляться работами других,
                    создавая
                    уникальное сообщество любителей искусства!
                </p>
            </div>
        </div>
        <Bottom />
    </div>

</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');

.gray {
    background-color: rgba(1, 1, 1, 0.75);
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    z-index: 1500;
}

.page {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background-image: url('../assets/img/svg/BackgroundAbout.svg');
    background-size: 100% 100%;
    background-repeat: no-repeat;
}

p {
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

}

.text {
    max-width: 1440px;
    height: auto;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    margin-top: auto;
    margin-left: auto;
    margin-right: auto;
}

.wrap_p {
    margin-top: 60px;
    margin-left: 80px;
    margin-right: 80px;
}
</style>

<script>

import axios from 'axios';
import HeaderAuth from '@/components/HeaderAuth.vue';
import HeaderNoAuth from '@/components/HeaderNoAuth.vue';
import Bottom from '@/components/Bottom.vue'
import Login from '@/components/Login.vue';


export default {
    data() {
        return {
            show: false,
            visable: {
                user: false,
            },
            authorised: false,
        }
    },
    components: { Login, Bottom, HeaderAuth, HeaderNoAuth },
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
                this.loading = true

            })
            .catch(error => {
                this.loading = true
                console.log(error.message);
            })
            .finally(() => {
                this.visable.user = true
            });
    },
    methods: {
        authorised1(authorised) {
            this.authorised = authorised
        },
        show_login(show) {
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
    }
}
</script>