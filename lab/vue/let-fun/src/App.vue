<template>
  <v-app id="sandbox">
    <v-navigation-drawer
      v-model="primaryDrawer.model"
      :clipped="primaryDrawer.clipped"
      :floating="primaryDrawer.floating"
      :mini-variant="primaryDrawer.mini"
      :permanent="primaryDrawer.type === 'permanent'"
      :temporary="primaryDrawer.type === 'temporary'"
      app
      overflow
    />

    <v-app-bar :clipped-left="primaryDrawer.clipped" app>
      <v-app-bar-nav-icon
        v-if="primaryDrawer.type !== 'permanent'"
        @click.stop="primaryDrawer.model = !primaryDrawer.model"
      />
      <v-toolbar-title>Vuetify</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <div id="nav">
          <router-link to="/">Home</router-link>|
          <router-link to="/about">About</router-link>
        </div>
        <router-view />
        <v-row align="center" justify="center">
          <v-col cols="10">
            <v-card>
              <v-card-text>
                <v-row>
                  <v-col cols="12" md="6">
                    <span>Scheme</span>
                    <v-switch v-model="$vuetify.theme.dark" primary label="Dark" />
                  </v-col>
                  <v-col cols="12" md="6">
                    <span>Drawer</span>
                    <v-radio-group v-model="primaryDrawer.type" column>
                      <v-radio
                        v-for="drawer in drawers"
                        :key="drawer"
                        :label="drawer"
                        :value="drawer.toLowerCase()"
                        primary
                      />
                    </v-radio-group>
                    <v-switch v-model="primaryDrawer.clipped" label="Clipped" primary />
                    <v-switch v-model="primaryDrawer.floating" label="Floating" primary />
                    <v-switch v-model="primaryDrawer.mini" label="Mini" primary />
                  </v-col>
                  <v-col cols="12" md="6">
                    <span>Footer</span>
                    <v-switch v-model="footer.inset" label="Inset" primary />
                  </v-col>
                </v-row>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn text>Cancel</v-btn>
                <v-btn text color="primary">Submit</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer :inset="footer.inset" app>
      <span class="px-4">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawers: ["Default (no property)", "Permanent", "Temporary"],
    primaryDrawer: {
      model: null,
      type: "default (no property)",
      clipped: false,
      floating: false,
      mini: false
    },
    footer: {
      inset: false
    }
  })
};
</script>