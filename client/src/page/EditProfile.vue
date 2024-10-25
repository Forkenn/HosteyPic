<template>
    <div class="page">
        <HeaderAuth />

        <div class="wrap__edit">

            <div class="wrap__item">
                <label>Фото</label>
                <div class="icon_btn">
                    <img src="../assets/img/svg/userIconmain.svg" alt="аватарка">
                    <button class="btn_edit">Изменить</button>
                </div>
            </div>
            <div class="wrap__item">
                <label>Псевдоним</label>
                <div class="inptbtn">
                    <input type="text" placeholder="Псевдоним">
                    <button class="btn_edit">Изменить</button>
                </div>
            </div>
            <div class="wrap__item">
                <label>О себе</label>
                <textarea placeholder="Расскажите о себе"></textarea>
            </div>
            <div class="wrap__item">
                <label>Почта</label>
                <div class="inptbtn">
                    <input type="text" placeholder="user_mail@mail.ru">
                    <button class="btn_edit">Изменить</button>
                </div>
            </div>
            <div class="wrap__item">
                <p>Пароль</p>
                <label style="font-size: 24px;">Введите новый пароль</label>
                <div class="inptbtn">
                    <input type="password" placeholder="********">
                    <button class="btn_edit">Изменить</button>
                </div>
                <label style="font-size: 24px;">Подтвердите пароль</label>
                <input type="password" placeholder="********">
            </div>
            <div class="wrap__item">
                <p>Ссылки</p>

                <label class="lbl_social">GitLab</label>
                <input class="inpt_social" type="text" placeholder="https://gitlab.com/username">
                <label class="lbl_social">GitHub</label>
                <input class="inpt_social" type="text" placeholder="https://github.com/username">
                <label class="lbl_social">VK</label>
                <input class="inpt_social" type="text" placeholder="https://vk.com/username">
                <label class="lbl_social">OK</label>
                <input class="inpt_social" type="text" placeholder="https://ok.com/username">
            </div>
            <div class="button__save">
                <button style="width: 237px;">Сохранить</button>
                <button style="width: 194px;">Отмена</button>
            </div>
        </div>

        <Bottom />
    </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');
@import '../assets/reset.css';

.page {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.wrap__edit {

    width: 540px;
    /* height: 1145px; */
    margin: auto;
    margin-top: 60px;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: left;
    margin-bottom: 50px;
}

.wrap__photo {
    width: 273px;
    /* height: 143px; */
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
}

.wrap__item img {
    height: 100px;
    width: 100px;
}

.icon_btn {
    display: flex;
    align-items: center;
}

.wrap__item {
    margin-top: 20px;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    /* box-sizing: content-box; */

}

.btn_edit {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: center;

    width: 153px;
    height: 40px;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1);
    background: rgba(255, 255, 255, 1);
    margin-left: 19px;
    color: rgba(71, 67, 25, 1);

}

label {
    margin-right: auto;

    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

}

textarea {
    box-sizing: border-box;
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;

    width: 473px;
    height: 96px;

    border-radius: 16px;
    border: 2px solid #B1A73F;
    outline: none;
    resize: none;
    color: rgba(71, 67, 25, 1);

    caret-color: rgba(71, 67, 25, 1);
    padding-left: 20px;
    padding-right: 20px;
}

textarea::placeholder {
    color: rgba(71, 67, 25, 0.7);
}

input {
    width: 300px;
    height: 40px;
    border-radius: 16px;
    border: 2px solid rgba(177, 167, 63, 1);
    padding-left: 20px;
    padding-right: 20px;
    color: rgba(71, 67, 25, 1);
    caret-color: rgba(71, 67, 25, 1);
    outline: none;

}

input::placeholder {
    color: rgba(71, 67, 25, 0.7);
}

.inpt_social {
    width: 473px;
    height: 40px;

    border-radius: 16px;
    border: 2px solid rgba(177, 167, 63, 1)
}

p {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

}

.lbl_social {
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;
    color: rgba(71, 67, 25, 1);
    margin-top: 20px;
}

.button__save {
    width: 100%;
    margin-top: 50px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.button__save button {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;
    color: rgba(71, 67, 25, 1);

    height: 50px;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1)
}
</style>

<script>
import HeaderAuth from '@/components/HeaderAuth.vue';
import Bottom from '@/components/Bottom.vue';

import axios from 'axios';


export default {
    components: { Bottom, HeaderAuth },
    data() {
        return {

        }

    },
    mounted() {
        axios({
            timeoute: 1000,
            method: 'get',
            url: (`http://localhost/api/users/current`),
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                if (response.status == 200) {
                    console.log(response);
                    this.userName = response.data.username
                    this.userId = response.data.id
                }

            })
            .catch(error => {
                if (error.status != null) {
                    if (error.status != 401)
                        this.$router.push({
                            name: 'codeerrorview',
                            query: {
                                ErrorNum: error.status
                            }
                        })
                    else {
                        this.$router.push({ name: 'homeview' })
                    }
                }
            });
    },
    methods: {

    }
}
</script>
