<template>
  <div id="app">
  <v-app id="inspire">
    <drawer-bar></drawer-bar>
    <!-- <container id="container" ></container> -->
    <div id = "container"><router-view></router-view></div>
    
  </v-app>
</div>
</template>

<script>
import Drawer from 'comp/Drawer'
// import ContainerSheets from 'comp/container/ContainerSheets'
// import ContainerGrid from 'comp/container/ContainerGrid'
// import ContainerOriginal from 'comp/container/ContainerOriginal'
//import ContainerPlugin from 'comp/container/ContainerPlugin'
export default {
    name: 'layout',
    components: {
        'drawer-bar':Drawer,
        //'container':ContainerPlugin
    }
  }
</script>

<style>
#container {
  padding:75px;
}
</style>
