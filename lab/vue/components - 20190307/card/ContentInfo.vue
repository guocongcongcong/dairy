<template>
  <div>
    <v-btn class="demo2" fab right color="orange" dark fixed @click.stop="dialog = !dialog">
      <v-icon>burst_mode</v-icon>
    </v-btn>
    <v-dialog v-model="dialog" width="800px">
      <v-card>
        <v-card-title class="grey lighten-4 py-4 headline font-weight-black" v-html="make.name"></v-card-title>
        <v-container grid-list-sm class="pa-4">
          <v-layout row wrap>
            <!-- <v-flex xs12 align-center justify-space-between>
              <h5 class="headline font-weight-black">五香牛肉</h5>
            </v-flex>-->
            <v-flex xs12>
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title>主料:</v-list-tile-title>
                  <v-list-tile-sub-title v-html="make.ingredients"></v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-flex>

            <v-flex xs12>
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title>辅料:</v-list-tile-title>
                  <v-list-tile-sub-title v-html="make.excipient"></v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-flex>

            <v-flex xs12>
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title>制作方法:</v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
              <ol>
                <div v-for="(items,i) in make.production" :key="i">
                <li>{{items.item}}</li>
                </div>
              </ol>
            </v-flex>
          </v-layout>
        </v-container>
        <v-card-actions>
          <!-- <v-
          btn flat color="primary">More</v-btn>
          <v-spacer></v-spacer>
          <v-btn flat color="light-green accent-4" @click="dialog = false"></v-btn>
          <v-btn flat color="light-green accent-4" @click="dialog = false">保存</v-btn>-->
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script >
export default {
  data: () => ({
    dialog: false,
    make: {
      name: "五香牛肉",
      ingredients: "牛腱子 1KG",
      excipient: "黄酒，冰糖，小茴香，花椒，八角，桂皮，丁洋，陈皮，香叶",
      production: [
        { item: "牛肉解冻后，泡水半小时，三次" },
        { item: "加入葱姜少许料酒，焯水出浮沫，加入冷水洗净" },
        {
          item:
            "起炖锅，清水，开盖煮开，加五香，盐，冰糖，料酒，少许葱姜，滚5分钟"
        },
        { item: "转小火1小时" },
        { item: "趁热捞出，晾干后，冷浸一晚（两次）" },
        { item: "阴干后食用" }
      ]
    }
  })
};
</script>
<style>
.demo2 {
  bottom: 85px;
}
</style>