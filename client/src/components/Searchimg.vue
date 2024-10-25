<template>

    <div class="wrapper__picture">
        <div id="list" v-if="res.length > 0">

            <div class="column1" :style=style(1)>
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img class="picture" v-bind:src="'../../dist/uploads/' + this.column1[(el - 1)].src1"
                        :alt="'img ' + el">
                    <button id="download" class="button__hov"><img src="../assets/img/svg/downloadmini.svg" alt=""
                            style="background: none;"></button>
                    <button id="add" class="button__hov"><img src="../assets/img/svg/Plus.svg" alt=""
                            style="background: none;"></button>
                    <button id="report" class="button__hov"><img src="../assets/img/svg/AlertCircle.svg" alt=""
                            style="background: none;"></button>
                    <button id="delete" class="button__hov"><img src="../assets/img/svg/Trash.svg" alt=""
                            style="background: none;"></button>
                </div>
            </div>
            <div class="column2" :style=style(2) v-if="column2.length > 0 & this.k >= 2">
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img class="picture" v-if="el - 1 < this.column2.length"
                        v-bind:src="'../../dist/uploads/' + this.column2[(el - 1)].src1"
                        :alt="'img ' + this.countImg * 2">
                    <button id="download" class="button__hov"><img src="../assets/img/svg/downloadmini.svg" alt=""
                            style="background: none;"></button>
                    <button id="add" class="button__hov"><img src="../assets/img/svg/Plus.svg" alt=""
                            style="background: none;"></button>
                    <button id="report" class="button__hov"><img src="../assets/img/svg/AlertCircle.svg" alt=""
                            style="background: none;"></button>
                    <button id="delete" class="button__hov"><img src="../assets/img/svg/Trash.svg" alt=""
                            style="background: none;"></button>
                </div>
            </div>
            <div class="column3" :style=style(3) v-if="column3.length > 0 & this.k >= 3">
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img class="picture" v-if="el - 1 < this.column3.length"
                        v-bind:src="'../../dist/uploads/' + this.column3[(el - 1)].src1"
                        :alt="'img ' + this.countImg * 3">
                    <button id="download" class="button__hov"><img src="../assets/img/svg/downloadmini.svg" alt=""
                            style="background: none;"></button>
                    <button id="add" class="button__hov"><img src="../assets/img/svg/Plus.svg" alt=""
                            style="background: none;"></button>
                    <button id="report" class="button__hov"><img src="../assets/img/svg/AlertCircle.svg" alt=""
                            style="background: none;"></button>
                    <button id="delete" class="button__hov"><img src="../assets/img/svg/Trash.svg" alt=""
                            style="background: none;"></button>
                </div>
            </div>
            <div class="column4" :style=style(4) v-if="column4.length > 0 & this.k >= 4">
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img class="picture" v-if="el - 1 < this.column4.length"
                        v-bind:src="'../../dist/uploads/' + this.column4[(el - 1)].src1"
                        :alt="'img ' + this.countImg * 4">
                    <button id="download" class="button__hov"><img src="../assets/img/svg/downloadmini.svg" alt=""
                            style="background: none;"></button>
                    <button id="add" class="button__hov"><img src="../assets/img/svg/Plus.svg" alt=""
                            style="background: none;"></button>
                    <button id="report" class="button__hov"><img src="../assets/img/svg/AlertCircle.svg" alt=""
                            style="background: none;"></button>
                    <button id="delete" class="button__hov"><img src="../assets/img/svg/Trash.svg" alt=""
                            style="background: none;"></button>
                </div>
            </div>
            <div class="column5" v-if="column5.length > 0 & this.k == 5">
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img v-if="el - 1 < this.column5.length"
                        v-bind:src="'../../dist/uploads/' + this.column5[(el - 1)].src1"
                        :alt="'img ' + this.countImg * 5">
                </div>
            </div>

        </div>
    </div>
</template>

<script>



