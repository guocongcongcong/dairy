<template>
  <v-container fluid grid-list-xl>
    <v-layout flex-child wrap>
      <v-layout flex-child wrap>
      <v-flex xs12 md6 d-flex>
        <v-layout wrap>
          <v-flex xs12>
            <v-sheet class="d-flex" color="grey lighten-3" height="615">

<v-card>
        <v-container
          fluid
          grid-list-md
        >
          <v-layout row wrap>
            <v-flex
              v-for="card in cards"
              :key="card.title"
              v-bind="{ [`xs${card.flex}`]: true }"
            >
              <v-card>
                <v-img
                  :src="card.src"
                  height="200px"
                >
                  <v-container
                    fill-height
                    fluid
                    pa-2
                  >
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
            <v-sheet class="d-flex" color="teal lighten-3" height="615">
              
              <template>
                <v-form v-model="valid">
                  <v-container>
                    <v-layout>
                      <v-flex
                        xs12
                        md4
                      >
                        <v-text-field
                          v-model="firstname"
                          :rules="nameRules"
                          :counter="10"
                          label="First name"
                          required
                        ></v-text-field>
                      </v-flex>

                      <v-flex
                        xs12
                        md4
                      >
                        <v-text-field
                          v-model="lastname"
                          :rules="nameRules"
                          :counter="10"
                          label="Last name"
                          required
                        ></v-text-field>
                      </v-flex>

                      <v-flex
                        xs12
                        md4
                      >
                        <v-text-field
                          v-model="email"
                          :rules="emailRules"
                          label="E-mail"
                          required
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-form>
              </template>

            </v-sheet>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex xs12 md6 d-flex>
        <v-layout wrap>
          <v-flex xs12>
            <v-sheet class="d-flex" color="green lighten-3" height="450">
              
              <template>
                <v-container
                  id="input-usage"
                  grid-list-xl
                  fluid
                >
                  <v-layout wrap>
                    <v-flex xs12>
                      <v-input
                        :messages="['Messages']"
                        append-icon="close"
                        prepend-icon="phone"
                      >
                        Default Slot
                      </v-input>
                    </v-flex>
                  </v-layout>
                </v-container>
              </template>

            </v-sheet>
          </v-flex>
          <v-flex xs12>
            <v-sheet class="d-flex" color="yellow lighten-3" height="450">
              
              <template>
                <v-card
                  class="hide-overflow"
                  color="purple lighten-1"
                  dark
                >
                  <v-toolbar
                    card
                    color="purple"
                  >
                    <v-icon>mdi-account</v-icon>
                    <v-toolbar-title class="font-weight-light">User Profile</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="purple darken-3"
                      fab
                      small
                      @click="isEditing = !isEditing"
                    >
                      <v-icon v-if="isEditing">close</v-icon>
                      <v-icon v-else>edit</v-icon>
                    </v-btn>
                  </v-toolbar>
                  <v-card-text>
                    <v-text-field
                      :disabled="!isEditing"
                      color="white"
                      label="Name"
                    ></v-text-field>
                    <v-autocomplete
                      :disabled="!isEditing"
                      :items="states"
                      :filter="customFilter"
                      color="white"
                      item-text="name"
                      label="State"
                    ></v-autocomplete>
                  </v-card-text>
                  <v-divider></v-divider>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      :disabled="!isEditing"
                      color="success"
                      @click="save"
                    >
                      Save
                    </v-btn>
                  </v-card-actions>
                  <v-snackbar
                    v-model="hasSaved"
                    :timeout="2000"
                    absolute
                    bottom
                    left
                  >
                    Your profile has been updated
                  </v-snackbar>
                </v-card>
              </template>

            </v-sheet>
          </v-flex>
          <v-flex xs12>
            <v-sheet class="d-flex" color="red lighten-3" height="300">
              
              <template>
                <v-layout>
                  <v-flex xs12 sm6 offset-sm3>
                    <v-card>
                      <v-img
                        src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
                        aspect-ratio="2.75"
                      ></v-img>

                      <v-card-title primary-title>
                        <div>
                          <h3 class="headline mb-0">Kangaroo Valley Safari</h3>
                          <div>Located two hours south of Sydney in the <br>Southern Highlands of New South Wales, ...</div>
                        </div>
                      </v-card-title>

                      <v-card-actions>
                        <v-btn flat color="orange">Share</v-btn>
                        <v-btn flat color="orange">Explore</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-flex>
                </v-layout>
              </template>

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
    data () {
      return {
       cards: [
        { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
        { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
      ],
         valid: false,
      firstname: '',
      lastname: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 10 || 'Name must be less than 10 characters'
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      text: '',
      hasSaved: false,
        isEditing: null,
        model: null,
        states: [
          { name: 'Florida', abbr: 'FL', id: 1 },
          { name: 'Georgia', abbr: 'GA', id: 2 },
          { name: 'Nebraska', abbr: 'NE', id: 3 },
          { name: 'California', abbr: 'CA', id: 4 },
          { name: 'New York', abbr: 'NY', id: 5 }
        ],
        card_text: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.'
      }
    },
    methods: {
      appendIconCallback () {},
      prependIconCallback () {},
      customFilter (item, queryText, itemText) {
        const textOne = item.name.toLowerCase()
        const textTwo = item.abbr.toLowerCase()
        const searchText = queryText.toLowerCase()

        return textOne.indexOf(searchText) > -1 ||
          textTwo.indexOf(searchText) > -1
      },
      save () {
        this.isEditing = !this.isEditing
        this.hasSaved = true
      }
    }
  }
</script>
<style>
  #input-usage .v-input__prepend-outer,
  #input-usage .v-input__append-outer,
  #input-usage .v-input__slot,
  #input-usage .v-messages {
    border: 1px dashed rgba(0,0,0, .4);
  }
</style>