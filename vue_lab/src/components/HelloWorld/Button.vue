<template>
    <div class='input'>
        <a>{{msg}}</a>
        <input name= 'input1' class = 'input1' />
    </div>
</template>
<script>
export default {
  name: 'Button',
  data () {
    return {
      msg: '输入框：'
    }
  }
}
</script>

<style scoped>
a {
  color: #42b983;
}
</style>
