<template>
  <v-container fluid grid-list-xl>
    <v-layout flex-child wrap>
      <v-layout flex-child wrap>
        <v-flex xs12 md6>
          <v-layout wrap>
            <v-flex xs12>
              <menu-table-base :p-name="menus.pName" :p-rows="menus.pRows" :p-content="getContent"/>
            </v-flex>
            <v-flex xs12>
              <menu-table/>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs12 md6>
          <v-layout wrap>
            <v-flex xs12>
              <menu-table/>
            </v-flex>
            <v-flex xs12>
              <menu-table/>
            </v-flex>
            <v-flex xs12>
              <menu-table/>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-layout>
    <add-info></add-info>
    <content-info-base></content-info-base>
  </v-container>
</template>
<script>
import ContentInfo from "comp/card/ContentInfo";
import AddInfo from "comp/card/Addinfo";
import MenuTable from "comp/card/MenuTable";
import MenuTableBase from "comp/card/MenuTableBase";
import ContentInfoBase from "comp/card/ContentInfoBase";

export default {
  data: () => ({
    menus: {
      pName: "炖菜",
      pRows: 10,
      pContent: []
    }
  }),
  computed: {
    getContent: function() {
      return (this.menus.pContent = [
        {
          name: "酸菜白肉1",
          taste: "酸咸1，利口1",
          ingredients: "酸菜1，五花肉1",
          production: {
            ingredients: ["牛腱子1KG"],
            excipient: [
              "黄酒",
              "冰糖",
              "小茴香",
              "花椒",
              "八角",
              "桂皮",
              "丁洋",
              "陈皮",
              "香叶"
            ],
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
        }
      ]);
    }
  },
  components: {
    AddInfo,
    //ContentInfo,
    MenuTable,
    MenuTableBase,
    ContentInfoBase
  }
};
</script>
