<template>
  <v-container fluid grid-list-xl>
    <v-layout flex-child wrap>
      <v-layout flex-child wrap>
        <v-flex xs12 md6 d-flex>
          <v-layout wrap>
            <v-flex xs12>
              <v-sheet class="d-flex" color="grey lighten-3" height="615">
                <v-card>
                  <v-container fluid grid-list-md>
                    <v-layout row wrap>
                      <v-flex
                        v-for="card in cards"
                        :key="card.title"
                        v-bind="{ [`xs${card.flex}`]: true }"
                      >
                        <v-card>
                          <v-img :src="card.src" height="200px">
                            <v-container fill-height fluid pa-2>
                              <v-layout fill-height>
                                <v-flex xs12 align-end flexbox>
                                  <span class="headline white--text" v-text="card.title"></span>
                                </v-flex>
                              </v-layout>
                            </v-container>
                          </v-img>

                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn icon>
                              <v-icon>favorite</v-icon>
                            </v-btn>
                            <v-btn icon>
                              <v-icon>bookmark</v-icon>
                            </v-btn>
                            <v-btn icon>
                              <v-icon>share</v-icon>
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card>
              </v-sheet>
            </v-flex>
            <v-flex xs12>
              <v-sheet class="d-flex" color="teal lighten-3" height="615"></v-sheet>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs12 md6 d-flex>
          <v-layout wrap>
            <v-flex xs12>
              <v-sheet class="d-flex" color="green lighten-3" height="450"></v-sheet>
            </v-flex>
            <v-flex xs12>
              <v-sheet class="d-flex" color="yellow lighten-3" height="450"></v-sheet>
            </v-flex>
            <v-flex xs12>
              <v-sheet class="d-flex" color="red lighten-3" height="300"></v-sheet>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      cards: [
        {
          title: "Favorite road trips",
          src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
          flex: 6
        },
        {
          title: "Best airlines",
          src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
          flex: 6
        },
        {
          title: "Pre-fab homes",
          src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
          flex: 12
        }
      ]
    };
  }
};
</script>
