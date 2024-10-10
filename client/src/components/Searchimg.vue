<template>
    
<div class="wrapper__picture" >
      <div id="list" >
            <div v-for="(el, index) in res" :key="index" className="item"  :style=style(index)>

                <img v-bind:src="'src/assets/img/svg/'+ el.src1" alt="">
            </div>
      </div>
    </div>
</template>

<script>

export default{
    data() {
    return {
        
    k:5,   
    window: {
            width: window.innerWidth,
            height: window.innerHeight
        }
    
    }
    
    },
    props:{
        res: Object,
    },  
    created() {
        window.addEventListener('resize', this.handleResize)
        
        this.handleResize();
        
        
        },

    methods:{
        handleResize() {
            this.window.width = window.innerWidth;
            this.window.height = window.innerHeight;
                this.k = 5
                if (this.window.width < 1280) {
                    this.k = 1;

                while (this.window.width - 270 * this.k + 70 > 0) {
                    this.k++;
                }
                this.k--;
                }
        },
        style(key){
            let styleobj = {

            }
            if ((key + 1) > this.k) {
                styleobj.marginTop ='70px'

            };
            if (this.k!=1){
            if ((key + 1) % this.k == 0 ){
                styleobj.marginRight = 0
            }
            }
            else{
                styleobj.marginLeft = '70px'
            }
            if (key+1 == this.res.length){
                styleobj.marginRight = 0
            }
            return styleobj
        },
        
    }
    
}

</script>

<style scoped>

.wrapper__picture {
    box-sizing: content-box;
    max-width: 1280px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 75px;
    display: flex;
    text-align: center;
    margin-bottom: 200px;
}

#list {
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    text-align: justify;
    justify-content: center;
    
}

.item {

    margin-right: 70px;
    height: 200px;
    width: 200px;
    overflow: hidden;

}



#list img {
    height: 100%;
    width: 100%;
    background-color: #deefd9;

    transition: transform 400ms ease-in;
}



#list img:hover {

    overflow: hidden;
    transform: scale(1.15);
}
</style>