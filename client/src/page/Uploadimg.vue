<template>
    <div class="page">
        <HeaderAuth />
        <div class="wrap">
            <div class="drag__drop__wrap">
                <div class="drag__drop">
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
                <div class="input__wrap">
                    <label>Название</label>
                    <textarea class="name" placeholder="Придумайте название"></textarea>
                    <label>Описание</label>
                    <textarea class="description" placeholder="Подробно опишите"></textarea>
                    <label>Альбом</label>
                    <textarea placeholder="Выберите альбом"></textarea>
                    <label>Теги</label>
                    <input autofocus maxlength="30" v-model="taginput" placeholder="Введите тег для поиска"
                        v-on:keyup.enter="addtag(this.taginput)"></input>
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
}

.drag__drop {
    background: rgba(239, 237, 217, 1);

    align-self: flex-start;
    margin-left: 80px;
    width: 420px;
    height: 600px;
    width: 420px;

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
</style>

<script>

import HeaderAuth from '@/components/HeaderAuth.vue';
import Bottom from "../components/Bottom.vue";
import AddTag from '@/components/AddTag.vue';
export default {
    components: { HeaderAuth, Bottom, AddTag },
    data() {
        return {
            taginput: "",
            tag: "",
            ArrayTag: [],
        }

    },
    methods: {
        addtag(tag) {
            if (this.ArrayTag.length < 10)
                this.ArrayTag.push({ nametag: tag })
        }
    }
}
</script>