<template>
    <Report v-show="showreport" :showreport="showreport" :reportid="reportid" @showreport=showReport() />
    <div :id="urlstr" class="wrapper__picture" style="position: relative;" v-if="res.length > 0">
        <div id="list" v-if="res.length > 0">
            <div class="column1" v-if="column1.length > 0" :style=style(1) id="column1">
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img class="picture" v-if="el - 1 < this.column1.length"
                        v-bind:src="'../../dist/uploads/attachments/362x/' + this.column1[(el - 1)].attachment"
                        :alt="'img ' + this.column1[(el - 1)].id" @click="goToPicturePost(this.column1[(el - 1)].id)">

                    <button v-show="!this.column1[(el - 1)].is_liked & user.is_verified" id="add" class="button__hov"
                        @click="liked(this.column1[(el - 1)])">
                        <img src="../assets/img/svg/Heart.svg" alt="" style="background: none;">
                    </button>
                    <button id="report" class="button__hov" @click="showReport(this.column1[(el - 1)].id)"><img
                            src="../assets/img/svg/AlertCircle.svg" alt="" style="background: none;"></button>

                    <button v-show="this.column1[(el - 1)].is_liked & user.is_verified" style="background: rgba(177, 167, 63, 1);
border: 2px solid rgba(255, 255, 255, 1)" id="add" class="button__hov" @click="unliked(this.column1[(el - 1)])">
                        <img src="../assets/img/svg/Heartwhite.svg" alt="" style="background: none;">
                    </button>


                    <button v-show="!this.column1[(el - 1)].is_editable" id="download" class="button__hov">
                        <a download :download="this.column1[(el - 1)].name"
                            :href="'../../dist/uploads/attachments/original/' + this.column1[(el - 1)].attachment"
                            title="ImageName">
                            <img src="../assets/img/svg/downloadmini.svg" alt="" style="background: none;">
                        </a>
                    </button>

                    <button v-show="this.column1[(el - 1)].is_editable" id="download" class="button__hov"
                        @click="goToEdit(this.column1[(el - 1)].id)">
                        <img src="../assets/img/svg/Edit.svg" alt="" style="background: none;">
                    </button>
                    <button v-show="user.is_moderator" @click="deletePost((this.column1[(el - 1)]))" id="delete"
                        class="button__hov"><img src="../assets/img/svg/Trash.svg" alt=""
                            style="background: none;"></button>
                </div>
            </div>
            <div id="column2" class="column2" :style=style(2) v-if="column2.length > 0 & this.k >= 2">
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img class="picture" v-if="el - 1 < this.column2.length"
                        v-bind:src="'../../dist/uploads/attachments/362x/' + this.column2[(el - 1)].attachment"
                        :alt="'img ' + this.column2[(el - 1)].id" @click="goToPicturePost(this.column2[(el - 1)].id)">
                    <div v-if="el - 1 < this.column2.length">
                        <button v-show="!this.column2[(el - 1)].is_editable" id="download" class="button__hov">
                            <a download :download="this.column2[(el - 1)].name"
                                :href="'../../dist/uploads/attachments/original/' + this.column2[(el - 1)].attachment"
                                title="ImageName">
                                <img src="../assets/img/svg/downloadmini.svg" alt="" style="background: none;">
                            </a>
                        </button>
                        <button id="report" class="button__hov" @click="showReport(this.column2[(el - 1)].id)"><img
                                src="../assets/img/svg/AlertCircle.svg" alt="" style="background: none;"></button>
                        <button v-show="!this.column2[(el - 1)].is_liked & user.is_verified" id="add"
                            class="button__hov" @click="liked(this.column2[(el - 1)])">
                            <img src="../assets/img/svg/Heart.svg" alt="" style="background: none;">
                        </button>

                        <button v-show="this.column2[(el - 1)].is_liked & user.is_verified" style="background: rgba(177, 167, 63, 1);
