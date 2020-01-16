<template>
  <v-card>
    <v-card-title>
      目录
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="搜索"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table :headers="headers" :items="desserts" :search="search">
      <template v-slot:items="props">
        <td class="text-xs-center">{{ props.item.name }}</td>
        <td class="text-xs-center">{{ props.item.address }}</td>
        <td class="text-xs-center"><a :href=publicPath+props.item.link target="_blank" :download=props.item.name>下载</a></td>
      </template>
      <v-alert v-slot:no-results :value="true" color="error" icon="warning">
        Your search for "{{ search }}" found no results.
      </v-alert>
    </v-data-table>
  </v-card>
</template>
<script>
import bookIndex from './bookIndex.json'
export default {
  data() {
    return {
      search: "",
      headers: [
        {
          text: "名称",
          align: "center",
          sortable: false,
          value: "name"
        },
        { text: "地址",align: "center", value: "address" },
        { text: "索引",align: "center", value: "link" },
      ],
      desserts: bookIndex,
      publicPath: process.env.BASE_URL
    };
  }
};
</script>
