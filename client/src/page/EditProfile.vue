<template>

    <div class="page">
        <HeaderAuth />
        <Announcement v-show="showannouncement" @showannouncement=ShowAnnouncement :email="this.email" :edit="true" />
        <div class="wrap__edit">

            <div class="wrap__item">
                <label>Фото</label>
                <div class="icon_btn">
                    <!-- <input id="file" type="file" @change="onFileSelected" hidden accept="image/*,.png,.jpeg,.jpg" /> -->
                    <div class="img__wrap">
                        <img v-if="image.name" :src="image.url" alt="аватарка">
                        <img v-else :src="`../../dist/uploads/avatars/original/${this.avatar}`" alt="аватарка">

                    </div>
                    <button @click="show_edit" class="btn_edit">Изменить</button>
                </div>
                <div v-if="show" class="editavatar">
                    <AvatarUploader :avatar="avatar" />
                </div>
            </div>
            <div class="wrap__item">
                <label>Псевдоним</label>
                <div class="inptbtn">
                    <input v-model="username" type="text" placeholder="Псевдоним">
                    <button @click="SetUsername" class="btn_edit">Изменить</button>
                </div>
            </div>
            <div class="wrap__item">
                <label>О себе</label>
                <textarea placeholder="Расскажите о себе"></textarea>
            </div>
            <div class="wrap__item">
                <label>Почта</label>
                <div class="inptbtn">
                    <input type="text" v-model=email>
                    <button class="btn_edit" @click="EditEmail(); ShowAnnouncement()">Изменить</button>
                </div>
            </div>
            <div class="wrap__item">
                <p>Пароль</p>
                <label class="lbl_social" style="font-size: 24px;">Введите старый пароль</label>
                <input v-model="password.first" type="password" placeholder="********">

                <label style="font-size: 24px; margin-top: 10px;">Введите новый пароль</label>
                <div class="inptbtn"><input v-model="password.second" type="password" placeholder="********">

                    <button @click="EditPassword" class="btn_edit">Изменить</button>
                </div>
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

    width: 482px;
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

/* .wrap__item img {
    height: 100px;
    width: 100px;
} */

.img__wrap {
    /* min-width: 256px; */
    width: 100px;
    height: 100px;
    /* overflow: hidden; */
    position: relative;
}

.icon_btn {
    display: flex;
    align-items: center;
}

.icon_btn img {
    border-radius: 50%;
    height: 100%;
    width: 100%;
    object-fit: cover;
    position: absolute;
    left: 0;
    top: 0;
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

input:focus::placeholder {
    color: transparent
}

textarea:focus::placeholder {
    color: transparent
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

button:active {
    transform: scale(0.9);
}

.editavatar {
    height: 350px;
    margin-top: 10px;
}
</style>

<script>
import HeaderAuth from '@/components/HeaderAuth.vue';
import Bottom from '@/components/Bottom.vue';
import AvatarUploader from '@/components/AvatarUploader.vue';
import Announcement from '@/components/Announcement.vue';

import axios from 'axios';


export default {
    components: { Bottom, HeaderAuth, AvatarUploader, Announcement },
    data() {
        return {
            showannouncement: false,
            file: Object,
            username: "",
            avatar: "",
            email: "",
            image: {
                name: "",
                url: "",
            },
            password: {
                first: "",
                second: "",
            },
            show: false,
        }

    },
    mounted() {
        axios({
            timeoute: 1000,
            method: 'get',
            url: (import.meta.env.VITE_BACKEND_URL + `users/current`),
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                if (response.status == 200) {
                    console.log(response);
                    this.username = response.data.username
                    this.userId = response.data.id
                    if (response.data.avatar) {
                        this.avatar = response.data.avatar
                    }
                    else {
                        this.avatar = "0Z9fPWMyZfPi2VAUi9LvdRiAr9HhDM.jpg"
                    }
                    this.email = response.data.email
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
        show_edit() {
            this.show = !this.show
        },
        onFileSelected(event) {
            this.file = event.target.files[0];
            if (!['image/jpeg', 'image/png', 'image/jpg'].includes(this.file.type))
                alert('неверный файл')
            else {
                const reader = new FileReader(); // Создаём новый экземпляр FileReader 
                reader.onload = ({ target }) => {
                    const img = new Image(); // Подготавливаем изображение для работы с ним 
                    img.onload = () => {
                        // img.width
                        // alert(`Размер: ${this.file.size} байт, Ширина: ${img.width}px, Высота: ${img.height}px`); // И вот что у нас получилось! 
                        if (img.width < 256) {
                            console.log("ошибка")
                        }
                        else {
                            this.image.name = this.file.name
                            this.image.url = URL.createObjectURL(this.file)
                        }
                    };
                    img.src = target.result;

                };
                reader.readAsDataURL(this.file); // Преобразуем файл в формат Base64 
            }
        },
        SetUsername() {
            console.log(this.file)
            axios({
                timeoute: 1000,
                method: 'patch',
                url: import.meta.env.VITE_BACKEND_URL + 'users/current/username',
                data: { username: this.username },
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log(response);
                    window.location.reload()
                })
                .catch(error => {
                    if (error.status != null) {
                        // this.$router.push({
                        //     name: 'codeerrorview',
                        //     query: {
                        //         ErrorNum: error.status
                        //     }
                        // })
                    }
                    console.log(error.message);
                    // console.log(error.toJSON())
                });
        },
        EditEmail() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: import.meta.env.VITE_BACKEND_URL + 'auth/request-change-email',
                data: { new_email: this.email },
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log(response);
                    // window.location.reload()
                })
                .catch(error => {
                    if (error.status != null) {
                        // this.$router.push({
                        //     name: 'codeerrorview',
                        //     query: {
                        //         ErrorNum: error.status
                        //     }
                        // })
                    }
                    console.log(error.message);
                });
        },
        EditPassword() {
            axios({
                timeoute: 1000,
                method: 'post',
                url: import.meta.env.VITE_BACKEND_URL + 'auth/change-password',
                data: {
                    old: this.password.first,
                    new: this.password.second
                },
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log(response);
                    // window.location.reload()
                })
                .catch(error => {
                    if (error.status != null) {
                        // this.$router.push({
                        //     name: 'codeerrorview',
                        //     query: {
                        //         ErrorNum: error.status
                        //     }
                        // })
                    }
                    console.log(error.message);
                });
        },
        ShowAnnouncement() {
            this.showannouncement = !this.showannouncement
        }

    }
}
</script>
