<template>
  <v-container fluid grid-list-xs>
    <v-layout flex-child wrap  >
      <v-flex xs2 md2 v-for="(item,i) in items" :key="i">
        <v-layout wrap>
          <v-flex xs12>
            <v-sheet class="d-flex" color="brown lighten-5" height="50">
              <v-avatar >
                <v-icon x-large>{{item.icon}}</v-icon>
              </v-avatar>
            </v-sheet>
          </v-flex>
          <v-flex xs12>
            <v-sheet class="d-flex" color="grey lighten-2" height="30">
              <center style="padding:4px;">{{item.name}}</center>
            </v-sheet>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
    
  </v-container>
</template>
<script>

import icon_list from "../../assets/icon.json";
export default {
  data() {
    return {
        items:icon_list
    }
    }
};
</script>