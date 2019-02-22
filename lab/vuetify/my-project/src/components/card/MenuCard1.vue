<template>
  <v-card  color="blue-grey lighten-5">
    <v-card-title primary-title>
      <div>
        <h3 class="headline mb-0">主菜</h3>
      </div>
    </v-card-title>
    <v-container fluid grid-list-lg>
      <v-list two-line>
        <template v-for="(item, index) in items">
          <v-subheader v-if="item.header" :key="item.header">
            <h3 class="headline mb-0">{{ item.header }}</h3>
          </v-subheader>

          <v-divider   v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>

          <!-- <v-list-tile
              v-else
              :key="item.title"
              avatar
              @click=""
          >-->
          <v-list-tile v-else :key="item.title" avatar ripple @click="">
            <div v-if=" item.avatar">
              <v-list-tile-avatar>
                <img :src="item.avatar">
              </v-list-tile-avatar>
            </div>
            <v-list-tile-content>
              <v-list-tile-title v-html="item.title"></v-list-tile-title>
              <v-list-tile-sub-title v-html="item.subtitle"></v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-container>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      items: [
        { header: "炒菜" },
        {
          avatar: "",
          title: "圆白菜",
          subtitle:
            "<span class='text--primary'>圆白菜，肉</span> &mdash; 葱姜蒜，料酒"
        },
        { divider: true, inset: false },
        {
          avatar: "",
          title: '西兰花 <span class="grey--text text--lighten-1">2</span>',
          subtitle: "<span class='text--primary'>西兰花</span> &mdash; 蒜"
        },
        { divider: true, inset: false },
        {
          avatar: "",
          title: '蒿子杆 <span class="grey--text text--lighten-1">素炒</span>',
          subtitle:
            "<span class='text--primary'>蒿子杆</span> &mdash; 葱，姜，蒜"
        },
        { divider: true, inset: false },
        { header: "炖菜" },
        {
          avatar: "",
          title: "酸菜白肉",
          subtitle:
            "<span class='text--primary'>五花肉，酸菜</span> &mdash; 葱，姜，蒜，料酒，配料"
        },
        { divider: true, inset: false },
        {
          avatar: "",
          title:
            '土豆炖豆角 <span class="grey--text text--lighten-1">素</span>',
          subtitle:
            "<span class='text--primary'>土豆，豆角</span> &mdash; 大料，花椒，葱，姜，蒜，香叶"
        }
      ]
    };
  }
};
</script>