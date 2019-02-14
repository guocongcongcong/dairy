<template>
  <div id="app">
  <v-app id="inspire">
    <drawer-bar></drawer-bar>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center align-center>
          <v-tooltip right>
            <v-btn
              icon
              large
              :href="source"
              target="_blank"
              slot="activator"
            >
              <v-icon large>code</v-icon>
            </v-btn>
            <span>Source</span>
          </v-tooltip>
        </v-layout>
      </v-container>
    </v-content>
    <add-info></add-info>
  </v-app>
</div>
</template>

<script>
import Drawer from 'comp/Drawer'
import AddInfo from 'comp/Addinfo'

export default {
    name: 'layout',
    components: {
        'drawer-bar':Drawer,
        'add-info':AddInfo
  },
    props: {
      source: String
    }
  }
</script>

<style>

</style>
