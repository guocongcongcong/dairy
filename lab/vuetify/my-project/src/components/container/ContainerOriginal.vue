<template>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center align-center>
          <v-tooltip right>
            <v-btn
              icon
              large
              :href="source"
              target="_blank"
              slot="activator"
            >
              <v-icon large>code</v-icon>
            </v-btn>
            <span>Source</span>
          </v-tooltip>
        </v-layout>
        <div class="text-md-center">
              <v-btn
                color="primary"
                @click="alert = !alert"
              >
                Toggle
              </v-btn>
            </div>
            <v-alert
              :value="alert"
              type="success"
              transition="scale-transition"
            >
              This is a success alert.
            </v-alert>
      </v-container>
    </v-content>
</template>
<script>
export default {
    data () {
      return {
        alert:true
      }
    },
    props: {
      source: String
    }
}
</script>
