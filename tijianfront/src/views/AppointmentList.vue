<template>
  <div class="wrapper">
    <header>
      <i class="fa fa-angle-left" onclick="history.go(-1)"></i>
      <p>我的预约</p>
      <div></div>
    </header>
    <div class="top-ban"></div>

    <ul>
      <li v-for="orders in ordersArr" :key="orders.orderId">
        <div class="left" @click="toConfirmOrder(orders)">
          <p>{{orders.orderDate}}</p>
          <p>{{orders.setmeal.name}}</p>
        </div>
        <div class="right" v-if="curDate<orders.orderDate" @click="cancel(orders.orderId)">
          取消预约
        </div>
      </li>
    </ul>

    <div class="bottom-ban"></div>
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
import { reactive, toRefs } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
axios.defaults.baseURL = "http://localhost:8080/tijian/";
import { getSessionStorage, getCurDate } from "../common.js";

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();

    const state = reactive({
      users: getSessionStorage("users"),
      ordersArr: [],
      curDate: getCurDate()
    });

    init();
    function init() {
      axios
        .post("orders/listOrdersByUserId", {
          userId: state.users.userId,
          state: 1
        })
        .then((response) => {
          state.ordersArr = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    }

    function cancel(orderId){
      if(!confirm('确定取消此次预约吗？')){
        return;
      }

      axios
        .post("orders/removeOrders", {
          orderId: orderId
        })
        .then((response) => {
          if(response.data==1){
            init();
          }else{
            alert('取消预约失败！');
          }
        })
        .catch((error) => {
          console.error(error);
        });
    }

    function toConfirmOrder(orders){
      router.push({path:'/confirmOrder',query:{hpId:orders.hpId,smId:orders.smId,selectDay:orders.orderDate}});
    }

    return {
      ...toRefs(state),
      cancel,
      toConfirmOrder
    };
  },
  components: { Footer },
};
</script>

<style scoped>
/*********************** 总容器 ***********************/
.wrapper {
  width: 100%;
  height: 100%;
  background-color: #f9f9f9;
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

/*********************** ul ***********************/
ul {
  width: 86vw;
  margin: 0 auto;
}
ul li {
  width: 100%;
  height: 14vw;
  border-bottom: solid 1px #eee;

  display: flex;
  justify-content: space-between;
  align-items: center;
}
ul li .left {
  user-select: none;
  cursor: pointer;
}
ul li .left p:first-child {
  color: #555;
  font-size: 3.3vw;
}
ul li .left p:last-child {
  color: #333;
  font-size: 4.2vw;
  font-weight: 600;
}
ul li .right {
  font-size: 4vw;
  color: #e6a23c;
}
</style>