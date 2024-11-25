<template>

    <div class="page">
        <HeaderAuth />
        <Announcement v-show="showannouncement" @showannouncement=ShowAnnouncement :email="this.email" :edit="true" />
        <div>
            <div class="menu">
                <div class="tabs-header">

                    <button class="tabs-btn" style="margin-top: 65px;" @click="activeTab = 1"
                        :class="{ active: activeTab === 1 }">Профиль
                    </button>
                    <button class="tabs-btn" @click="activeTab = 2" :class="{ active: activeTab === 2 }">Контакты
                    </button>
                    <button class="tabs-btn" @click="activeTab = 3" :class="{ active: activeTab === 3 }">Безопасность
                    </button>

                </div>
            </div>
        </div>
        <div class="tabs_body">
            <div class="wrap__edit" v-show="activeTab === 1">

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
                    <div style="position: relative;">
                        <label class="error_inp" v-if="busy">
                            Никнейм уже занят
                        </label>
                        <label class="error_inp" v-if="nick_valid">
                            Неверный формат ника
                        </label>
                    </div>
                </div>

            </div>

            <div class="wrap__edit" v-show="activeTab === 2">
                <div class="wrap__item" style="position: relative;">
                    <label>О себе</label>
                    <textarea v-model="social.about_me" placeholder="Расскажите о себе" maxlength="140"></textarea>
                    <div class="count">
                        {{ social.about_me.length }} / 140
                    </div>
                </div>

                <div class="wrap__item">
                    <p>Ссылки</p>

                    <label class="lbl_social">GitLab</label>
                    <input v-model="social.gitlab_link" class="inpt_social" type="text"
                        placeholder="https://gitlab.com/username">
                    <div style="position: relative;">
                        <label class="error_inp" v-if="valid.gitlab">
                            Неверный формат ссылки
                        </label>
                    </div>
                    <label class="lbl_social">GitHub</label>
                    <input v-model="social.github_link" class="inpt_social" type="text"
                        placeholder="https://github.com/username">
                    <div style="position: relative;">
                        <label class="error_inp" v-if="valid.github">
                            Неверный формат ссылки
                        </label>
                    </div>
                    <label class="lbl_social">VK</label>
                    <input v-model="social.vk_link" class="inpt_social" type="text"
                        placeholder="https://vk.com/username">
                    <div style="position: relative;">
                        <label class="error_inp" v-if="valid.vk">
                            Неверный формат ссылки
                        </label>
                    </div>
                    <label class="lbl_social">OK</label>
                    <input v-model="social.ok_link" class="inpt_social" type="text"
                        placeholder="https://ok.com/username">
                    <div style="position: relative;">
                        <label class="error_inp" v-if="valid.ok">
                            Неверный формат ссылки
                        </label>
                    </div>
                </div>
                <div class="button__save">
                    <button @click="EditAbout()">
                        Сохранить
                    </button>
                </div>
            </div>

            <div class="wrap__edit" v-show="activeTab === 3">
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
                    <input v-model="password.second" type="password" placeholder="********">
                    <div style="position: relative;">
                        <label class="error_inp" v-if="valid_pas">
                            Пароль слишком легкий
                        </label>
                    </div>
                    <label class="lbl_social" style="font-size: 24px;">Подтвердите пароль</label>
                    <div class="inptbtn"><input id="conf_pas" v-model="password.third" type="password"
                            placeholder="********">



                        <button @click="EditPassword" class="btn_edit">Изменить</button>
                    </div>
                    <div style="position: relative;">
                        <label class="error_inp" v-if="conf_err">
                            Пароли не совпадают
                        </label>
                    </div>
                </div>
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


.menu {
    position: relative;
    max-width: 1440px;
    margin-left: 80px;
    margin-right: auto;
}

.tabs-header {
    position: absolute;
    top: 0;
    left: 0;
    width: 190px;
    height: 197px;

    border-radius: 0px 0px 16px 16px;
    background: rgba(239, 237, 217, 1);
    display: flex;
    flex-wrap: wrap;
    align-items: end;
    justify-content: center;

}

