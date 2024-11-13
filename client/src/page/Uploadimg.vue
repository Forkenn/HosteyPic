<template>
    <div class="page">
        <HeaderAuth />
        <div class="wrap">
            <div class="drag__drop__wrap">
                <input id="file" type="file" @change="onFileSelected" hidden accept="image/*,.png,.jpeg,.jpg" />
                <div v-if="!droped" onclick="file.click()" class="drag__drop" @dragover.prevent="onDragOver"
                    @dragleave.prevent="onDragLeave" @drop.prevent="onDrop">

                    <div>
                        <div class="text">
                            <p>Выберите файл</p>
                            <p>или</p>
                            <p>перетащите его сюда</p>
                        </div>
                        <img class="download" src="../assets/img/svg/Download.svg" alt="">
                        <div class="text2">
                            <p> На данный момент допустима</p>
                            <p>загрузка изображений до 20 Мб</p>
                        </div>
                    </div>


                </div>
                <div v-else class="dropimg__wrap">
                    <div class="img__wrap" style="position: relative;">
                        <div class="reset" @click="reset">
                            <img src="../assets/img/svg/reset.svg" alt="">
                        </div>
                        <img class="drop_img" :src="image.url" :style="this.styleobj" alt="drop_img">
                    </div>
                    <div style="display: flex; align-items: center; justify-content: center;">
                        <button @click="UploadImg">Опубликовать</button>
                    </div>
                </div>
                <div :class="[{ input__wrap: droped }, { disable: !droped }]">
                    <label>Название</label>
                    <textarea class="name" v-model="title" placeholder="Придумайте название"
                        :readonly="!droped"></textarea>
                    <label>Описание</label>
                    <textarea :readonly="!droped" v-model="body" class="description"
                        placeholder="Подробно опишите"></textarea>
                    <!-- <label>Альбом</label>
                    <textarea :readonly="!droped" placeholder="Выберите альбом"></textarea> -->
                    <label>Теги</label>
                    <input id="idSearch" :readonly="!droped" maxlength="30" v-model="taginput"
                        placeholder="Введите тег для поиска"></input>
                    <div class="maxvalue" style="position: relative;" v-show="ArrayTag.length == 10">
                        <p
                            style="position: absolute; top: -15px; left: 20px; color:rgba(189, 38, 38, 1); width: 200px;">
                            Достигнут
                            лимит тегов.</p>
                    </div>
                    <div class="wrap_tagul" style="position: absolute; top: 510px;"
                        v-show="taginput.length > 0 & ArrayTag.length != 10">
                        <div id="searchResults" class="tagul">
                            <ul style="color: black;">
                                <li class="tagli" v-for="el in tags.items" @click="addtag(el.name, el.id)"
                                    v-show="!this.ArrayTag.find(function (item) { return item.id === el.id; })">
                                    {{ el.name }}
                                    {{ ArrayTag.id }}</li>
                            </ul>
                        </div>
                    </div>
                    <AddTag :ArrayTag="ArrayTag" />
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
    /* box-sizing: border-box; */
}

.wrap {

    overflow: hidden;
    margin-bottom: 40px;
}

.drag__drop__wrap {
    max-width: 1440px;
    margin-top: 40px;

    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: flex-start;
    min-height: 688px;
}

.drag__drop {
    background: rgba(239, 237, 217, 1);

    align-self: flex-start;
    margin-left: 80px;
    width: 420px;
    height: 600px;

    border-radius: 50px;


    border: 4px dashed rgba(177, 167, 63, 1);


}

.input__wrap {
    /* overflow: hidden; */
    width: calc(100% - 630px);
    min-width: 300px;
    margin-left: 40px;
    align-self: flex-end;
    align-self: start;
    display: flex;
    flex-direction: column;
    margin-right: 80px;
    align-items: flex-start;

}

label {

    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    margin-left: 20px;
    color: rgba(71, 67, 25, 1);


}

textarea {
    box-sizing: border-box;
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    padding-left: 20px;
    padding-top: 10px;
    max-width: 820px;
    width: 100%;
    border-radius: 16px;
    border: 2px solid #B1A73F;
    outline: none;
    resize: none;
    margin-bottom: 20px;
    height: 40px;
    color: rgba(71, 67, 25, 1);

    caret-color: rgba(71, 67, 25, 1);

}

