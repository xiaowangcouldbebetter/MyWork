<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>登录</span>
      </div>
    </template>
    <div class="text item">
      <el-form ref="formRef" :model="loginForm" label-width="120px">
        <el-form-item label="医生编码">
          <el-input v-model="loginForm.docCode"></el-input>
        </el-form-item>
        <el-form-item label="登录密码">
          <el-input v-model="loginForm.password" type="password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="login">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </el-card>
</template>

<script>
import { reactive, toRefs } from "vue";
import { useRouter } from "vue-router";
import { setSessionStorage } from "../common.js";
import axios from "axios";
axios.defaults.baseURL = "http://localhost:8088/tijiancms/";

export default {
  setup() {
    const router = useRouter();

    const state = reactive({
      loginForm: {
        docCode: "",
        password: "",
      },
    });

    const login = () => {
      if(state.loginForm.docCode==''){
        alert('医生编码不能为空！');
        return;
      }
      if(state.loginForm.password==''){
        alert('密码不能为空！');
        return;
      }

      axios
        .post("doctor/getDoctorByCodeByPass", state.loginForm)
        .then((response) => {
          let doctor = response.data;
          if (doctor != "") {
            setSessionStorage("doctor", doctor);
            router.push("/ordersList");
          } else {
            alert("医生编码或密码不正确！");
          }
        })
        .catch((error) => {
          console.error(error);
        });
    };

    return {
      ...toRefs(state),
      login,
    };
  },
};
</script>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 400px;
  margin: 0 auto;
  margin-top: 150px;
}
</style>