border: 2px solid rgba(255, 255, 255, 1)" id="add" class="button__hov" @click="unliked(this.column2[(el - 1)])">
                            <img src="../assets/img/svg/Heartwhite.svg" alt="" style="background: none;">
                        </button>
                        <button v-show="this.column2[(el - 1)].is_editable" id="download" class="button__hov"
                            @click="goToEdit(this.column2[(el - 1)].id)">
                            <img src="../assets/img/svg/Edit.svg" alt="" style="background: none;">
                        </button>
                        <button v-show="user.is_moderator" @click="deletePost((this.column2[(el - 1)]))" id="delete"
                            class="button__hov"><img src="../assets/img/svg/Trash.svg" alt=""
                                style="background: none;"></button>
                    </div>
                </div>
            </div>
            <div id="column3" class="column3" :style=style(3) v-if="column3.length > 0 & this.k >= 3">
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img class="picture" v-if="el - 1 < this.column3.length"
                        v-bind:src="'../../dist/uploads/attachments/362x/' + this.column3[(el - 1)].attachment"
                        :alt="'img ' + this.column3[(el - 1)].id" @click="goToPicturePost(this.column3[(el - 1)].id)">
                    <div v-if="el - 1 < this.column3.length">
                        <button v-show="!this.column3[(el - 1)].is_editable" id="download" class="button__hov">
                            <a download :download="this.column3[(el - 1)].name"
                                :href="'../../dist/uploads/attachments/original/' + this.column3[(el - 1)].attachment"
                                title="ImageName">
                                <img src="../assets/img/svg/downloadmini.svg" alt="" style="background: none;">
                            </a>
                        </button>
                        <button id="report" class="button__hov" @click="showReport(this.column3[(el - 1)].id)"><img
                                src="../assets/img/svg/AlertCircle.svg" alt="" style="background: none;"></button>

                        <button v-show="!this.column3[(el - 1)].is_liked & user.is_verified" id="add"
                            class="button__hov" @click="liked(this.column3[(el - 1)])">
                            <img src="../assets/img/svg/Heart.svg" alt="" style="background: none;">
                        </button>

                        <button v-show="this.column3[(el - 1)].is_liked & user.is_verified" style="background: rgba(177, 167, 63, 1);
border: 2px solid rgba(255, 255, 255, 1)" id="add" class="button__hov" @click="unliked(this.column3[(el - 1)])">
                            <img src="../assets/img/svg/Heartwhite.svg" alt="" style="background: none;">
                        </button>
                        <button v-show="this.column3[(el - 1)].is_editable" id="download" class="button__hov"
                            @click="goToEdit(this.column3[(el - 1)].id)">
                            <img src="../assets/img/svg/Edit.svg" alt="" style="background: none;">
                        </button>
                        <button v-show="user.is_moderator" @click="deletePost((this.column3[(el - 1)]))" id="delete"
                            class="button__hov"><img src="../assets/img/svg/Trash.svg" alt=""
                                style="background: none;"></button>
                    </div>
                </div>
            </div>
            <div id="column4" class="column4" :style=style(4) v-if="column4.length > 0 & this.k >= 4">
                <div v-for="(el, index) in this.countImg" :key="index" className="item">
                    <img class="picture" v-if="el - 1 < this.column4.length"
                        v-bind:src="'../../dist/uploads/attachments/362x/' + this.column4[(el - 1)].attachment"
                        :alt="'img ' + this.column4[(el - 1)].id" @click="goToPicturePost(this.column4[(el - 1)].id)">
                    <div v-if="el - 1 < this.column4.length">
                        <button v-show="!this.column4[(el - 1)].is_editable" id="download" class="button__hov">
                            <a download :download="this.column4[(el - 1)].name"
                                :href="'../../dist/uploads/attachments/original/' + this.column4[(el - 1)].attachment"
                                title="ImageName">
                                <img src="../assets/img/svg/downloadmini.svg" alt="" style="background: none;">
                            </a>
                        </button>
                        <button id="report" class="button__hov" @click="showReport(this.column4[(el - 1)].id)"><img
                                src="../assets/img/svg/AlertCircle.svg" alt="" style="background: none;"></button>
                        <button v-show="!this.column4[(el - 1)].is_liked & user.is_verified" id="add"
                            class="button__hov" @click="liked(this.column4[(el - 1)])">
                            <img src="../assets/img/svg/Heart.svg" alt="" style="background: none;">
                        </button>

                        <button v-show="this.column4[(el - 1)].is_liked & user.is_verified" style="background: rgba(177, 167, 63, 1);
border: 2px solid rgba(255, 255, 255, 1)" id="add" class="button__hov" @click="unliked(this.column4[(el - 1)])">
                            <img src="../assets/img/svg/Heartwhite.svg" alt="" style="background: none;">
                        </button>
                        <button v-show="this.column4[(el - 1)].is_editable" id="download" class="button__hov"
                            @click="goToEdit(this.column4[(el - 1)].id)">
                            <img src="../assets/img/svg/Edit.svg" alt="" style="background: none;">
                        </button>

                        <button v-show="user.is_moderator" id="delete" @click="deletePost((this.column4[(el - 1)]))"
                            class="button__hov"><img src="../assets/img/svg/Trash.svg" alt=""
                                style="background: none;"></button>
                    </div>
                </div>
            </div>

        </div>

        <div v-if="verticalScroll >= 200 & res.length > 5" class="go_top" :style="styletop()">
            <button @click="goToUp">
                <img src="../assets/img/svg/Arrowup.svg" alt="">
            </button>
        </div>
    </div>
