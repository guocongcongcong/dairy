<template>
  <v-container fluid grid-list-xl>
    <v-layout flex-child wrap>
      <v-layout flex-child wrap>
        <v-flex xs12 md6>
          <v-layout wrap>
            <v-flex xs12>
              <menu-table-base v-bind:p-rows="10" v-bind:p-name="post.pName"/>
              <!-- <menu-card></menu-card> -->
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
    <c-info></c-info>
  </v-container>
</template>
<script>
import ContentInfo from "comp/card/ContentInfo";
import AddInfo from "comp/card/Addinfo";
import MenuTable from "comp/card/MenuTable";
import MenuTableBase from "comp/card/MenuTableBase";
export default {
  date: () => ({
    post:{
        pName: "炖菜",
        pRows: 10,
        pContent: [
          {
            name: "酸菜白肉1",
            taste: "酸咸1，利口1",
            ingredients: "酸菜1，五花肉1"
          },
          {
            name: "酸菜白肉2",
            taste: "酸咸2，利口2",
            ingredients: "酸菜2，五花肉2"
          }
        ]
    }
    }
  ),
  components: {
    SheetFooter: {
      functional: true,
      render(h, { children }) {
        return h(
          "v-sheet",
          {
            staticClass: "mt-auto align-center justify-center d-flex",
            props: {
              color: "rgba(0, 0, 0, .36)",
              dark: true,
              height: 50
            }
          },
          children
        );
      }
    },
    "add-info": AddInfo,
    "c-info": ContentInfo,
    "menu-table": MenuTable,
    "menu-table-base": MenuTableBase
  }
};
</script>
