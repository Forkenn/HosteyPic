<template>
    <body>
        
    
    <div class="wrapper_login" >
        
            <form>
                <label>
                   Username:
                </label>
                <input v-model="Username" type="text" 
                    placeholder="Enter your Username" required>

                <label v-if="show">
                    e-mail:
                </label>
                <input  v-if="show" v-model="e_mail" type="text"
                    placeholder="Enter your e-mail" required>

                

                <label>
                    Password:
                </label>
                <input v-model="Password" type="password"
                    placeholder="Enter your Password" required>
                <label v-if="show">
                    Confirm password:
                </label>
                <input v-if="show" v-model="confirm_password" type="password" 
                    placeholder="Confirm  your password" required>

                  
                  <div v-if="!show" class="wrap">
                        <button type="button" @click=printinfo2()>
                              Log in
                        </button>
                  </div>
                  <div class="wrap">
                    <div v-if="!show"class="line"></div>
                  </div>
                  <div class="wrap" v-if="show" >
                        <button type="button" @click=printinfo() >
                              Sign in
                        </button>
                    </div>
                    <div v-else class="wrap"  >
                        <button type="button" @click=change_show() >
                              Sign in
                        </button>
                    </div>
                  
            </form>

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
    src : url('../assets/fonts/chewy-v18-latin-regular.woff2') format('woff2');
    /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
}

body {
 
    
    font-family: Chewy;
    font-size: 32px;
    font-weight: 400;
    line-height: 41.81px;
    text-align: left;


    display: flex;
    align-items: center;
    justify-content: center;
    background: #f3f3f3;
    flex-direction: column;
    margin: 0;
    
}

.wrapper_login {
    position: fixed;
    left: 50%;

    top: 50%;
    transform:translate(-50%,-50%);
    

    z-index: 200;
    background-color: #EFEDD9;
    border-radius: 50px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
    padding: 10px 20px;
    transition: transform 0.2s;
    width: 1000px;
    /* height: 685px; */
    text-align: center;
    justify-content: center;
}

h1 {
    color: #4CAF50;
}

label {
    display: block;
    width: 100%;
    margin-top: 10px;
    margin-bottom: 5px;
    text-align: center;
    color: #474319;
    font-weight: bold;
}


input {
    font-family: Chewy;
    font-size: 16px;
    font-weight: 400;
    line-height: 41.81px;
    text-align: left;

    width: 875px;
    height: 40px;
    gap: 0px;
    border-radius: 15px;
    border: 2px 0px 0px 0px;
    opacity: 0px;

    
}

button {
    font-family: Chewy;
    font-size: 48px;
    font-weight: 400;
    line-height: 41.81px;
    text-align: center;

    border-radius: 10px;
    margin-top: 15px;
    margin-bottom: 15px;
    
    border: 4px solid #B1A73F;

    color: #474319;
    cursor: pointer;
    
    border-radius: 30px;
    width: 300px;
    height: 104px;
}
.line{
    width: 900px;
    height: 0px;
    text-align: center;
    gap: 0px;
    border: 2px solid #B1A73F;
    opacity: 0px;

}
.wrap {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style >

<script>

export default{
    data(){
        return{
            Username : "",
            Password : "",
            confirm_password :"",
            e_mail : "",
            show : false,
            hiedth : "350px"
        }
    },
    methods:{
        change_show(){
        if(this.show){
            this.show=false
          }
          else{
            this.show=true
          }
    },
    printinfo(){
        this.$emit('login', {
      email: this.e_mail,
      Username : this.Username,
      Password: this.Password
    })
    this.$emit('show_ch', true)

        },
        printinfo2(){
            this.$emit('show_ch', true)
        this.$emit('login', {
      Username : this.Username,
      Password: this.Password
      
    })
}
    },
    
}


</script>