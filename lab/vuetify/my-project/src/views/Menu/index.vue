<template>
  <v-container fluid grid-list-xl>
    <v-layout flex-child wrap>
      <v-layout flex-child wrap>
        <v-flex xs12 md6>
          <v-layout wrap>
            <v-flex xs12>
              <menu-table/>
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
import MenuCard from "comp/card/MenuCard1";
import ContentInfo from "comp/card/ContentInfo";
import AddInfo from "comp/Addinfo";
import MenuTable from "comp/card/MenuTable";

export default {
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
    "menu-card": MenuCard,
    "add-info": AddInfo,
    "c-info": ContentInfo,
    "menu-table": MenuTable
  }
};
</script>
