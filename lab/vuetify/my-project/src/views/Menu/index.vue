<template>
  <v-container fluid grid-list-xl>
    <v-layout flex-child wrap>
      <v-layout flex-child wrap>
        <v-flex xs12 md6>
          <v-layout wrap>
            <v-flex xs12>
              <menu-table-base :p-name="menus.pName" :p-rows="menus.pRows" :p-content="getContent"/>
            </v-flex>
            <v-flex xs12>
              <menu-table/>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs12 md6>
          <v-layout wrap>
            <v-flex xs12>
              <menu-table/>
            </v-flex>
            <v-flex xs12>
              <menu-table/>
            </v-flex>
            <v-flex xs12>
              <menu-table/>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-layout>
    <add-info></add-info>
    <content-info></content-info>
  </v-container>
</template>
<script>
import ContentInfo from "comp/card/ContentInfo";
import AddInfo from "comp/card/Addinfo";
import MenuTable from "comp/card/MenuTable";
import MenuTableBase from "comp/card/MenuTableBase";

export default {
  data: () => ({
    menus: {
      pName: "炖菜",
      pRows: 10,
      pContent: []
    }
  }),
  computed:{
    getContent:function(){
      return this.menus.pContent = [{
          name: "酸菜白肉1",
          taste: "酸咸1，利口1",
          ingredients: "酸菜1，五花肉1"
        },
        {
          name: "酸菜白肉2",
          taste: "酸咸2，利口2",
          ingredients: "酸菜2，五花肉2"
        }];
    }
  },
  components: {
    AddInfo,
    ContentInfo,
    MenuTable,
    MenuTableBase
  }
};
</script>
