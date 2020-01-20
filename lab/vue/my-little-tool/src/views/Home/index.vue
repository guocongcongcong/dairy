<template>
  <div class="home">
    <v-row align="center" justify="center">
      <v-col cols="10">
        <v-card>
          <v-flex xs12 text-center>
            <img alt="Vue logo" src="../../assets/logo.png" />
            <HelloWorld msg="Welcome to Your Vue.js App" />
          </v-flex>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "home",
  components: {
    HelloWorld
  }
};
</script>
