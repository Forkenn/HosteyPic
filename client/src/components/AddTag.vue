<template>
    <div class="wrapper__tag" id="wrap">

        <div v-for="(el, index) in ArrayTag" :key="index" className="item">
            <p>{{ el.name }}</p>

            <img class="del_tag" src="../assets/img/svg/X.svg" @click="del_tag(index)">

            </img>
        </div>
    </div>
</template>

<style scoped>
.wrapper__tag {
    box-sizing: content-box;
    width: 100%;
    margin-left: 20px;
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    text-align: center;
    max-height: 300px;
}

.item {
    font-family: Balsamiq Sans;
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: left;


    display: flex;
    max-width: 360px;
    height: 40px;
    align-items: center;
    justify-content: space-between;
    border: 2px solid rgba(177, 167, 63, 1);
    border-radius: 20px;
    background: rgba(239, 237, 217, 1);
    margin-right: 10px;
    margin-bottom: 5px;
    padding-left: 5px;
    padding-right: 5px;
    color: rgba(71, 67, 25, 0.7);

}

.del_tag {
    margin-left: 4px;
}
</style>

<script>


export default {

    data() {
        return {
        }

    },
    props: {
        ArrayTag: Object,
    },
    methods: {

        del_tag(index) {
            this.ArrayTag.splice(index, 1)
        }
    },
}
</script>
