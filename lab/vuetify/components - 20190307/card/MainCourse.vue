<template>
  <v-container  grid-list-xl>
    <v-layout  wrap>
      <v-flex xs12 md8 d-flex>
        <v-sheet class="d-flex" color="grey lighten-3" height="1424">
        </v-sheet>
      </v-flex>

    </v-layout>
          <v-sheet class="windows"  color="red lighten-3" witch   height="250">

            </v-sheet>
    <add-info></add-info>
    <c-info></c-info>
  </v-container>
</template>
<script>
import ContentInfo from "comp/card/ContentInfo";
import AddInfo from "comp/Addinfo";

export default {
  components: {
    // SheetFooter: {
    //   functional: true,
    //   render(h, { children }) {
    //     return h(
    //       "v-sheet",
    //       {
    //         staticClass: "mt-auto align-center justify-center d-flex",
    //         props: {
    //           color: "rgba(0, 0, 0, .36)",
    //           dark: true,
    //           height: 50
    //         }
    //       },
    //       children
    //     );
    //   }
    // },
    "add-info": AddInfo,
    "c-info": ContentInfo
  }
};
</script>
<style scoped>
.windows {
  bottom: 1450px;
  position: fixed;
  right: 16px;
  
}
</style>
