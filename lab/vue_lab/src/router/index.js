import Vue from 'vue'
import Router from 'vue-router'
import Punctuation from '@/components/Punctuation'
import TopMenu from '@/components/TopMenu'
import Test from '@/components/Test'

Vue.use(Router)

export default new Router({
  routes: [ {
    path: '/punctuation',
    name: 'Punctuation',
    component: Punctuation
  },
  {
    path: '/projects',
    name: 'TopMenu',
    component: TopMenu
  },
  {
    path: '/services',
    name: 'hello',
    component: Test
  }]
})