textarea ::placeholder {
    color: rgba(71, 67, 25, 0.7);
    margin-left: 20px;

}

textarea:focus::placeholder {
    color: transparent;
}

input {

    box-sizing: border-box;
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    padding-left: 20px;
    max-width: 840px;
    width: 100%;
    border-radius: 16px;
    border: 2px solid #B1A73F;
    outline: none;
    resize: none;
    margin-bottom: 20px;
    height: 40px;
    color: rgba(71, 67, 25, 1);
    caret-color: rgba(71, 67, 25, 1);
}

input ::placeholder {
    color: rgba(71, 67, 25, 0.7);
    margin-left: 20px;

}

input:focus::placeholder {
    color: transparent;
}

.name {
    height: 40px;
    /* width: 840px; */
    padding-top: 8px;
    align-items: center;


}

.description {
    height: 158px;
}

.text {
    margin-top: 142px;
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: center;
    max-height: 80px;
    color: rgba(71, 67, 25, 1);

}

.download {

    margin-top: 26px;
    margin-left: 190px;

}

.text2 {
    font-family: Balsamiq Sans;
    font-size: 24px;
    font-weight: 400;
    line-height: 28.8px;
    text-align: center;
    color: rgba(71, 67, 25, 0.7);
    margin-top: 195px;
}

.dropimg__wrap {
    align-self: flex-start;
    margin-left: 80px;
    max-width: 420px;

    /* max-height: 600px; */
    /* overflow: hidden; */
}

.img__wrap {
    /* min-width: 256px; */
    width: 420px;
    height: 600px;
    overflow: hidden;
    border-radius: 50px;
}

.reset {
    position: absolute;
    right: 0px;
    top: 0px;
    height: 70px;
    width: 70px;
    background: rgba(71, 67, 25, 0.5);
    border-radius: 0 0 0 50%;
    display: flex;
    justify-content: center;
}

.reset img {
    width: 40px;
}

.drop_img {
    border-radius: 50px;
    border: 4px solid rgba(177, 167, 63, 1)
}

button {
    font-family: Balsamiq Sans;
    font-size: 32px;
    font-weight: 400;
    line-height: 38.4px;
    text-align: center;
    color: rgba(71, 67, 25, 1);
    padding: 6px 40px 6px 40px;
    margin-top: 42px;
    /* margin-left: 65px; */
    width: 290px;
    height: 50px;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1)
}

button:active {
    transform: scale(0.90);
}

.disable {
    width: calc(100% - 630px);
    min-width: 300px;
    margin-left: 40px;
    align-self: flex-end;
    align-self: start;
    display: flex;
    flex-direction: column;
    margin-right: 80px;
    align-items: flex-start;
}

.disable input {
    background: rgba(201, 201, 201, 1);
    color: rgba(146, 146, 146, 1);
    border: 2px solid rgba(146, 146, 146, 1) read
}

.disable input::placeholder {
    color: rgba(146, 146, 146, 0.7);
}

.disable textarea {
    background: rgba(201, 201, 201, 1);
    color: rgba(146, 146, 146, 1);
    border: 2px solid rgba(146, 146, 146, 1)
        /*  */

}

.disable textarea::placeholder {
    color: rgba(146, 146, 146, 0.7);
}

.disable label {
    color: rgba(146, 146, 146, 1);

}

.wrap_tagul {
    position: relative;
    border-radius: 20px;
    margin-top: 10px;
    width: 300px;
    height: 200px;
    background: rgba(239, 237, 217, 1);
    border: 2px solid rgba(177, 167, 63, 1);
    overflow: hidden;
}

.tagul {
    position: absolute;
    top: 0;
    left: 0;
    padding: 5px 5px 5px 20px;
    width: calc(100% - 5px);
    max-height: 200px;
    overflow: scroll;
    scroll-margin: 20px;
    /* background-color: black; */
}

.tagli {
    margin-top: 10px;
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(71, 67, 25, 1);


}

.tagli:hover {
    background: rgba(224, 220, 178, 1);


}

.maxvalue p {
    font-family: Balsamiq Sans;
    font-size: 14px;
    font-weight: 400;
    line-height: 16.8px;
    text-align: left;

}

.hide {
    display: none;
}
</style>

