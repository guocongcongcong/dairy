<template>
<div id="main">
  <div class="nav-mask">
    <nav :class="active" @click.prevent>
      <a href="#" class="home" @click="makeActive('home')">Home</a>
      <a href="#" class="projects" @click="makeActive('projects')">Projects</a>
      <a href="#" class="services" @click="makeActive('services')">Services</a>
      <a href="#" class="contact" @click="makeActive('contact')">Contact</a>
    </nav>
  </div>
<p>You chose <b>{{active}}</b></p>
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
color: #389dc1;
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
background-color: #7fc9e9;
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
padding: 18px 30px;
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
background-color: #dda1b4;
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