export default {
    data() {
        return {

            column1: [],
            column2: [],
            column3: [],
            column4: [],
            column5: [],

            countImg: 4,
            newmas: this.res,
            k: 5,
            window: {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight
            }

        }

    },
    props: {
        res: Object,

    },

    created() {
        if (this.res.length != 0) {

            if (this.countImg > this.res.length)
                this.countImg = this.res.length
        }
        window.addEventListener('resize', this.handleResize)

        this.handleResize();


    },
    watch: {
        res: function (newVal, oldVal) {
            this.createColumn();

        },
        k: function (newVal, oldVal) {
            this.createColumn();

        }
    },
    mounted() {

        window.addEventListener('scroll', () => {
            const documentReact = document.documentElement.getBoundingClientRect();

            if (documentReact.bottom < document.documentElement.clientHeight + 300) {
                if (this.countImg + 4 < this.res.length / this.k) {
                    this.countImg += 4
                }
                else {
                    this.countImg = Math.ceil(this.res.length / this.k)
                }
            }

        })

    },


    methods: {

        createColumn() {
            if (this.res)
                if (this.res.length < 15) {
                    this.countImg = Math.ceil(this.res.length / this.k)
                }
                else if (this.res.length > 15) {
                    this.countImg = 4
                }

            this.column1 = []
            this.column2 = []
            this.column3 = []
            this.column4 = []
            this.column5 = []


            for (let index = 0; index < this.res.length; index++) {
                if (index < (this.res.length - (this.res.length % this.k)) / this.k) {
                    this.column1.push(this.res[index])

                }
                if ((index >= (this.res.length - (this.res.length % this.k)) / this.k) & (index < ((this.res.length - (this.res.length % this.k)) / this.k) * 2)) {
                    this.column2.push(this.res[index])

                }
                if ((index >= ((this.res.length - (this.res.length % this.k)) / this.k) * 2) & (index < ((this.res.length - (this.res.length % this.k)) / this.k) * 3)) {
                    this.column3.push(this.res[index])

                }
                if ((index >= ((this.res.length - (this.res.length % this.k)) / this.k) * 3) & (index < ((this.res.length - (this.res.length % this.k)) / this.k) * 4)) {
                    this.column4.push(this.res[index])
                }
                // if ((index >= ((this.res.length - (this.res.length % this.k)) / this.k) * 4) & (index < ((this.res.length - (this.res.length % this.k)) / this.k) * 5)) {
                //     this.column5.push(this.res[index])
                // }
            }
            if (this.res.length % this.k != 0) {
                for (let index = this.res.length - this.res.length % this.k; index < this.res.length; index++) {
                    if (this.res.length > 5) {
                        if (index % this.k == 0) {
                            this.column1.push(this.res[index - 1])
                        }
                        if (index % this.k == 1 & this.k > 2) {
                            this.column2.push(this.res[index - 1])
                        }
                        if (index % this.k == 2 & this.k > 3) {
                            this.column3.push(this.res[index - 1])
                        }
                        if (index % this.k == 3 & this.k > 4) {
                            this.column4.push(this.res[index - 1])
                        }
                    }
                    else {
                        if (index % this.k == 0) {
                            this.column1.push(this.res[index])
                        }
                        if (index % this.k == 1 & this.k > 2) {
                            this.column2.push(this.res[index])
                        }
                        if (index % this.k == 2 & this.k > 3) {
                            this.column3.push(this.res[index])
                        }
                        if (index % this.k == 3 & this.k > 4) {
                            this.column4.push(this.res[index])
                        }
                    }
                }
            }

        },
        handleResize() {
            this.window.width = document.documentElement.clientWidth;
            this.window.height = document.documentElement.clientHeight;
            this.k = 4;
            if (this.window.width <= 1280) {
                this.k = 1;

                while (this.window.width - 325 * (this.k - 1) - 305 >= 0) {
                    this.k++;
                }
                this.k--;
            }

        },
        style(key) {

            let styleobj = {
            }
            if (key == this.k) {
                styleobj.marginRight = 0
            }
            return styleobj
        },


    }

}

</script>

<style scoped>
.wrapper__picture {


    max-width: 1280px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 75px;
    /* display: flex; */


    margin-bottom: 200px;
}

#list {
    box-sizing: border-box;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-wrap: wrap;

    text-align: justify;
    justify-content: center;




}

.item {
    /* display: inline-block; */
    position: relative;
    margin-bottom: 20px;
    padding: 0;
    /* margin-bottom: 20px; */
    /* height: 200px; */
    min-height: 50px;
    width: 305px;
    /* height: 100%; */
    border-radius: 20px;
    overflow: hidden;

}

.column1,
.column2,
.column3 {
    margin-right: 20px;
}

#list img {
    /* height: 100%; */
    width: 100%;
    height: auto;
    background-color: #deefd9;
    /* border-radius: 20px; */
    display: block;
    transition: transform 400ms ease-in;
}

.button__hov {
    opacity: 0;
    position: absolute;
    z-index: 100;
    border-radius: 50%;
    height: 40px;
    width: 40px;
    border: 0;
    /* transition: opacity 1s ease; */
}

#download {
    position: absolute;
    bottom: 10px;
    right: 10px;
    background: rgba(71, 67, 25, 1);

}

#add {
    position: absolute;
    top: 10px;
    right: 10px;
    background: rgba(71, 67, 25, 1);

}

#report {
    position: absolute;
    bottom: 10px;
    left: 10px;
    background: rgba(189, 38, 38, 1);

}

#delete {
    position: absolute;
    top: 10px;
    left: 10px;
    background: rgba(189, 38, 38, 1);

}

.item:hover .picture {

    overflow: hidden;
    transform: scale(1.15);
}

.item:hover .button__hov {
    opacity: 1;
    /* transition: opacity .35s ease; */
}
</style>