</template>

<script>

import axios from 'axios';
import Report from './Report.vue';

// const config = dotenv.config()
export default {
    components: { Report },
    data() {
        return {
            reportid: 1,
            verticalScroll: 0,
            showreport: false,
            column1: [],
            column2: [],
            column3: [],
            column4: [],
            column5: [],
            pushin: 0,
            user: {},
            loadstop: true,
            page: 1,
            countImg: 4,
            newmas: this.res,
            k: 4,
            window: {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight
            }

        }

    },
    props: {
        res: Object,
        urlstr: String,
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
            this.page = 1
            this.loadstop = true
            this.createColumn();

        },
        countImg() {


            // if (this.countImg > 4 & this.loadstop & this.res.length == 20)
            if (this.countImg > 4 & this.loadstop & this.res.length == 20)
                axios({
                    timeoute: 1000,
                    method: 'get',
                    url: import.meta.env.VITE_BACKEND_URL + `${this.urlstr}?start=${(this.page) * 20}&end=${(this.page + 1) * 20}`,

                    withCredentials: true,
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(response => {
                        // this.result = response.data.items

                        this.columnadd(response.data.items)
                        if (response.data.count == 20) {
                            this.page++
                        }
                        else {
                            this.loadstop = false
                        }
                    })
                    .catch(error => {
                        console.log(error.message);
                    });
        }
    },
    mounted() {
        axios({
            timeoute: 1000,
            method: 'get',
            url: import.meta.env.VITE_BACKEND_URL + `users/current`,

            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                this.user = response.data
            })
            .catch(error => {
                console.log(error.message);
            });


        window.addEventListener('scroll', () => {
            const documentReact = document.documentElement.getBoundingClientRect();
            this.verticalScroll = window.scrollY;

            let documentimg1 = document.getElementById('column1');
            let documentimg2 = document.getElementById('column2');
            let documentimg3 = document.getElementById('column3');
            let documentimg4 = document.getElementById('column4');
            if (!documentimg1 || !documentimg2 || !documentimg3 || !documentimg4) {
                return
            }
            let heightMin = Math.min(documentimg1.lastElementChild.getBoundingClientRect().bottom, documentimg2.lastElementChild.getBoundingClientRect().bottom,
                documentimg3.lastElementChild.getBoundingClientRect().bottom, documentimg4.lastElementChild.getBoundingClientRect().bottom);


            // console.log(heightMin, document.documentElement.clientHeight)
            // this.style()
            if (heightMin < document.documentElement.clientHeight + 300) {

                if (this.countImg + 4 < this.column1.length) {
                    this.countImg += 4
                }
                else {
                    this.countImg = Math.ceil(this.column1.length)
                }
            }

        })

        setTimeout(() => {
            this.handleResize()
        }, 100);
    },


    methods: {
        columnpush(column, start, end, res) {
            for (let index = start; index < end; index++) {


                column.push(res[index]);
            }


            // return column
        },

        columnadd(res) {

            let count = Math.floor(res.length / this.k)
            if (this.k > 0) {

                this.columnpush(this.column1, 0, count, res)
                if (this.k > 1) {
                    this.columnpush(this.column2, count, 2 * count, res)
                    if (this.k > 2) {
                        this.columnpush(this.column3, 2 * count, 3 * count, res)
                        if (this.k > 3) {
                            this.columnpush(this.column4, 3 * count, 4 * count, res)
                        }
                    }
                }
            }

            if (count * this.k != res.length) {

                let ostatok = res.length - count * this.k
                while (ostatok > 0) {
                    if (this.pushin == 0 & this.pushin + 1 <= this.k) {
                        this.columnpush(this.column1, res.length - ostatok, res.length - ostatok + 1, res)
                        ostatok--
                        this.pushin++

                    }
                    else if (this.pushin == 1 & this.pushin + 1 <= this.k) {
                        this.columnpush(this.column2, res.length - ostatok, res.length - ostatok + 1, res)

                        ostatok--
                        this.pushin++

                    }
                    else if (this.pushin == 2 & this.pushin + 1 <= this.k) {
                        this.columnpush(this.column3, res.length - ostatok, res.length - ostatok + 1, res)

                        ostatok--
                        this.pushin++

                    }
                    else if (this.pushin == 3 & this.pushin + 1 <= this.k) {
                        this.columnpush(this.column4, res.length - ostatok, res.length - ostatok + 1, res)

                        ostatok--
                        this.pushin = 0

                    }
                    if (this.pushin + 1 > this.k) {
                        this.pushin = 0
                    }



                }
            }
        },
        createColumn() {
            if (this.res)
                if (this.res.length < 16) {
                    this.countImg = Math.ceil(this.res.length / this.k)
                }
                else if (this.res.length >= 16) {
                    this.countImg = 4
                }
            let count = Math.floor(this.res.length / this.k)

            this.column1 = []
            this.column2 = []
            this.column3 = []
            this.column4 = []

            if (this.k > 0) {

                this.columnpush(this.column1, 0, count, this.res)
                if (this.k > 1) {
                    this.columnpush(this.column2, count, 2 * count, this.res)
                    if (this.k > 2) {
                        this.columnpush(this.column3, 2 * count, 3 * count, this.res)
                        if (this.k > 3) {
                            this.columnpush(this.column4, 3 * count, 4 * count, this.res)
                        }
                    }
                }
            }

            if (count * this.k != this.res.length) {

                let ostatok = this.res.length - count * this.k
                while (ostatok > 0) {
                    if (this.pushin == 0 & this.pushin + 1 <= this.k) {
                        this.columnpush(this.column1, this.res.length - ostatok, this.res.length - ostatok + 1, this.res)

                        ostatok--
                        this.pushin++

                    }
                    else if (this.pushin == 1 & this.pushin + 1 <= this.k) {
                        this.columnpush(this.column2, this.res.length - ostatok, this.res.length - ostatok + 1, this.res)

                        ostatok--
                        this.pushin++

                    }
                    else if (this.pushin == 2 & this.pushin + 1 <= this.k) {
                        this.columnpush(this.column3, this.res.length - ostatok, this.res.length - ostatok + 1, this.res)
                        ostatok--
                        this.pushin++

                    }
                    else if (this.pushin == 3 & this.pushin + 1 <= this.k) {
                        this.columnpush(this.column4, this.res.length - ostatok, this.res.length - ostatok + 1, this.res)
                        ostatok--
                        this.pushin = 0

                    }
                    if (this.pushin + 1 > this.k) {
                        this.pushin = 0
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
        goToPicturePost(id) {
            // let route = this.$router.push({ name: 'postview', params: { id: id } });
            window.open(`/post/${id}`, '_blank');


        },
        goToEdit(id) {
            this.$router.push({ name: 'uploadimgview', query: { id: id } })
        },
        style(key) {

            let styleobj = {
            }
            if (key == this.k) {
                styleobj.marginRight = 0
            }
            return styleobj
        },
        styletop() {
            let styleobj = {
            }
            // var h = 5000
            var h = document.getElementById(this.urlstr);
            if (h) {
                if (this.window.height - 200 - h.getBoundingClientRect().top > h.clientHeight)
                    styleobj.bottom = '-80px'
                else {
                    styleobj.top = this.window.height - 200 - h.getBoundingClientRect().top + 'px'
                }
            }
            return styleobj
        },
        goToUp() {
            scroll({
                top: 0,
                behavior: "smooth"
            });
        },
        liked(column) {
            axios({
                timeoute: 1000,
                method: 'post',
                url: (import.meta.env.VITE_BACKEND_URL + `likes/posts/${column.id}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {

                    column.is_liked = true

                })
                .catch(error => {
                    console.log(error)
                });
        },
        unliked(column) {
            axios({
                timeoute: 1000,
                method: 'delete',
                url: (import.meta.env.VITE_BACKEND_URL + `likes/posts/${column.id}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {

                    column.is_liked = false

                })
                .catch(error => {
                    console.log(error)
                });
        },
        deletePost(column) {
            axios({
                timeoute: 1000,
                method: 'delete',
                url: (import.meta.env.VITE_BACKEND_URL + `posts/${column.id}`),
                withCredentials: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    window.location.reload();

                })
                .catch(error => {
                    console.log(error)
                });
        },
        showReport(id) {
            this.showreport = !this.showreport
            this.reportid = id
        }
    }

}

</script>

<style scoped>
button {
    cursor: pointer;
}

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
    padding: 10px;
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
    top: 10px;
    left: 10px;
    background: rgba(189, 38, 38, 1);

}

#delete {
    position: absolute;
    bottom: 10px;
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

.go_top {
    position: absolute;
    /* bottom: 20px; */
    right: 0;
    z-index: 500;

}

.go_top button {
    width: 80px;
    height: 80px;
    border: 0;
    border-radius: 50%;
    background: rgba(177, 167, 63, 1);
}
</style>