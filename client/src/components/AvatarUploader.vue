<template>
    <input ref="input" type="file" name="image" accept="image/*" @change="setImage" />
    <div class="content">
        <div class="img-cropper">
            <vue-cropper style="height: 300px; width: 300px;" ref="cropper" :view-mode="1" :auto-crop-area="1"
                :aspect-ratio="1" :src="imgSrc" />
        </div>
        <div class="btn__wrap">
            <button style="width: 150px;" @click="showFileChooser">Загрузить изображение</button>
            <button @click="SetAvatars">Сохранить</button>
        </div>
        <div class="cropped-image">
            <img v-if="cropImg" :src="cropImg" alt="Cropped Image" />
            <div v-else class="crop-placeholder" />
        </div>
    </div>
</template>

<script>
import VueCropper from 'vue-cropperjs';
import 'cropperjs/dist/cropper.css';

import axios from 'axios';

export default {
    components: {
        VueCropper,
    },
    data() {
        return {
            imgSrc: `../../dist/uploads/avatars/original/${this.avatar}`,
            cropImg: '',
        };
    },
    props: {
        avatar: String,
    },
    methods: {
        cropImage() {
            // get image data for post processing, e.g. upload or setting image src
            this.cropImg = this.$refs.cropper.getCroppedCanvas().toDataURL();
        },
        setImage(e) {
            const file = e.target.files[0];

            if (file.type.indexOf('image/') === -1) {
                alert('Please select an image file');
                return;
            }

            if (typeof FileReader === 'function') {
                const reader = new FileReader();

                reader.onload = (event) => {
                    this.imgSrc = event.target.result;
                    // rebuild cropperjs with the updated source
                    this.$refs.cropper.replace(event.target.result);
                };

                reader.readAsDataURL(file);
            } else {
                alert('Sorry, FileReader API not supported');
            }
        },
        showFileChooser() {
            this.$refs.input.click();
        },
        SetAvatars() {
            // img = base64_decode(this.$refs.cropper.getCroppedCanvas().toDataURL());
            let byteString = atob(this.$refs.cropper.getCroppedCanvas().toDataURL().split(',')[1]);
            // Определить MIME-тип из Data URI
            let mimeString = this.$refs.cropper.getCroppedCanvas().toDataURL().split(',')[0].split(':')[1].split(';')[0];
            // Формируем массив бинарных данных
            let ia = new Uint8Array(byteString.length);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            // Создаем файл из блоба
            let file = new File([ia], 'avatar', { type: mimeString });

            axios({
                timeoute: 1000,
                method: 'post',
                url: import.meta.env.VITE_BACKEND_URL + 'users/current/avatar',
                data: { image: file },
                withCredentials: true,
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => {
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
                });
        },
    },
};
</script>

<style>
.cropper-view-box {
  display: block;
  height: 100%;
  outline: 1px solid #b1a73f !important;
  outline-color: #b1a73f !important;
  overflow: hidden;
  width: 100%;
}

.cropper-line {
  background-color: #b1a73f !important;
}

.cropper-point {
  background-color: #b1a73f !important;
  height: 5px;
  opacity: 0.75;
  width: 5px;
}
</style>

<style scoped>
input[type="file"] {
    display: none;
}

.img-cropper {
    height: 300px;
    width: 300px;
}

.content {
    display: flex;
    flex-wrap: wrap;
    width: 300px;
    /* justify-content: space-between; */
}

.cropper-area {
    width: 614px;
}

.actions {
    margin-top: 1rem;
}

.cropped-image {
    height: 100px;
    width: 100px;
}

.cropped-image img {
    border-radius: 50%;
    max-width: 100%;
}

.btn__wrap {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    width: 300px;
    justify-content: space-between;
}

button {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: center;
    color: rgba(71, 67, 25, 1);
    width: 100px;
    height: 50px;
    border-radius: 30px;
    border: 4px solid rgba(177, 167, 63, 1)
}

button:active {
    transform: scale(0.9);
}
</style>