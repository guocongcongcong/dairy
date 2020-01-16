<template>
  <v-container fluid grid-list-xl>
    <v-layout flex-child wrap>
      <v-layout flex-child wrap>
        <v-flex xs12 md6 d-flex>
          <v-layout wrap>
            <v-flex xs12>
              <v-sheet class="d-flex" color="grey lighten-3" height="615">
              </v-sheet>
            </v-flex>
            <v-flex xs12>
              <v-sheet class="d-flex" color="teal lighten-3" height="615">
              </v-sheet>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs12 md6 d-flex>
          <v-layout wrap>
            <v-flex xs12>
              <v-sheet class="d-flex" color="green lighten-3" height="450">
                <sheet-footer>小菜</sheet-footer>
              </v-sheet>
            </v-flex>
            <v-flex xs12>
              <v-sheet class="d-flex" color="yellow lighten-3" height="450">
                <sheet-footer>汤</sheet-footer>
              </v-sheet>
            </v-flex>
            <v-flex xs12>
              <v-sheet class="d-flex" color="red lighten-3" height="300">
                <sheet-footer>主食</sheet-footer>
              </v-sheet>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-layout>
  </v-container>
</template>
<script>
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
    }
  }
};
</script>