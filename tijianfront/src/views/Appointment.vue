<template>
  <div class="wrapper">
    <header>
      <i class="fa fa-angle-left" onclick="history.go(-1)"></i>
      <p>用户体检预约</p>
      <div></div>
    </header>
    <div class="top-ban"></div>

    <section>
      <img src="../assets/yuyue.png" />
      
      <p>
        <img src="../assets/benrenyuyue.png" @click="toHospital" /><!-- 此处是一个事件，当用户点击图片时跳转到医院 -->
        <img src="../assets/jiashuyuyue.png" />
      </p>
    </section>

    <div class="bottom-ban"></div>

    <Footer></Footer>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import Footer from "../components/Footer.vue";
import axios from "axios";
axios.defaults.baseURL = "http://localhost:8080/tijian/";
import { getSessionStorage } from "../common.js";//导入自己的js文件，从数据库中获取

export default {
  setup() {
    const router = useRouter();

//这是刚刚那个事件的方法tohospital
    function toHospital() {
      axios
        .post("orders/getOrdersByUserId", {
          userId: getSessionStorage('users').userId//获取users对象，也就是取出user的ID
        })
        //判断是否预约
        .then((response) => {
          if(response.data>=1){
            alert('已经预约了！');
          }else{
            router.push('/hospital');//进入到下一个主键
          }
        })
        .catch((error) => {
          console.error(error);
        });
    }

    return {
      toHospital,
    };
  },
  components: {
    Footer,
  },
};
</script>

<style scoped>
/*********************** 总容器 ***********************/
.wrapper {
  width: 100%;
  height: 100%;
}

/*********************** header ***********************/
header {
  width: 100%;
  height: 15.7vw;
  background-color: #fff;

  position: fixed;
  left: 0;
  top: 0;

  display: flex;
  align-items: center;
  justify-content: space-between;

  box-sizing: border-box;
  padding: 0 3.6vw;
}
header .fa {
  font-size: 8vw;
}

/*********************** common样式 ***********************/
.top-ban {
  width: 100%;
  height: 15.7vw;
}
.bottom-ban {
  width: 100%;
  height: 14.2vw;
}

/*********************** section ***********************/
section {
  width: 100%;
}
section img {
  width: 100vw;
}
section p {
  box-sizing: border-box;
  padding: 0 3.6vw;
  margin-top: 10vw;

  display: flex;
  justify-content: space-between;
}
section p img {
  width: 44vw;
  border-radius: 1.6vw;
  display: block;
  cursor: pointer;
}
</style>