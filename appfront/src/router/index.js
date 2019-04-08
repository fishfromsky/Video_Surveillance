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
      component: home,
      meta: {
        title: '算法配置'
      }
    },
    {
      path: '/',
      name: 'login',
      component: login,
      meta: {
        title: '登录'
      }
    },
    {
      path: '/statistic_chart',
      name: 'statistic_chart',
      component: statistic_chart,
      meta: {
        title: '可视化分析'
      }

    },
  ]
})
