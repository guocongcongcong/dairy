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
          name: "Grid",

          link: "https://next.vuetifyjs.com/zh-Hans/framework/grid",
          content:
            "Vuetify拥有一个12点的栅格系统，它使用flex-box构建，栅格用于布局应用程序的内容。它包含5种类型的媒体断点，用于定位特定的屏幕大小或方向。栅格组件的属性实际上是从它们定义的属性派生的类，这允许您轻松地将这些辅助类指定为属性，同时仍然提供在任何地方使用的类。"
        }
      ]
    };
  }
};
</script>


