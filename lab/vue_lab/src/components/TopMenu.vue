<template>
<div id="main">
    <nav :class="active" @click.prevent>
      <div class="nRight">
      <a href="#" class="home" @click="makeActive('home')"><router-link to='/home'> Home</router-link></a>
      <a href="#" class="projects" @click="makeActive('projects')"><router-link to='/projects'>Projects</router-link></a>
      <a href="#" class="services" @click="makeActive('services')"><router-link to='/services'>Services</router-link></a>
      <a href="#" class="contact" @click="makeActive('contact')"><router-link to='/contact'>Contact</router-link></a>
      </div>
    </nav>
<p>You chose <b>{{active}}</b></p>
  <router-view></router-view>
</div>
</template>

<script>
export default {
  name: 'topMenu',
  data () {
    return {
      active: 'home'
    }
  },
  methods: {
    makeActive: function (item) {
      this.active = item
    }
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

nav.home .home,
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
