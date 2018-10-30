<template>

  <div id="app">

    <nav class='navbar navbar-default' role='navigation'>
      <div class='container-fluid'>
      <div class='navbar-header'>
          <a class='navbar-brand' href='#'>菜鸟教程</a>
      </div>
      <div>
          <ul class='nav navbar-nav'>
              <li class='active'><a href='#'>iOS</a></li>
              <li><a href='#'>SVN</a></li>
              <li class='dropdown'>
                  <a href='#' class='dropdown-toggle' data-toggle='dropdown'>`
                      Java
                      <b class='caret'></b>
                  </a>
                  <ul class='dropdown-menu'>
                      <li><a href='#'>jmeter</a></li>
                      <li><a href='#'>EJB</a></li>
                      <li><a href='#'>Jasper Report</a></li>
                      <li class='divider'></li>
                      <li><a href='#'>分离的链接</a></li>
                      <li class='divider'></li>
                      <li><a href='#'>另一个分离的链接</a></li>
                  </ul>
              </li>
          </ul>
      </div>
      </div>
  </nav>
    <!-- <img src="./assets/logo.png"> -->
    <router-view/>

  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
