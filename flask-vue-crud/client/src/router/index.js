import Vue from 'vue';
import Router from 'vue-router';
import Healthcheck from '@/components/Health';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Healthcheck',
      component: Healthcheck,
    },
  ],
});
