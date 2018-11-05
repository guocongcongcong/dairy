// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from '../components/Punctuation'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#Punctuation',
  data: {
    msg: 'guoliwei'
  },
  components: {App},
  template: '<App/>'
})
