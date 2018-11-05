<template>
  <div id="app">
    <nav :class="active" @click.prevent>
      <a href="#" class="punctuation" @click="makeActive('punctuation')"><router-link to='/punctuation'>标点</router-link></a>
      <a href="#" class="projects" @click="makeActive('projects')"><router-link to='/projects'>Projects</router-link></a>
      <a href="#" class="services" @click="makeActive('services')"><router-link to='/services'>Services</router-link></a>
      <a href="#" class="contact" @click="makeActive('contact')"><router-link to='/contact'>Contact</router-link></a>
    </nav>
    <p>You chose <b>{{active}}</b></p>
    <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">删除区划</h3>
          </div>
          <div class="panel-body">
            <form class="form-horizontal" id="diabeldInfo">
              <div class="row">
                <div class="row col-sm-12">
                  <div class="row">
                    <div class="form-group">
                      <center>
                        <label class="col-xs-2 control-label" for="cardNum_del"><span class="nNull">*</span>区划编码:
                        </label>
                        <div class="col-xs-4">
                          <input class="form-control" type="text" id="cardNum_del" name="cardNum_del" placeholder="请输入区划编码">
                        </div>
                      </center>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
  <router-view/>
  </div>
</template>
<script>
//  $(function () { 
//     alert(123); 
//   });
export default {
  name: 'App',
  data () {
    return {
      active: 'punctuation'
    }
  },
  methods: {
    makeActive: function (item) {
      this.active = item
    }
  },
  created () {
    console.log($)
  }
}
</script>
<style>
*{
margin: 0;
padding: 0;
}

body{
text-align: center;
font:15px/1.3 'Open Sans',sans-serif;
color: #5e5b64;
}
a,a:visited{
outline:none;
color: #157ba0;
}

a:hover{
text-decoration: none;
}

section,footer,header,aside,nav{
display:block;
}

/* The menu */
nav,nav-mask{
display: inline-block;
/* margin: 60px auto 45px; 浮动*/
background-color: #209bd4;
box-shadow: 0 1px 1px #ccc;
border-radius: 2px;
text-align: end;
}

nav-mask{
background-color: #7fc9e9;
height: auto;
}
nav a{
  font:12px Helvetica Neue,Helvetica,Arial,Microsoft Yahei,Hiragino Sans GB,Heiti SC,WenQuanYi Micro Hei,sans-serif;
display: inline-block;
padding: 10px 60px;
color: #fff !important;
font-weight: bold;
font-size: 16px;
text-decoration: none !important;
line-height: 1;
text-transform: uppercase;
background-color:transparent;

-webkit-transition: background-color 0.25s;
-moz-transition: background-color 0.25s;
transition: background-color 0.25s;
}

nav a:first-child{
border-radius: 2px 0 0 2px;
}

nav a:last-child{
border-radius: 0px 2px 2px 0px;
}

nav.punctuation .punctuation,
nav.projects .projects,
nav.services .services,
nav.contact .contact{
background-color: #da6b8e;
}

p{
margin: 60px auto 45px;
font-size: 22px;
font-weight: bold;
color: #7d9098;
}

p b{
color: #fff;
display: inline-block;
padding: 5px 10px;
background-color: #c4d7e0;
border-radius: 2px;
text-decoration: uppercase;
font-size: 18px;
}

</style>
