<template>
  <v-container fluid grid-list-md>
    <v-layout flex-child wrap>
      <v-layout flex-child wrap>
        <v-flex xs12 md6 d-flex>
          <v-layout wrap>
            <v-flex xs12>
              <v-sheet class="d-flex" color="grey lighten-3" height="420">
                <v-card>
                  <v-container fluid grid-list-md>
                    <v-layout row wrap>
                      <v-flex
                        v-for="card in cards"
                        :key="card.title"
                        v-bind="{ [`xs${card.flex}`]: true }"
                      >
                        <v-card>
                          <v-img :src="card.src" height="130px">
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
            <!-- <v-flex xs12>
              <v-sheet class="d-flex" color="teal lighten-3" height="605"></v-sheet>
            </v-flex>-->
          </v-layout>
        </v-flex>
        <v-flex xs12 md6 d-flex>
          <v-layout wrap>
            <v-flex xs12>
              <v-sheet class="d-flex" color="green lighten-3" height="205"></v-sheet>
            </v-flex>
            <v-flex xs12>
              <v-sheet class="d-flex" color="red lighten-3" height="205"></v-sheet>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs12 md12>
          <v-toolbar flat dark>
            <v-toolbar-title>项目经历</v-toolbar-title>
            <v-spacer></v-spacer>
            <div  >
              <div class="text-md-center d-flex align-center" >
                <v-tooltip bottom v-for="(remark,i) in remarks" :key="i">
                  <template #activator="data">
                    <span v-on="data.on">{{remark.name}} | </span>
                  </template>
                  <span>{{remark.remark}}</span>
                </v-tooltip>
              </div>
            </div>
          </v-toolbar>
          <v-data-table :headers="headers" :items="desserts" class="elevation-1" dark>
            <template slot="items" slot-scope="props">
              <td>{{ props.item.name }}</td>
              <td class="text-xs">{{ props.item.date }}</td>
              <td class="text-xs">{{ props.item.front }}</td>
              <td class="text-xs">{{ props.item.rear }}</td>
              <td class="text-xs">{{ props.item.duties }}</td>
              <td class="text-xs">{{ props.item.completion }}</td>
            </template>
          </v-data-table>
        </v-flex>
      </v-layout>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      dialog: false,
       remarks: [
         {
          name: "名词解释",
          remark: "名词解释"
        },
        {
          name: "sword",
          remark: "中软自己开发的框架"
        },
        {
          name: "pug",
          remark: "html整合工具"
        }
      ],
      headers: [
        {
          text: "项目",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "时间", value: "date" },
        { text: "前端", value: "front" },
        { text: "后端", value: "rear" },
        { text: "职责", value: "duties" },
        { text: "完成度", value: "completion" }
      ],
      desserts: [
        {
          name: "补贴系统",
          date: "2018/9-2019/1",
          front: "Node.js,pug,bootstarp",
          rear: "sword",
          duties: "整站开发",
          completion: "100%"
        }
      ],
      cards: [
        {
          title: "Favorite road trips",
          src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
          flex: 3
        },
        {
          title: "Best airlines",
          src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
          flex: 3
        },
        {
          title: "Best airlines",
          src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
          flex: 3
        },
        {
          title: "Best airlines",
          src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
          flex: 3
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
