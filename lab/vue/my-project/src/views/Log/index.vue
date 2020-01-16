<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap v-for="(item,i) in items" :key="i">
      <v-flex xs12>
        <div v-if="i%2 == 0">
          <v-card dark color="primary">
            <v-card-text>
              <code>{{item.name}}</code>
              : {{item.content}}
              <br>
              <var>{{item.link}}</var>
            </v-card-text>
          </v-card>
        </div>
        <div v-else>
          <v-card dark color="secondary">
            <v-card-text>
              <code>{{item.name}}</code>
              : {{item.content}}
              <br>
              <var>{{item.link}}</var>
            </v-card-text>
          </v-card>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      items: [
        {
          name: "icon",
          link: "",
          content:
            "添加icon页面，可以很清晰的看到所有icon"
        }
      ]
    };
  }
};
</script>


