import Vue from 'vue';
import Router from 'vue-router';
import Healthcheck from '@/components/Health';
import Advices from '@/components/Advices';

Vue.use(Router);

export default new Router({
  // below mode needed to get rid of shebang symbol in url, like localhost/#/healthcheck
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Advice',
      component: Advices,
    },
    {
      path: '/healthcheck',
      name: 'Healthcheck',
      component: Healthcheck,
    },
  ],
});
