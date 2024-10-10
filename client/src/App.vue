<template>

  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>main screen</title>

  </head>

  <body>
    <div v-if="show" >
        <Login :login1="login" @authorised1="authorised1" @show_ch='show_login' @login="log_login"/>
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
          <div class="user__icon" v-if="authorised" v-on:click="authorised=!authorised">
            <img src="../src/assets/img/svg/userIcon.svg" alt="">
          </div>
          <div class="wrap_login" v-if="!authorised">
            <button class="login" v-on:click="show_login(false),  login=false">
              Вход
            </button>
            <button class="sing_in" v-on:click="show_login(false),  login=true">
              Регистрация
            </button>
          </div>

        </div>
      </header>


      <div class="wrapper__searchbar">
        <div class="searchbar">
          <div class="input">
            <input v-model="serach" v-on:keyup.enter="printInformation" placeholder="Напишите здесь для поиска..." id="idSearch">
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

<style scoped>


@font-face {
    font-display: swap;
    /* Check https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display for other options. */
    font-family: 'Chewy';
    font-style: normal;
    font-weight: 400;
    src : url('./assets/fonts/chewy-v18-latin-regular.woff2') format('woff2');
    /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
}

@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap');

.wrap_login{
  height: 80px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

.login{
  width: 111px;
  height: 46px;
  margin-right: 40px;
  gap: 0px;
  border-radius: 30px 30px 30px 30px;
  border-width: 0px;

  padding: 0px 9px 2px 11px;

  display: flex;
  align-items: center;
  justify-content: center;
  
  color: #474319;

  font-family: Balsamiq Sans;
  font-size: 32px;
  font-weight: 400;
  line-height: 38.4px;
  text-align: center;


}

button.login:active{
  transform: scale(0.90);
}

button.sing_in:active{
  transform: scale(0.90);
}
.sing_in{
  width: 222px;
  height: 46px;
  margin-right: 80px;
  gap: 0px;
  border-radius: 30px 30px 30px 30px;
  border-width: 0px;
  padding: 0px 9px 2px 11px;

  color: #474319;

  font-family: Balsamiq Sans;
  font-size: 32px;
  font-weight: 400;
  line-height: 38.4px;
  text-align: center;


}
</style>


<script>

import Searchimg from "./components/Searchimg.vue"
import Login from "./components/Login.vue"

const data = ['searchicon.svg', 'userIcon.svg', 'logo.svg']

export default { 
  components: {Searchimg, Login},
      data() { 
        return { 
          authorised:false,
          login : true,
          show: false,
            serach: "", 
            result:[],
            data,
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
          this.data=data
          console.log(data)
        },
        authorised1(authorised){
          this.authorised=authorised
        },
        // onEnter: function() {
        //   console.log(this.serach);
        // },
        
      }, 
    };


</script>