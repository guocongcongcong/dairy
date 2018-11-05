<template> 
  <div class="hello "> 
    <section>
    <div class='col-md-4'></div>
    <div class='col-md-4'><form class="form-inline">
        <div class="form-group">
            <label for="exampleInputName2">Name</label>
            <input type="text" class="form-control" id="exampleInputName2" placeholder="Jane Doe">
        </div>
        <div class="form-group">
            <label for="exampleInputEmail2">Email</label>
            <input type="email" class="form-control" id="exampleInputEmail2" placeholder="jane.doe@example.com">
        </div>
        <button type="submit" class="btn btn-default">Send invitation</button>
    </form></div>
    <div class='col-md-4'></div>
    </section>
  </div> 
</template> 
   
<script> 
  // $(function () { 
  //   alert(123); 
  // }); 
  export default { 
    name: 'hello', 
    data () { 
      return { 
        msg: 'Welcome to Your Vue.js App' 
      } 
    } 
  } 
</script> 
   
<!-- Add "scoped" attribute to limit CSS to this component only --> 
<style scoped> 
  h1, h2 { 
    font-weight: normal; 
  } 
   
  ul { 
    list-style-type: none; 
    padding: 0; 
  } 
   
  li { 
    display: inline-block; 
    margin: 0 10px; 
  } 
   
  a { 
    color: #42b983; 
  } 
</style>