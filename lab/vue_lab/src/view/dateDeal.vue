<template>
    <el-container>
              <el-header>
                <el-col :span="10" :offset="7">
                <el-row>
                  <el-button type="primary" icon="el-icon-edit"></el-button>
                  <el-button type="primary" icon="el-icon-share"></el-button>
                  <el-button type="primary" icon="el-icon-delete"></el-button>
                  <el-button type="primary" icon="el-icon-search">搜索</el-button>
                  <el-button type="primary">上传<i class="el-icon-upload el-icon--right"></i></el-button>
                </el-row>
            </el-col>
              </el-header>
              <el-main>
                <el-row :gutter="24">
                  <el-col :span="20" :offset="2">               
                    <el-table
                      :data="tableData"
                      style="width: 100%">
                      <el-table-column
                        prop="date"
                        label="日期"
                        width="180">
                      </el-table-column>
                      <el-table-column
                        prop="name"
                        label="姓名"
                        width="180">
                      </el-table-column>
                      <el-table-column
                        prop="address"
                        label="地址">
                      </el-table-column>
                    </el-table>
                  </el-col>
                </el-row>
              </el-main>
              <el-footer>
                <el-button-group class='footer page'>
                      <el-button type="primary" icon="el-icon-arrow-left">上一页</el-button>
                      <el-button type="primary">下一页<i class="el-icon-arrow-right el-icon--right"></i></el-button>
                    </el-button-group>
              </el-footer>
            </el-container>
</template>
