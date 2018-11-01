<template>

  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
      <div>
        <nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header"><a class="navbar-brand" href="#">自建小工具</a></div>
        <div>
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">1</a></li>
            <li class="active"><a href="#">2</a></li>
            <li class="dropdown"><a class="dropdown-toggle" href="#" data-toggle="dropdown">数据处理<b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">截取身份证号添加英文逗号和引号</a></li>
                <li class="divider"></li>
                <li><a href="#">去逗号加引号</a></li>
                <li class="divider"></li>
                <li><a href="#">大小写转化</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <section class="container">
      <div class="login">
        <div class="form-horizontal" id="disabledForm">
          <div class="panel panel-default">
            <div class="panel-heading">
              <h3 class="panel-title">添加区划                                  </h3>
            </div>
            <div class="panel-body" id="printPage">
              <form class="form-horizontal" id="diabeldInfo">
                <div class="row">
                  <div class="row col-sm-12">
                    <div class="row">
                      <div class="form-group">
                        <label class="col-xs-2 control-label" for="name_add"><span class="nNull">*</span>长度:
                        </label>
                        <div class="col-xs-4">
                          <input class="form-control" type="text" id="name_add" name="name_add" placeholder="请输入截取长度（默认为不截取）"/>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </form>
            </div>
            <div class="panel-heading">
              <h3 class="panel-title">去逗号加引号</h3>
            </div>
            <div class="panel-body" style="text-align:center;padding: 10px;">
              <div class="row clearfix">
                <div class="col-md-6 column">
                  <div class="panel panel-default">
                    <div class="panel-heading">
                      <h3 class="panel-title">原始数据</h3>
                    </div>
                    <div class="panel-body">
                      <div class="col-xs-12" style="text-align:center;padding: 10px;">
                        <center>
                          <textarea class="form-control" type="text" id="original" name="original" rows="15"> </textarea>
                        </center>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-md-6 column">
                  <div class="panel panel-default">
                    <div class="panel-heading">
                      <h3 class="panel-title">处理结果</h3>
                    </div>
                    <div class="panel-body">
                      <div class="col-xs-12" style="text-align:center;padding: 10px;">
                        <center>
                          <textarea class="form-control" type="text" id="result" name="result" rows="15"> </textarea>
                        </center>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div style="text-align:center;padding: 10px;"><a class="btn btn-warning" id="processing" role="button" type="button" style="margin: 10px;">处理</a><a class="btn btn-warning" id="copy" role="button" type="button" style="margin: 10px;">复制</a><a class="btn btn-warning" id="cleanValue" role="button" type="button" style="margin: 10px;">重置</a></div>
          </div>
        </div>
      </div>
    </section>
  </div>
    <router-view/>

  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/* #app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
