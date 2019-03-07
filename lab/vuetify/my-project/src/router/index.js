import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

// 非登录页的包裹组件
const Layout = resolve => require(['@/views/Layout'], resolve)

// FoodMenu
const FoodMenu = resolve => require(['@/views/Menu'], resolve)

// // FoodMenu
// const MainCourse = resolve => require(['comp/card/MainCourse'], resolve)

// Author
const Author = resolve => require(['@/views/Author'], resolve)

// Log
const Log = resolve => require(['@/views/Log'], resolve)

// ContainerSheets
const ContainerSheets = resolve => require(['comp/container/ContainerSheets'], resolve)

// ContainerGrid
const ContainerGrid = resolve => require(['comp/container/ContainerGrid'], resolve)

// ContainerOriginal
const ContainerOriginal = resolve => require(['comp/container/ContainerOriginal'], resolve)

// ContainerPlugin
const ContainerPlugin = resolve => require(['comp/container/ContainerPlugin'], resolve)

// ContainerList
const ContainerList = resolve => require(['comp/container/ContainerList'], resolve)

// ContainerAvatars
const ContainerAvatars = resolve => require(['comp/container/ContainerAvatars'], resolve)

// ContainerIcon
const ContainerIcon = resolve => require(['comp/container/ContainerIcon'], resolve)

// ContainaerBtn
const ContainerBtn = resolve => require(['comp/container/ContainerBtn'], resolve)

// ContainerWindow
const ContainerWindow = resolve => require(['comp/container/ContainerWindow'], resolve)

// ContainaerTable
const ContainaerTable = resolve => require(['comp/container/ContainaerTable'], resolve)

Vue.use(Router)

const router = new Router({
  routes: [
    {
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
        component: FoodMenu
      }]
    },
    {
      path: '/about',
      meta: {
        requireAuth: true
      },
      component: Layout,
      // redirect: '/project-info', // 重定向到第一个子路由，否则只渲染Layout组件，这块儿使用时解除注释
      // redirect: '/signin', // 这里重定向到登录页面，是为了展示使用，实际用这个项目开发时，需要注释这行，解除上一行的注释
      children: [
        {
          path: 'author',
          meta: {
            requireAuth: true
          },
          component: Author
        },
        {
          path: 'log',
          meta: {
            requireAuth: true
          },
          component: Log
        }
      ]
    },
    {
      path: '/api',
      meta: {
        requireAuth: true
      },
      component: Layout,
      // redirect: '/project-info', // 重定向到第一个子路由，否则只渲染Layout组件，这块儿使用时解除注释
      // redirect: '/signin', // 这里重定向到登录页面，是为了展示使用，实际用这个项目开发时，需要注释这行，解除上一行的注释
      children: [
        {
          path: 'original',
          meta: {
            requireAuth: true
          },
          component: ContainerOriginal
        },
        {
          path: 'plugin',
          meta: {
            requireAuth: true
          },
          component: ContainerPlugin
        },
        {
          path: 'icon',
          meta: {
            requireAuth: true
          },
          component: ContainerIcon
        },
        {
          path: 'btn',
          meta: {
            requireAuth: true
          },
          component: ContainerBtn
        },
        {
          path: 'sheets',
          meta: {
            requireAuth: true
          },
          component: ContainerSheets
        },
        {
          path: 'grid',
          meta: {
            requireAuth: true
          },
          component: ContainerGrid
        },
        {
          path: 'list',
          meta: {
            requireAuth: true
          },
          component: ContainerList
        },
        {
          path: 'avatar',
          meta: {
            requireAuth: true
          },
          component: ContainerAvatars
        },
        {
          path: 'table',
          meta: {
            requireAuth: true
          },
          component: ContainaerTable
        },
        {
          path: 'window',
          meta: {
            requireAuth: true
          },
          component: ContainerWindow
        }
      ]
    }
  ]
})

export default router
