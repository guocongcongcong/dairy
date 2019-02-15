<template>
  <v-container fluid grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex v-for="item in items" :key="item" xs12>
        <v-card dark color="primary">
          <v-card-text>
            <code>{{item.name}}</code>
            : {{item.content}}
            <br>
            <var>{{item.link}}</var>
          </v-card-text>
        </v-card>
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
          "name": "v-alert",
          "link": "https://next.vuetifyjs.com/zh-Hans/components/alerts",
          "content":
            "组件被用来向用户传达重要信息，它有4个变种，成功（success），信息（info），警告（warning）和错误（error）。它们被分配了可以修改的表示不同操作的默认图标"
        },
        {
          "name": "v-alert",
          "link": "https://next.vuetifyjs.com/zh-Hans/components/alerts",
          "content":
            "组件被用来向用户传达重要信息，它有4个变种，成功（success），信息（info），警告（warning）和错误（error）。它们被分配了可以修改的表示不同操作的默认图标"
        }
      ]
    };
  }
};
</script>