.tabs-btn {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

    width: 180px;
    height: 39px;
    margin-bottom: 5px;
    border-radius: 16px;
    border: 0;
    padding-left: 10px;
    background: rgba(239, 237, 217, 1);
}

.tabs-btn.active {

    background: rgba(224, 220, 178, 1);

}

.error_inp {
    position: absolute;
    top: 5px;
    left: 0;
    margin: 0;
    margin-left: 10px;
    font-family: Balsamiq Sans;
    font-size: 14px;
    font-weight: 400;
    line-height: 16.8px;
    text-align: left;
    color: rgba(189, 38, 38, 1);

}

.tabs_body {
    max-width: 583px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    justify-content: center;
}

.tabs-body-item {
    background: rgba(239, 237, 217, 1);

    margin-top: 40px;
    display: flex;
    flex-wrap: wrap;
    /* flex-direction: column; */
    /* align-items: center; */
    justify-content: center;
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: left;

    border-radius: 50px;
    width: 100%;
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

    width: 100%;
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

.count {
    position: absolute;
    right: 12px;
    bottom: 1px;
    font-family: Balsamiq Sans;
    font-size: 14px;
    font-weight: 400;
    line-height: 16.8px;
    text-align: left;
    color: rgba(71, 67, 25, 1);

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
    width: 100%;
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
    justify-content: center;
}

.button__save button {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: center;


    color: rgba(71, 67, 25, 1);
    width: 153px;
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
            busy: false,
            nick_valid: false,
            conf_err: false,
            valid_pas: false,
            file: Object,
            activeTab: 1,
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
                third: "",
            },
            social: {
                vk_link: "",
                ok_link: "",
                github_link: "",
                gitlab_link: "",
                about_me: "",
            },
            show: false,
            valid: {
                gitlab: false,
                github: false,
                vk: false,
                ok: false,
            }
        }

    },
    watch: {
        'password.second': function (newval) {

            let reg = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*#?&]{6,}$/
            if (newval.length > 0)
                this.valid_pas = !reg.test(newval)
        },
        'password.third': function (newval) {

            if (newval == this.password.second)
                this.conf_err = false
        },
    },
    mounted() {
        const conf_pas = document.getElementById('conf_pas')
        conf_pas.addEventListener('blur', () => {
            if (this.password.second != this.password.third)
                this.conf_err = true
            else
                this.conf_err = false

        })

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
                    this.email = response.data.email
                    this.social.about_me = response.data.about_me
                    this.social.vk_link = response.data.vk_link
                    this.social.ok_link = response.data.ok_link
                    this.social.github_link = response.data.github_link
                    this.social.gitlab_link = response.data.gitlab_link
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
            this.busy = false
            this.nick_valid = false
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
                    if (error.status == 400) {
                        this.busy = true
                    }
                    if (error.status == 422) {
                        this.nick_valid = true
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
        EditAbout() {
            axios({
                timeoute: 1000,
                method: 'patch',
                url: import.meta.env.VITE_BACKEND_URL + 'users/current',
                data: {
                    about_me: this.social.about_me,
                    vk_link: this.social.vk_link,
                    ok_link: this.social.ok_link,
                    github_link: this.social.github_link,
                    gitlab_link: this.social.gitlab_link,
                },
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log(response);
                    this.valid.vk = false
                    this.valid.ok = false
                    this.valid.gitlab = false
                    this.valid.github = false
                })
                .catch(error => {
                    if (error.status != null) {

                    }
                    error.response.data.detail.forEach(element => {
                        if (element.loc[1] == 'vk_link')
                            this.valid.vk = true
                        if (element.loc[1] == 'gitlab_link')
                            this.valid.gitlab = true
                        if (element.loc[1] == 'github_link')
                            this.valid.github = true
                        if (element.loc[1] == 'ok_link')
                            this.valid.ok = true
                    });
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
