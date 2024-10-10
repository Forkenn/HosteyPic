<template>

  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>main screen</title>

  </head>

  <body>
    <div v-if="show" >
        <Login @show_ch='show_login' @login="log_login"/>
        <div class="gray" @click=show_login(true)></div>
    </div>

    <div class="page">



      <header class="header">
        <div class="wrapper__header">
          <div class="header__logo">
            <a href="/" class="header__logo-link">

              <p> <span class="color__white">Hostey</span>
                <span class="color__black">PIC</span>
              </p>
            </a>
          </div>
          <div class="user__icon" v-on:click=show_login()>
            <img src="../src/assets/img/svg/userIcon.svg" alt="">
          </div>
        </div>
      </header>


      <div class="wrapper__searchbar">
        <div class="searchbar">
          <div class="input">
            <input v-model="serach" v-on:keyup.enter="printInformation" placeholder="Type here for search..." id="idSearch">
          </div>
          <div class="searchbar__icon">
                
            <img  src="../src/assets/img/svg/searchicon.svg" @click="printInformation" alt="">
          </div>
        </div>
      </div>
      
      <Searchimg  :res="result"/>

      


      <div class="bottom">
        <div class="wrapper__bottom">
          <p> <span class="bot">
            asd
          </span></p>
        </div>
      </div>
    </div>

    
  </body>
</template>

<style scoped></style>


<script>

import Searchimg from "./components/Searchimg.vue"
import Login from "./components/Login.vue"

const data = ['searchicon.svg', 'userIcon.svg', 'logo.svg']

export default { 
  components: {Searchimg, Login},
      data() { 
        return { 
          show: false,
            serach: "", 
            result:[],
            tag:"123",
            srcimg:""
        }; 
      }, 
      methods: { 
        show_login(show){
          if(show){
            this.show=false
          }
          else{
            this.show=true
          }
          
        },
        printInformation() { 
          this.result = []
          for (let index = 0; index < this.serach; index++) {
            this.srcimg = data[index%3],
            this.result.push({
              src1 : this.srcimg,
              tag : this.tag
            })
          }
          
        }, 
        log_login(data){
          console.log(data)
        },
        onEnter: function() {
          console.log(this.serach);
        },
        
      }, 
    };


</script>