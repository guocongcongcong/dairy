<template>
  <div>

    <div>
      <el-container>
        <el-header>
            <el-col :span="6" :offset="18" >
                <el-row>
                  <el-button icon="el-icon-search" circle></el-button>
                  <el-button type="primary" icon="el-icon-edit" circle></el-button>
                  <el-button type="success" icon="el-icon-check" circle></el-button>
                  <el-button type="info" icon="el-icon-message" circle></el-button>
                  <el-button type="warning" icon="el-icon-star-off" circle></el-button>
                  <el-button type="danger" icon="el-icon-delete" circle></el-button>
                </el-row>
              </el-col>
        </el-header>
        <el-container>
          <el-aside width="200px">Aside</el-aside>
          <el-main >
            
          </el-main>
        </el-container>
      </el-container>
    </div>
  </div>
</template>

<script>
export default {
   data() {
        return {
          tableData: [{
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1517 弄'
          }, {
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1519 弄'
          }, {
            date: '2016-05-03',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1516 弄'
          }]
        }
      }
  };
</script>

<style>
  /* .transition-box {
    margin-bottom: 10px;
    width: 200px;
    height: 100px;
    border-radius: 4px;
    background-color: #409EFF;
    text-align: center;
    color: #fff;
    box-sizing: border-box;
    margin-right: 20px;
  } */
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

    .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
