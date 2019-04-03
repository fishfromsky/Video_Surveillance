import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import login from '@/components/login'
import statistic_chart from '@/components/statistic_chart'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/statistic_chart',
      name: 'statistic_chart',
      component: statistic_chart
    },
  ]
})
