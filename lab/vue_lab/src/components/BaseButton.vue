<template>
  <div>
      <button type="button" class="btn btn-info">{{msg}}</button>
  </div>
</template>

<script>
export default {
  name: 'BaseButton',
  data () {
    return {
      msg: 'button'
    }
  }
}
</script>