<script>

import HeaderAuth from '@/components/HeaderAuth.vue';
import Bottom from "../components/Bottom.vue";
import AddTag from '@/components/AddTag.vue';
import axios from 'axios';
export default {
    components: { HeaderAuth, Bottom, AddTag },
    data() {
        return {
            title: "",
            body: "",
            input__wrap: 'input__wrap',
            disable: 'disable',
            taginput: "",
            tag: "",
            ArrayTag: [],
            droped: false,
            file: Object,
            image: {
                name: "",
                url: "",
            },
            tags: "",
            styleobj: {
                width: "",
                height: "",

            },
        }

    },
    mounted() {
        document.querySelector('#idSearch').oninput = function () {
            let val = this.value.trim();

            let itemli = document.querySelectorAll('.tagli');
            if (val != '') {
                itemli.forEach(function (elem) {
                    if (elem.innerText.search(val) == -1) {
                        elem.classList.add('hide');
                    }
                    else {
                        elem.classList.remove('hide');
                    }
                });
            }
            else {
                itemli.forEach(function (elem) {
                    elem.classList.remove('hide');
                });
            }
        }


        axios({
            timeoute: 1000,
            method: 'get',
            url: (import.meta.env.VITE_BACKEND_URL + `tags`),
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.tags = response.data

            })
            .catch(error => {
                if (error.status != null) {
                    this.$router.push({
                        name: 'codeerrorview',
                        query: {
                            ErrorNum: error.status
                        }
                    })
                }
            });
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
                if (response.status == 200) {
                    this.authorised = true
                }
                else {
                    this.$router.push({ name: 'homeview' })
                }

            })
            .catch(error => {
                if (error.status != null) {
                    this.$router.push({
                        name: 'homeview',
                    })
                }
                console.log(error.message);
            });

    },
    methods: {

        addtag(tag, id) {
            if (this.ArrayTag.length < 10)
                this.ArrayTag.push({ nametag: tag, id: id })
            this.taginput = ""

        },
        onDragOver(event) {
            event.preventDefault();
            event.dataTransfer.dropEffect = "copy";
        },
        onDragLeave(event) {
            event.preventDefault();
        },
        onDrop(event) {
            event.preventDefault();

            this.file = event.dataTransfer.files[0];
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
                            console.log("ошиька")
                        }
                        else {
                            this.image.name = this.file.name
                            this.image.url = URL.createObjectURL(this.file)
                            this.droped = true
                            if (img.height / img.width <= 1.5) {
                                this.styleobj.width = '100%'
                                this.styleobj.height = 'auto'
                            } else {
                                this.styleobj.height = '100%'
                                this.styleobj.width = 'auto'
                            }
                        }
                    };
                    img.src = target.result;

                };

                reader.readAsDataURL(this.file); // Преобразуем файл в формат Base64 
            }
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
                            console.log("ошиька")
                        }
                        else {
                            this.image.name = this.file.name
                            this.image.url = URL.createObjectURL(this.file)
                            this.droped = true
                            if (img.height / img.width <= 1.5) {
                                this.styleobj.width = '100%'
                                this.styleobj.height = 'auto'
                            } else {
                                this.styleobj.height = '100%'
                                this.styleobj.width = 'auto'
                            }
                        }
                    };
                    img.src = target.result;

                };

                reader.readAsDataURL(this.file); // Преобразуем файл в формат Base64 

            }
        },
        UploadImg() {
            // console.log(this.ArrayTag.id)
            const bodyFormData = new FormData()
            bodyFormData.append('attachment', this.file)
            bodyFormData.append('title', this.title)
            bodyFormData.append('body', this.body)
            this.ArrayTag.forEach((item) => {
                bodyFormData.append('tag', item.id)
            })
            axios({
                timeoute: 1000,
                method: 'post',
                url: import.meta.env.VITE_BACKEND_URL + `posts`,
                withCredentials: true,
                data: bodyFormData,

                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => {

                    console.log(response)

                })
                .catch(error => {
                    if (error.status != null) {
                        // this.$router.push({
                        //     name: 'homeview',
                        // })
                    }
                    console.log(error.message);
                });
        },
        reset() {
            this.droped = false
            const item = document.getElementById('file')
            item.value = '';
        }
    }
}
</script>