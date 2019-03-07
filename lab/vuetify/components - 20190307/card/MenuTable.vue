<template>
  <v-card>
    <v-card-title>
      {{tableName}}
      <v-spacer></v-spacer>
      <v-text-field v-model="search" append-icon="search" label="搜索菜品" single-line hide-details></v-text-field>
    </v-card-title>
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="desserts"
      :pagination.sync="pagination"
      select-all
      item-key="name"
      class="elevation-1"
    >
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="warning">您的{{tableName}}中没有菜品 :(</v-alert>
      </template>
      <template v-slot:headers="props">
        <tr>
          <th>
            <v-checkbox
              :input-value="props.all"
              :indeterminate="props.indeterminate"
              primary
              hide-details
              @click.stop="toggleAll"
            ></v-checkbox>
          </th>
          <th
            v-for="header in props.headers"
            :key="header.text"
            :class="['column sortable', pagination.descending ? 'desc' : 'asc', header.value === pagination.sortBy ? 'active' : '']"
            @click="changeSort(header.value)"
          >
            <v-icon small>arrow_upward</v-icon>
            {{ header.text }}
          </th>
        </tr>
      </template>
      <template v-slot:items="props">
        <tr :active="props.selected" @click="props.selected = !props.selected">
          <td>
            <v-checkbox :input-value="props.selected" primary hide-details></v-checkbox>
          </td>
          <td>{{ props.item.name }}</td>
          <td class="text-xs-right">{{ props.item.taste }}</td>
          <td class="text-xs-right">{{ props.item.ingredients }}</td>
          <td class="text-xs-right">查看</td>
        </tr>
      </template>
    </v-data-table>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    tableName: "菜谱",
    search: "",
    pagination: {
      sortBy: "name", //排序
      rowsPerPage: 5 //行数
    },
    selected: [],
    headers: [
      {
        text: "菜名",
        align: "left",
        value: "name"
      },
      { text: "口味", value: "taste" },
      { text: "主料", value: "ingredients" },
      { text: "操作", value: "action" }
    ],
    desserts: [
      {
        name: "酸菜白肉",
        taste: "酸咸，利口",
        ingredients: "酸菜，五花肉",
      }
    ]
  }),

  methods: {
    toggleAll() {
      if (this.selected.length) this.selected = [];
      else this.selected = this.desserts.slice();
    },
    changeSort(column) {
      if (this.pagination.sortBy === column) {
        this.pagination.descending = !this.pagination.descending;
      } else {
        this.pagination.sortBy = column;
        this.pagination.descending = false;
      }
    }
  }
};
</script>