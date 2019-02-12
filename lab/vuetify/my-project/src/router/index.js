import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

// 非登录页的包裹组件
const Layout = resolve => require(['@/views/Layout'], resolve)

// 小工具
const Menu = resolve => require(['@/views/Menu'], resolve)

Vue.use(Router)

const router = new Router({
  routes: [{
    path: '/',
    meta: {
      requireAuth: true
    },
    component: Layout,
    // redirect: '/project-info', // 重定向到第一个子路由，否则只渲染Layout组件，这块儿使用时解除注释
    // redirect: '/signin', // 这里重定向到登录页面，是为了展示使用，实际用这个项目开发时，需要注释这行，解除上一行的注释
    children: [{
      path: 'menu',
      meta: {
        requireAuth: true
      },
      component: Menu
    }]
  }]
})

export default router
