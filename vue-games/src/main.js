import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap"

import axios from 'axios';
import VueAxios from 'vue-axios';

import { createApp } from 'vue';
import router from './router';

import App from './App.vue';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const app = createApp(App);

app.use(router);
app.use(VueAxios, axios);

app.mount('#app');
