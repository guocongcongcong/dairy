import Vue from 'vue'
import Router from 'vue-router'
import BaseButton from '@/components/TopMenu'

Vue.use(Router)

export default new Router({
  routes: [ {
    path: '/',
    name: 'BaseButton',
    component: BaseButton
  }]
})
